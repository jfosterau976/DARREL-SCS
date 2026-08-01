from core.cognitive_memory import cognitive_memory


class MemoryRetriever:

    def __init__(self):
        self.name = "SCS Memory Retriever"


    def search(self, question):

        memories = cognitive_memory.recall()

        matches = []

        question_words = set(
            question.lower().split()
        )

        for memory in memories:

            old_question = memory.get(
                "question",
                ""
            ).lower()

            old_words = set(
                old_question.split()
            )

            overlap = len(
                question_words.intersection(old_words)
            )

            if overlap > 0:

                matches.append(
                    {
                        "memory": memory,
                        "similarity": overlap
                    }
                )

        return matches


memory_retriever = MemoryRetriever()