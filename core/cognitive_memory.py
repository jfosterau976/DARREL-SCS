import json
import os


class CognitiveMemory:

    def __init__(self):

        self.name = "SCS Cognitive Memory"

        self.file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "scs_memory.json"
        )

        self.memory = self.load()

        print("MEMORY COUNT:", len(self.memory))

    def load(self):

        if os.path.exists(self.file):

            with open(self.file, "r", encoding="utf-8") as file:
                return json.load(file)

        return []

    def save(self):

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(
                self.memory,
                file,
                indent=4,
                ensure_ascii=False
            )

    def memory_identity(self, memory):

        ignored_fields = {
            "strength",
            "importance",
            "timestamp"
        }

        return {
            key: value
            for key, value in memory.items()
            if key not in ignored_fields
        }

    def update_importance(self, memory):

        strength = memory.get("strength", 1)

        if strength >= 10:
            memory["importance"] = "HIGH"

        elif strength >= 3:
            memory["importance"] = "MEDIUM"

        else:
            memory["importance"] = "LOW"

    def remember(self, experience):

        incoming_identity = self.memory_identity(
            experience
        )

        for memory in self.memory:

            existing_identity = self.memory_identity(
                memory
            )

            if existing_identity == incoming_identity:

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

        experience.setdefault("strength", 1)

        self.update_importance(experience)

        self.memory.append(experience)

        self.save()

        return {
            "status": "memory_saved",
            "strength": experience["strength"],
            "importance": experience["importance"],
            "total_memories": len(self.memory)
        }

    def store(self, entry):
        return self.remember(entry)

    def recall(self):
        return self.memory

    def find_memory_type(self, memory_type):

        return [
            memory
            for memory in self.memory
            if memory.get("type") == memory_type
        ]

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

    def score_relevance(self, request, memory):

        request_words = set(
            request.lower().split()
        )

        memory_text = json.dumps(
            memory,
            ensure_ascii=False
        ).lower()

        score = 0

        for word in request_words:

            if word in memory_text:
                score += 1

        score += memory.get("strength", 1)

        return score

    def recall_relevant(self, request, limit=5):

        scored = []

        for memory in self.memory:

            score = self.score_relevance(
                request,
                memory
            )

            if score > 0:

                scored.append({
                    "score": score,
                    "memory": memory
                })

        scored.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return scored[:limit]


cognitive_memory = CognitiveMemory()