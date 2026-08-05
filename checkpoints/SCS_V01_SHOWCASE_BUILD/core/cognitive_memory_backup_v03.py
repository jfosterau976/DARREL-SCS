import json
import os


class CognitiveMemory:

    def __init__(self):

        self.name = "SCS Cognitive Memory"

        self.file = "scs_memory.json"

        self.memory = self.load()


    def load(self):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:

                return json.load(f)

        return []


    def save(self):

        with open(self.file, "w") as f:

            json.dump(
                self.memory,
                f,
                indent=4
            )


    def remember(self, experience):

        self.memory.append(experience)

        self.save()

        return {

            "status": "memory_saved",

            "total_memories": len(self.memory)

        }


    def recall(self):

        return self.memory


cognitive_memory = CognitiveMemory()