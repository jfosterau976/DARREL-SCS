from core.cognitive_memory import cognitive_memory


class MemoryConsolidator:

    def __init__(self):
        self.name = "SCS Memory Consolidator V2"


    def is_noise(self, memory):

        question = str(
            memory.get("question", "")
        ).lower().strip()

        if question == "":
            return True

        noise_words = [
            "test",
            "hello",
            "hello scs",
            "2+2"
        ]

        if question in noise_words:
            return True

        return False


    def find_related(self, memories):

        concepts = {}

        for item in memories:

            if self.is_noise(item):
                continue

            question = item.get(
                "question",
                "unknown"
            ).lower().strip()


            if question not in concepts:

                concepts[question] = []


            concepts[question].append(item)


        return concepts


    def consolidate(self):

        memories = cognitive_memory.recall()


        grouped = self.find_related(
            memories
        )


        learned_concepts = []


        for topic, items in grouped.items():

            importance = "LOW"

            if len(items) >= 10:
                importance = "HIGH"

            elif len(items) >= 3:
                importance = "MEDIUM"


            learned_concepts.append(
                {
                    "concept": topic,
                    "evidence_count": len(items),
                    "importance": importance,
                    "status": "learned"
                }
            )


        learned_concepts.sort(
            key=lambda x: x["evidence_count"],
            reverse=True
        )


        return {
            "system": self.name,
            "total_memories": len(memories),
            "concepts_created": len(learned_concepts),
            "concepts": learned_concepts
        }


memory_consolidator = MemoryConsolidator()