import json
import os


class CognitiveMemory:

    def __init__(self):
        self.name = "SCS Cognitive Memory"
        self.file = "scs_memory.json"


    def load(self):

        if not os.path.exists(self.file):

            return []

        with open(
            self.file,
            "r"
        ) as memory_file:

            return json.load(
                memory_file
            )


    def save(self, memories):

        with open(
            self.file,
            "w"
        ) as memory_file:

            json.dump(
                memories,
                memory_file,
                indent=4
            )


    def store(self, entry):

        memories = self.load()

        memories.append(
            entry
        )

        self.save(
            memories
        )

        return {
            "status": "stored",
            "total_memories": len(memories)
        }


    def recall(self):

        return self.load()


cognitive_memory = CognitiveMemory()