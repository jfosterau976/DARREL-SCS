


import json
import os


class MemoryAgent:

    def __init__(self):

        self.name = "SCS Memory Agent"
        self.file = "memory/system_memory.json"


    def load_memory(self):

        if not os.path.exists(self.file):
            return {
                "system": "Synthetic Cognitive System V0.1",
                "memories": []
            }

        with open(self.file, "r") as f:
            return json.load(f)


    def save_memory(self, input_text, result):

        memory = self.load_memory()

        memory["memories"].append({
            "input": input_text,
            "result": result
        })


        os.makedirs(
            "memory",
            exist_ok=True
        )


        with open(self.file, "w") as f:
            json.dump(
                memory,
                f,
                indent=4,
                default=str
            )


        return {
            "agent": self.name,
            "status": "memory_saved",
            "total_memories": len(memory["memories"])
        }


    def recall_memories(self, query):

        memory = self.load_memory()

        matches = []

        query_words = query.lower().split()


        for item in memory["memories"]:

            text = str(item).lower()

            for word in query_words:

                if word in text:
                    matches.append(item)
                    break


        return {
            "agent": self.name,
            "status": "recall_complete",
            "matches_found": len(matches),
            "memories": matches[-5:]
        }


memory_agent = MemoryAgent()