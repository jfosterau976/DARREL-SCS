import unittest
from unittest.mock import patch

from core.coordinator import coordinator


class ProviderTelemetryContractTests(unittest.TestCase):

    def test_coordinator_preserves_provider_fallback_metadata(self):

        fake_pulse_result = {
            "execution": {
                "results": {
                    "left_reasoning": {
                        "output": {
                            "llm": {
                                "status": "success",
                                "provider": "ollama",
                                "requested_provider": "anthropic",
                                "actual_provider": "ollama",
                                "model": "qwen3:1.7b",
                                "fallback": True,
                                "fallback_used": True,
                                "fallback_reason": "simulated anthropic failure",
                                "metrics": {
                                    "prompt_eval_count": 10,
                                    "eval_count": 4
                                }
                            }
                        }
                    }
                }
            },
            "execution_plan": {
                "modules_to_run": [
                    "left_reasoning"
                ]
            },
            "cognitive_state": {
                "complexity": "low",
                "risk": "low"
            }
        }

        with patch(
            "core.coordinator.pulse.run",
            return_value=fake_pulse_result
        ):
            result = coordinator.process(
                "Telemetry contract test"
            )

        telemetry = result["telemetry"]["llm"]

        self.assertTrue(
            telemetry["fallback_used"]
        )

        self.assertEqual(
            telemetry["llm_call_count"],
            1
        )

        call = telemetry["calls"][0]

        self.assertEqual(
            call["requested_provider"],
            "anthropic"
        )

        self.assertEqual(
            call["actual_provider"],
            "ollama"
        )

        self.assertTrue(
            call["fallback_used"]
        )

        self.assertEqual(
            call["fallback_reason"],
            "simulated anthropic failure"
        )

        self.assertEqual(
            call["provider"],
            "ollama"
        )

        self.assertEqual(
            call["data_quality"],
            {
                "valid": True,
                "normalized_fields": [],
            },
        )

    def test_direct_provider_failure_is_not_reported_as_provider_fallback(self):

        fake_pulse_result = {
            "execution": {
                "results": {
                    "left_reasoning": {
                        "output": {
                            "llm": {
                                "status": "connection_error",
                                "provider": "ollama",
                                "requested_provider": "ollama",
                                "actual_provider": "ollama",
                                "model": "qwen3:1.7b",
                                "fallback": True,
                                "fallback_used": False,
                                "fallback_reason": None,
                                "metrics": {}
                            }
                        }
                    }
                }
            },
            "execution_plan": {
                "modules_to_run": [
                    "left_reasoning"
                ]
            },
            "cognitive_state": {
                "complexity": "low",
                "risk": "low"
            }
        }

        with patch(
            "core.coordinator.pulse.run",
            return_value=fake_pulse_result
        ):
            result = coordinator.process(
                "Direct provider failure telemetry test"
            )

        telemetry = result["telemetry"]["llm"]
        call = telemetry["calls"][0]

        self.assertFalse(telemetry["fallback_used"])
        self.assertTrue(call["fallback"])
        self.assertFalse(call["fallback_used"])
        self.assertEqual(call["requested_provider"], "ollama")
        self.assertEqual(call["actual_provider"], "ollama")

    def test_malformed_provider_metrics_do_not_break_telemetry(self):
        fake_pulse_result = self.pulse_result({
            "status": "success",
            "provider": "ollama",
            "requested_provider": "ollama",
            "actual_provider": "ollama",
            "model": "qwen3:1.7b",
            "fallback": False,
            "fallback_used": False,
            "fallback_reason": None,
            "metrics": "unavailable",
        })

        with patch(
            "core.coordinator.pulse.run",
            return_value=fake_pulse_result,
        ):
            result = coordinator.process("Malformed provider metrics")

        telemetry = result["telemetry"]["llm"]
        call = telemetry["calls"][0]

        self.assertEqual(telemetry["llm_call_count"], 1)
        self.assertEqual(telemetry["input_tokens"], 0)
        self.assertEqual(call["metrics"], {})
        self.assertEqual(
            call["data_quality"]["normalized_fields"],
            ["metrics"],
        )

    def test_invalid_metric_and_fallback_values_are_normalized(self):
        fake_pulse_result = self.pulse_result({
            "status": "success",
            "provider": "ollama",
            "requested_provider": "ollama",
            "actual_provider": "ollama",
            "model": "qwen3:1.7b",
            "fallback": "false",
            "fallback_used": "false",
            "fallback_reason": None,
            "metrics": {
                "input_tokens": "ten",
                "output_tokens": -1,
                "prompt_eval_count": float("inf"),
                "eval_count": 3,
            },
        })

        with patch(
            "core.coordinator.pulse.run",
            return_value=fake_pulse_result,
        ):
            result = coordinator.process("Invalid provider telemetry")

        telemetry = result["telemetry"]["llm"]
        call = telemetry["calls"][0]

        self.assertFalse(telemetry["fallback_used"])
        self.assertFalse(call["fallback"])
        self.assertFalse(call["fallback_used"])
        self.assertEqual(telemetry["input_tokens"], 0)
        self.assertEqual(telemetry["output_tokens"], 0)
        self.assertEqual(telemetry["prompt_tokens"], 0)
        self.assertEqual(telemetry["eval_tokens"], 3)
        self.assertIsNone(call["metrics"]["input_tokens"])
        self.assertIsNone(call["metrics"]["output_tokens"])
        self.assertIsNone(call["metrics"]["prompt_eval_count"])
        self.assertEqual(
            call["data_quality"]["normalized_fields"],
            [
                "fallback",
                "fallback_used",
                "metrics.input_tokens",
                "metrics.output_tokens",
                "metrics.prompt_eval_count",
            ],
        )

    def test_missing_provider_identities_are_normalized_visibly(self):
        fake_pulse_result = self.pulse_result({
            "status": "success",
            "provider": "ollama",
            "model": "qwen3:1.7b",
            "fallback": False,
            "fallback_used": False,
            "fallback_reason": None,
            "metrics": {},
        })

        with patch(
            "core.coordinator.pulse.run",
            return_value=fake_pulse_result,
        ):
            result = coordinator.process("Missing provider identities")

        call = result["telemetry"]["llm"]["calls"][0]

        self.assertEqual(call["provider"], "ollama")
        self.assertEqual(call["requested_provider"], "ollama")
        self.assertEqual(call["actual_provider"], "ollama")
        self.assertEqual(
            call["data_quality"]["normalized_fields"],
            ["actual_provider", "requested_provider"],
        )

    def pulse_result(self, llm_result):
        return {
            "execution": {
                "results": {
                    "left_reasoning": {
                        "output": {
                            "llm": llm_result,
                        }
                    }
                }
            },
            "execution_plan": {
                "modules_to_run": ["left_reasoning"],
            },
            "cognitive_state": {
                "complexity": "low",
                "risk": "low",
            },
        }


if __name__ == "__main__":
    unittest.main()
