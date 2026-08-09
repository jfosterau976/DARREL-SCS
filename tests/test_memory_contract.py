import os
import tempfile
import unittest
from unittest.mock import patch

from core.cognitive_memory import CognitiveMemory


class MemoryContractTests(unittest.TestCase):

    def make_memory(self, entries, path):
        memory = CognitiveMemory.__new__(CognitiveMemory)
        memory.name = "Test Memory"
        memory.file = path
        memory.memory = entries
        return memory

    def test_relevant_memory_is_retrieved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "memory.json")
            memory = self.make_memory([
                {"topic": "ai assistant", "lesson": "use selective computation"},
                {"topic": "gardening", "lesson": "water tomatoes"}
            ], path)

            result = memory.recall_relevant(
                "Design an AI assistant using selective computation"
            )

            self.assertTrue(result)
            self.assertEqual(result[0]["memory"]["topic"], "ai assistant")

    def test_irrelevant_memory_is_skipped(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "memory.json")
            memory = self.make_memory([
                {"topic": "gardening", "lesson": "water tomatoes"}
            ], path)

            result = memory.recall_relevant(
                "Design quantum circuit architecture"
            )

            self.assertEqual(result, [])

    def test_simple_question_bypasses_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "memory.json")
            memory = self.make_memory([
                {"topic": "math", "lesson": "two plus two is four"}
            ], path)

            result = memory.recall_relevant("what is two plus two?")
            self.assertEqual(result, [])

    def test_memory_persists_and_reloads(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "memory.json")
            memory = self.make_memory([], path)

            result = memory.store({
                "type": "test_lesson",
                "lesson": "persistent memory works"
            })

            self.assertEqual(result["status"], "memory_saved")

            reloaded = CognitiveMemory.__new__(CognitiveMemory)
            reloaded.file = path
            reloaded.memory = reloaded.load()

            self.assertEqual(len(reloaded.memory), 1)
            self.assertEqual(
                reloaded.memory[0]["lesson"],
                "persistent memory works"
            )

    def test_environment_override_isolates_persistent_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            isolated_path = os.path.join(directory, "scs_memory.json")

            with patch.dict(
                os.environ,
                {"SCS_MEMORY_FILE": isolated_path}
            ):
                memory = CognitiveMemory()
                result = memory.store({
                    "type": "test_lesson",
                    "lesson": "isolated memory works"
                })

            self.assertEqual(result["status"], "memory_saved")
            self.assertEqual(memory.file, os.path.abspath(isolated_path))
            self.assertTrue(os.path.exists(isolated_path))

            reloaded = self.make_memory([], isolated_path)
            reloaded.memory = reloaded.load()
            self.assertEqual(
                reloaded.memory[0]["lesson"],
                "isolated memory works"
            )


if __name__ == "__main__":
    unittest.main()
