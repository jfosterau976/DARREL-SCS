import json
import os


class CognitiveMemory:

    def __init__(self, memory_file=None):

        self.name = "SCS Cognitive Memory"

        self.file = os.path.abspath(
            memory_file
            or os.getenv("SCS_MEMORY_FILE")
            or os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "scs_memory.json"
            )
        )

        self.memory = self.load()

        print("MEMORY COUNT:", len(self.memory))


    def load(self):

        if os.path.exists(self.file):

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        return []


    def save(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4,
                ensure_ascii=False
            )


    def recall(self):

        return self.memory



    def recall_relevant(self, request, limit=5):

        simple_patterns = [
            "what is",
            "calculate",
            "plus",
            "minus",
            "times",
            "equals"
        ]

        request_lower = request.lower()


        # Simple questions do not activate memory

        if any(
            pattern in request_lower
            for pattern in simple_patterns
        ):

            return []


        results = []


        for memory in self.memory:

            text = json.dumps(
                memory,
                ensure_ascii=False
            ).lower()


            score = 0


            for word in request_lower.split():

                if word in text:

                    score += 1


            if score > 0:

                results.append(
                    {
                        "score": score,
                        "memory": memory
                    }
                )


        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return results[:limit]



    def store(self, entry):

        self.memory.append(entry)

        self.save()

        return {

            "status": "memory_saved",

            "total_memories": len(self.memory)

        }


    def update_importance(self, memory):

        strength = memory.get("strength", 1)

        if strength >= 10:
            memory["importance"] = "HIGH"

        elif strength >= 3:
            memory["importance"] = "MEDIUM"

        else:
            memory["importance"] = "LOW"


    def strengthen_memory(self, memory_type, lesson):

        for memory in self.memory:

            if (
                memory.get("type") == memory_type
                and memory.get("lesson") == lesson
            ):

                memory["strength"] = memory.get(
                    "strength",
                    1
                ) + 1

                self.update_importance(memory)

                self.save()

                return {
                    "status": "memory_strengthened",
                    "strength": memory["strength"],
                    "importance": memory["importance"],
                    "total_memories": len(self.memory)
                }

        return {
            "status": "memory_not_found",
            "total_memories": len(self.memory)
        }
cognitive_memory = CognitiveMemory()
