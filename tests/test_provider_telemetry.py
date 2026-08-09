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


if __name__ == "__main__":
    unittest.main()
