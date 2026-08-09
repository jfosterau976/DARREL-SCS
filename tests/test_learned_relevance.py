import unittest
from unittest.mock import patch

from core.left_brain import left_brain


class LearnedReasoningRelevanceTests(unittest.TestCase):

    def learned_memory(self):
        return {
            "concepts": [
                {"concept": "should scs use multiple agents?", "evidence_count": 54, "strength_score": 54, "priority_score": 108, "importance": "HIGH", "status": "learned"},
                {"concept": "should an ai system use multiple specialised agents or one general agent?", "evidence_count": 3, "strength_score": 3, "priority_score": 6, "importance": "MEDIUM", "status": "learned"},
            ],
            "learned_reasoning": [
                {"verdict": "PASS", "confidence": 0.9, "lessons": ["historical lesson"], "improvements": []}
            ],
        }

    def fake_llm_result(self):
        return {"status": "success", "provider": "test", "model": "test-model", "response": "test response", "fallback": False, "metrics": {}}

    def test_irrelevant_strong_learning_is_not_injected(self):
        with patch("core.left_brain.memory_consolidator.consolidate", return_value=self.learned_memory()), patch("core.left_brain.llm_interface.generate", return_value=self.fake_llm_result()):
            result = left_brain.think("Design three innovative features for an AI assistant.", memories=[], think=False)

        self.assertEqual(result["reasoning_context"], [])
        self.assertEqual(result["learned_concepts"], [])

    def test_relevant_learning_is_injected(self):
        with patch("core.left_brain.memory_consolidator.consolidate", return_value=self.learned_memory()), patch("core.left_brain.llm_interface.generate", return_value=self.fake_llm_result()):
            result = left_brain.think("Should SCS use multiple specialised agents instead of one general agent?", memories=[], think=False)

        concepts = [item.get("concept") for item in result["reasoning_context"] if item.get("concept")]
        self.assertIn("should an ai system use multiple specialised agents or one general agent?", concepts)


if __name__ == "__main__":
    unittest.main()
