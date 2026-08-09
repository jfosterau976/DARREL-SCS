import unittest
from unittest.mock import patch

from core.cognitive_budget_manager import (
    CognitiveBudgetManager,
    cognitive_budget_manager,
)
from core.coordinator import coordinator
from core.neural_routing_layer import neural_routing_layer
from core.pulse import pulse


class CognitiveBudgetShadowTests(unittest.TestCase):

    def setUp(self):
        self.manager = CognitiveBudgetManager()

    def test_proposes_all_four_tiers(self):
        microscopic = self.manager.propose(
            "What is two plus two?",
            {"complexity": "low", "risk": "low"},
        )
        light = self.manager.propose(
            "Plan a short task.",
            {"complexity": "low", "risk": "low"},
            {"planning_intent": 0.5},
        )
        standard = self.manager.propose(
            "Compare two designs.",
            {"complexity": "medium", "risk": "low"},
        )
        deep = self.manager.propose(
            "Assess a high-risk design.",
            {"complexity": "medium", "risk": "high"},
        )

        self.assertEqual(microscopic["tier"], "microscopic")
        self.assertEqual(light["tier"], "light")
        self.assertEqual(standard["tier"], "standard")
        self.assertEqual(deep["tier"], "deep")

    def test_budget_contract_is_shadow_only(self):
        proposal = self.manager.propose(
            "Analyse this design.",
            {"complexity": "medium", "risk": "low"},
        )

        self.assertEqual(proposal["mode"], "shadow")
        self.assertFalse(proposal["authority"])
        self.assertFalse(proposal["enforced"])
        self.assertEqual(
            set(proposal["limits"]),
            {
                "latency_ms",
                "total_tokens",
                "api_cost_class",
                "model_calls",
                "memory_lookups",
                "tool_calls",
                "modules",
                "verification_passes",
                "correction_passes",
            },
        )

    def test_comparison_detects_overruns(self):
        proposal = self.manager.propose(
            "What is two plus two?",
            {"complexity": "low", "risk": "low"},
        )
        actual_usage = {
            "latency_ms": 2500,
            "total_tokens": 1200,
            "api_cost": None,
            "model_calls": 2,
            "memory_lookups": None,
            "tool_calls": None,
            "modules": 3,
            "verification_passes": 1,
            "correction_passes": 0,
        }

        comparison = self.manager.compare(proposal, actual_usage)

        self.assertEqual(comparison["status"], "compared")
        self.assertFalse(comparison["comparison"]["within_budget"])
        self.assertEqual(
            {
                item["dimension"]
                for item in comparison["comparison"]["overruns"]
            },
            {"latency_ms", "total_tokens", "model_calls", "modules"},
        )

    def test_comparison_reasserts_shadow_contract(self):
        proposal = self.manager.propose(
            "Compare two designs.",
            {"complexity": "medium", "risk": "low"},
        )
        proposal.update({
            "mode": "unexpected",
            "version": "unexpected",
            "authority": True,
            "enforced": True,
        })

        comparison = self.manager.compare(proposal, {})

        self.assertEqual(comparison["mode"], "shadow")
        self.assertEqual(
            comparison["version"],
            CognitiveBudgetManager.VERSION,
        )
        self.assertEqual(comparison["status"], "compared")
        self.assertFalse(comparison["authority"])
        self.assertFalse(comparison["enforced"])

    def test_pulse_keeps_authoritative_activation(self):
        routing = self.authoritative_low_route()
        execution = self.low_execution()
        shadow_prediction = neural_routing_layer.predict(
            "Design and verify a safe system."
        )
        budget_proposal = self.manager.propose(
            "Design and verify a safe system.",
            {"complexity": "high", "risk": "high"},
        )

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
            return_value=shadow_prediction,
        ), patch.object(
            cognitive_budget_manager,
            "propose",
            return_value=budget_proposal,
        ):
            result = pulse.run("Budget authority test")

        decide_execution.assert_called_once_with(routing["activation"])
        self.assertEqual(
            result["execution_plan"]["modules_to_run"],
            ["left_reasoning", "verifier"],
        )
        self.assertFalse(
            result["telemetry"]["cognitive_budget"]["authority"]
        )
        self.assertFalse(
            result["telemetry"]["cognitive_budget"]["enforced"]
        )

    def test_budget_failure_does_not_block_execution(self):
        routing = self.authoritative_low_route()
        execution = self.low_execution()
        shadow_prediction = neural_routing_layer.predict(
            "Budget failure test"
        )

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
            return_value=shadow_prediction,
        ), patch.object(
            cognitive_budget_manager,
            "propose",
            side_effect=RuntimeError("simulated budget failure"),
        ):
            result = pulse.run("Budget failure test")

        self.assertEqual(result["status"], "pulse_complete")
        self.assertEqual(
            result["telemetry"]["cognitive_budget"]["status"],
            "error",
        )
        self.assertFalse(
            result["telemetry"]["cognitive_budget"]["authority"]
        )

    def test_coordinator_enriches_budget_actual_usage(self):
        proposal = self.manager.propose(
            "Compare two designs.",
            {"complexity": "medium", "risk": "low"},
        )
        pulse_result = {
            "cognitive_state": {
                "complexity": "medium",
                "risk": "low",
            },
            "execution_plan": {
                "modules_to_run": ["left_reasoning", "verifier"],
            },
            "execution": {
                "results": {
                    "left_reasoning": {
                        "output": {
                            "llm": {
                                "provider": "mock",
                                "model": "mock-model",
                                "status": "success",
                                "metrics": {
                                    "input_tokens": 10,
                                    "output_tokens": 5,
                                    "prompt_eval_count": 4,
                                    "eval_count": 3,
                                },
                            }
                        }
                    },
                    "verifier": {
                        "output": {
                            "verdict": "PASS",
                            "confidence": 0.9,
                        }
                    },
                },
                "initial_verification": {"verdict": "REVIEW"},
                "corrected_verification": {"verdict": "PASS"},
                "correction_attempted": True,
                "status": "execution_complete",
            },
            "telemetry": {
                "cognitive_budget": proposal,
            },
        }

        with patch(
            "core.coordinator.pulse.run",
            return_value=pulse_result,
        ):
            result = coordinator.process("Compare two designs.")

        budget = result["telemetry"]["cognitive_budget"]
        self.assertEqual(budget["status"], "compared")
        self.assertFalse(budget["authority"])
        self.assertFalse(budget["enforced"])
        self.assertEqual(budget["actual_usage"]["total_tokens"], 22)
        self.assertEqual(budget["actual_usage"]["model_calls"], 1)
        self.assertEqual(budget["actual_usage"]["modules"], 2)
        self.assertEqual(budget["actual_usage"]["verification_passes"], 2)
        self.assertEqual(budget["actual_usage"]["correction_passes"], 1)
        self.assertEqual(
            result["pulse"]["telemetry"]["cognitive_budget"],
            budget,
        )

    def test_coordinator_comparison_failure_reasserts_shadow_contract(self):
        proposal = self.manager.propose(
            "Compare two designs.",
            {"complexity": "medium", "risk": "low"},
        )
        proposal.update({
            "mode": "unexpected",
            "version": "unexpected",
            "authority": True,
            "enforced": True,
        })
        pulse_result = {
            "cognitive_state": {
                "complexity": "medium",
                "risk": "low",
            },
            "execution_plan": {
                "modules_to_run": [],
            },
            "execution": {
                "results": {},
                "correction_attempted": False,
                "status": "execution_complete",
            },
            "telemetry": {
                "cognitive_budget": proposal,
            },
        }

        with patch(
            "core.coordinator.pulse.run",
            return_value=pulse_result,
        ), patch.object(
            cognitive_budget_manager,
            "compare",
            side_effect=RuntimeError("simulated comparison failure"),
        ):
            result = coordinator.process("Compare two designs.")

        budget = result["telemetry"]["cognitive_budget"]

        self.assertEqual(budget["mode"], "shadow")
        self.assertEqual(
            budget["version"],
            CognitiveBudgetManager.VERSION,
        )
        self.assertEqual(budget["status"], "error")
        self.assertFalse(budget["authority"])
        self.assertFalse(budget["enforced"])

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
            "initial_verification": {"verdict": "PASS"},
            "corrected_verification": None,
            "status": "execution_complete",
        }


if __name__ == "__main__":
    unittest.main()
