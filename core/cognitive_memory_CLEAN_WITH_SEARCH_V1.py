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

        print("MEMORY FILE:", self.file)
        print("MEMORY COUNT:", len(self.memory))


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

        if experience in self.memory:

            return {
                "status": "duplicate_memory_skipped",
                "total_memories": len(self.memory)
            }


        self.memory.append(experience)

        self.save()


        return {
            "status": "memory_saved",
            "total_memories": len(self.memory)
        }


    def store(self, entry):

        return self.remember(entry)


    def find_memory_type(self, memory_type):

        matches = []


        for memory in self.memory:

            if memory.get("type") == memory_type:

                matches.append(memory)


        return matches


    def score_relevance(self, request, memory):

        request_words = set(
            request.lower().split()
        )

        memory_text = str(memory).lower()

        score = 0


        for word in request_words:

            if word in memory_text:

                score += 1


        return score


    def recall_relevant(self, request, limit=5):

        scored = []


        for memory in self.memory:

            score = self.score_relevance(
                request,
                memory
            )


            if score > 0:

                scored.append(
                    {
                        "score": score,
                        "memory": memory
                    }
                )


        scored.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        if scored:

            return scored[:limit]


        return [
            {
                "score": 0,
                "memory": memory
            }
            for memory in self.memory[-limit:]
        ]


    def recall(self):

        return self.memory



cognitive_memory = CognitiveMemory()