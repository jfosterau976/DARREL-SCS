import json
import os


class MemoryOptimizer:

    def __init__(self):
        self.name = "SCS Memory Optimizer"
        self.file = "scs_memory.json"


    def optimize(self):

        if not os.path.exists(self.file):
            return {
                "status": "no_memory_found"
            }


        with open(self.file, "r") as f:
            memories = json.load(f)


        unique = []
        seen = set()


        for memory in memories:

            key = json.dumps(
                memory,
                sort_keys=True
            )

            if key not in seen:
                seen.add(key)
                unique.append(memory)


        removed = len(memories) - len(unique)


        with open(self.file, "w") as f:
            json.dump(
                unique,
                f,
                indent=4
            )


        return {
            "optimizer": self.name,
            "status": "memory_optimized",
            "before": len(memories),
            "after": len(unique),
            "removed": removed
        }


memory_optimizer = MemoryOptimizer()