import json
import os
from datetime import datetime


class ImprovementMemory:

    def __init__(self):
        self.name = "SCS Improvement Memory"
        self.file = "memory/improvement_memory.json"


    def save_improvement(self, recommendation):

        memory = self.load_memory()

        entry = {
            "timestamp": str(datetime.now()),
            "recommendation": recommendation
        }

        memory["improvements"].append(entry)

        with open(self.file, "w") as f:
            json.dump(memory, f, indent=4)

        return {
            "agent": self.name,
            "status": "improvement_saved",
            "total_improvements": len(memory["improvements"])
        }


    def load_memory(self):

        if not os.path.exists(self.file):
            return {
                "system": "Synthetic Cognitive System V0.1",
                "improvements": []
            }

        with open(self.file, "r") as f:
            return json.load(f)


improvement_memory = ImprovementMemory()