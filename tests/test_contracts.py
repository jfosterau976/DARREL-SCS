import unittest

from core.coordinator import coordinator


class DarrelContractTests(unittest.TestCase):

    def test_coordinator_top_level_contract(self):

        result = coordinator.process(
            "Should SCS use multiple specialised agents?"
        )

        expected_keys = {
            "system",
            "status",
            "question",
            "pulse",
            "activated_modules",
            "memory",
            "left_brain",
            "right_brain",
            "synthesis",
            "verification",
            "reflection",
            "learning",
            "executive",
            "telemetry",
        }

        self.assertTrue(
            expected_keys.issubset(
                result.keys()
            )
        )

        self.assertEqual(
            result.get("status"),
            "workspace_complete"
        )

    def test_pulse_execution_contract(self):

        result = coordinator.process(
            "Should SCS use multiple specialised agents?"
        )

        pulse = result.get(
            "pulse",
            {}
        )

        self.assertIn(
            "execution",
            pulse
        )

        execution = pulse.get(
            "execution",
            {}
        )

        expected_execution_keys = {
            "orchestrator",
            "executed_modules",
            "module_times_ms",
            "results",
            "complexity",
            "reasoning_think_mode",
            "synthesis_think_mode",
            "correction_attempted",
            "initial_verification",
            "corrected_verification",
            "status",
        }

        self.assertTrue(
            expected_execution_keys.issubset(
                execution.keys()
            )
        )

        self.assertEqual(
            execution.get("status"),
            "execution_complete"
        )

    def test_verifier_contract(self):

        result = coordinator.process(
            "Design a safe AI healthcare assistant."
        )

        verification = result.get(
            "verification",
            {}
        )

        expected_verifier_keys = {
            "verdict",
            "confidence",
            "critical_issues",
            "warnings",
            "improvements",
        }

        self.assertTrue(
            expected_verifier_keys.issubset(
                verification.keys()
            )
        )

        self.assertIn(
            verification.get("verdict"),
            [
                "PASS",
                "PASS_WITH_IMPROVEMENTS",
                "REVIEW",
            ]
        )


if __name__ == "__main__":
    unittest.main()