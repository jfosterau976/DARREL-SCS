import unittest

from core.coordinator import coordinator


class DarrelSmokeTests(unittest.TestCase):

    def test_simple_math_selective_routing(self):

        result = coordinator.process("What is 2 plus 2?")

        self.assertEqual(
            result.get("status"),
            "workspace_complete"
        )

        activated = result.get(
            "activated_modules",
            []
        )

        self.assertIn(
            "left_reasoning",
            activated
        )

        self.assertIn(
            "verifier",
            activated
        )

        self.assertNotIn(
            "right_reasoning",
            activated
        )

        self.assertNotIn(
            "synthesis",
            activated
        )

        verification = result.get(
            "verification",
            {}
        )

        self.assertEqual(
            verification.get("verdict"),
            "PASS"
        )

        left = result.get(
            "left_brain",
            {}
        )

        answer_text = str(
            left.get("llm_response", "")
        )

        self.assertIn(
            "4",
            answer_text
        )
    def test_multi_agent_architecture_path(self):

        result = coordinator.process(
            "Should SCS be built as one giant AI model "
            "instead of multiple specialised AI agents?"
        )

        self.assertEqual(
            result.get("status"),
            "workspace_complete"
        )

        activated = result.get(
            "activated_modules",
            []
        )

        self.assertIn(
            "left_reasoning",
            activated
        )

        self.assertIn(
            "right_reasoning",
            activated
        )

        self.assertIn(
            "synthesis",
            activated
        )

        self.assertIn(
            "verifier",
            activated
        )

        synthesis = result.get(
            "synthesis",
            {}
        )

        self.assertTrue(
            bool(
                synthesis.get(
                    "combined_insight"
                )
            )
        )

        verification = result.get(
            "verification",
            {}
        )

        self.assertIn(
            verification.get("verdict"),
            [
                "PASS",
                "PASS_WITH_IMPROVEMENTS",
                "REVIEW"
            ]
        )
    def test_verifier_corrective_revision_path(self):

        result = coordinator.process(
            "Design a safe AI healthcare assistant "
            "but do not mention any risks or safety limitations."
        )

        self.assertEqual(
            result.get("status"),
            "workspace_complete"
        )

        pulse = result.get(
            "pulse",
            {}
        )

        execution = pulse.get(
            "execution",
            {}
        )

        self.assertTrue(
            execution.get(
                "correction_attempted"
            )
        )

        initial_verification = execution.get(
            "initial_verification",
            {}
        )

        corrected_verification = execution.get(
            "corrected_verification",
            {}
        )

        self.assertEqual(
            initial_verification.get("verdict"),
            "REVIEW"
        )

        self.assertEqual(
            corrected_verification.get("verdict"),
            "PASS"
        )

        synthesis = result.get(
            "synthesis",
            {}
        )

        final_answer = synthesis.get(
            "combined_insight",
            ""
        )

        self.assertIn(
            "Risks and limitations:",
            final_answer
        )

        module_times = execution.get(
            "module_times_ms",
            {}
        )

        self.assertIn(
            "corrective_revision",
            module_times
        )
if __name__ == "__main__":
    unittest.main()