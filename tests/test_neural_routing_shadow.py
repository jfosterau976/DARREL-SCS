import unittest
from unittest.mock import patch

from core.neural_routing_layer import (
    NeuralRoutingLayer,
    neural_routing_layer,
)
from core.pulse import pulse


class NeuralRoutingLayerTests(unittest.TestCase):

    def setUp(self):
        self.layer = NeuralRoutingLayer()

    def test_signal_contract_contains_sixteen_normalized_signals(self):
        signals = self.layer.extract_signals(
            "Design and verify a safe medical assistant."
        )

        self.assertEqual(
            tuple(signals.keys()),
            NeuralRoutingLayer.SIGNAL_NAMES,
        )
        self.assertEqual(len(signals), 16)
        self.assertTrue(
            all(0.0 <= value <= 1.0 for value in signals.values())
        )

    def test_predictions_are_deterministic(self):
        question = "Compare two strategies for an AI assistant."

        first = self.layer.predict(question)
        second = self.layer.predict(question)

        self.assertEqual(first, second)
        self.assertFalse(first["authority"])
        self.assertEqual(first["mode"], "shadow")

    def test_prediction_covers_low_medium_and_high_routes(self):
        low = self.layer.predict("What is 2 plus 2?")
        medium = self.layer.predict(
            "Compare two designs for an AI assistant."
        )
        high = self.layer.predict(
            "Design a safe medical assistant and analyse its risks."
        )

        self.assertEqual(low["prediction"]["complexity"], "low")
        self.assertEqual(
            medium["prediction"]["complexity"],
            "medium",
        )
        self.assertEqual(high["prediction"]["complexity"], "high")

    def test_comparison_reports_module_differences(self):
        shadow = self.layer.predict(
            "Design a safe medical assistant."
        )
        routing = self.authoritative_low_route()
        execution = self.low_execution()

        record = self.layer.compare(shadow, routing, execution)

        self.assertFalse(record["comparison"]["exact_module_match"])
        self.assertIn(
            "goal_planning",
            record["comparison"]["false_positives"],
        )
        self.assertEqual(record["comparison"]["false_negatives"], [])

    def test_pulse_keeps_authoritative_activation(self):
        routing = self.authoritative_low_route()
        shadow = self.layer.predict(
            "Design a safe medical assistant."
        )
        execution = self.low_execution()

        with patch(
            "core.pulse.attention_router.route",
            return_value=routing,
        ), patch(
            "core.pulse.pulse_orchestrator.decide_execution",
            return_value={
                "modules_to_run": ["left_reasoning", "verifier"],
                "status": "execution_plan_created",
            },
        ) as decide_execution, patch(
            "core.pulse.pulse_orchestrator.execute",
            return_value=execution,
        ), patch.object(
            neural_routing_layer,
            "predict",
            return_value=shadow,
        ):
            result = pulse.run("Shadow authority test")

        decide_execution.assert_called_once_with(routing["activation"])
        self.assertEqual(
            result["execution_plan"]["modules_to_run"],
            ["left_reasoning", "verifier"],
        )
        self.assertFalse(
            result["telemetry"]["neural_routing"]["authority"]
        )

    def test_shadow_failure_does_not_block_execution(self):
        routing = self.authoritative_low_route()
        execution = self.low_execution()

        with patch(
            "core.pulse.attention_router.route",
            return_value=routing,
        ), patch(
            "core.pulse.pulse_orchestrator.decide_execution",
            return_value={
                "modules_to_run": ["left_reasoning", "verifier"],
                "status": "execution_plan_created",
            },
        ), patch(
            "core.pulse.pulse_orchestrator.execute",
            return_value=execution,
        ), patch.object(
            neural_routing_layer,
            "predict",
            side_effect=RuntimeError("simulated shadow failure"),
        ):
            result = pulse.run("Shadow failure test")

        self.assertEqual(result["status"], "pulse_complete")
        self.assertEqual(
            result["telemetry"]["neural_routing"]["status"],
            "error",
        )
        self.assertFalse(
            result["telemetry"]["neural_routing"]["authority"]
        )

    def authoritative_low_route(self):
        return {
            "cognitive_state": {
                "complexity": "low",
                "risk": "low",
            },
            "activation": {
                "activated_modules": [
                    "left_reasoning",
                    "verifier",
                ]
            },
        }

    def low_execution(self):
        return {
            "executed_modules": [
                "left_reasoning",
                "verifier",
            ],
            "results": {
                "left_reasoning": {
                    "status": "executed",
                    "output": {},
                },
                "verifier": {
                    "status": "executed",
                    "output": {
                        "verdict": "PASS",
                        "confidence": 0.9,
                    },
                },
            },
            "correction_attempted": False,
            "status": "execution_complete",
        }


if __name__ == "__main__":
    unittest.main()
