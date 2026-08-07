from core.cognitive_memory import cognitive_memory


class MemoryConsolidator:

    def __init__(self):

        self.name = "SCS Memory Consolidator V3"


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


            concepts[question].append(
                item
            )


        return concepts



    def consolidate(self):

        memories = cognitive_memory.recall()


        grouped = self.find_related(
            memories
        )


        learned_concepts = []

        learned_reasoning = []



        for item in memories:

            if item.get(
                "type"
            ) == "reasoning_feedback":


                learned_reasoning.append(
                    {
                        "verdict": item.get(
                            "verdict",
                            "UNKNOWN"
                        ),

                        "confidence": item.get(
                            "confidence",
                            0
                        ),

                        "lessons": item.get(
                            "lessons",
                            []
                        ),

                        "improvements": item.get(
                            "improvements",
                            []
                        )
                    }
                )



        for topic, items in grouped.items():

            importance = "LOW"


            if len(items) >= 10:

                importance = "HIGH"


            elif len(items) >= 3:

                importance = "MEDIUM"



            strength_total = 0


            for item in items:

                strength_total += item.get(
                    "strength",
                    1
                )



            priority_score = (
                len(items)
                +
                strength_total
            )


            learned_concepts.append(
                {
                    "concept": topic,
                    "evidence_count": len(items),
                    "strength_score": strength_total,
                    "priority_score": priority_score,
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

            "concepts_created": len(
                learned_concepts
            ),

            "concepts": learned_concepts,

            "learned_reasoning": learned_reasoning

        }



memory_consolidator = MemoryConsolidator()