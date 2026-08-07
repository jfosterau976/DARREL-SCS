from core.cognitive_memory import cognitive_memory


class MemoryConsolidator:

    def __init__(self):
        self.name = "SCS Memory Consolidator"

    def is_noise(self, memory):

        question = str(
            memory.get("question", "")
        ).lower().strip()

        if not question:
            return True

        return question in {
            "test",
            "hello",
            "hello scs",
            "2+2"
        }

    def consolidate(self):

        memories = cognitive_memory.recall()

        concepts = {}
        learned_reasoning = []

        for memory in memories:

            if self.is_noise(memory):
                continue

            if memory.get("type") == "reasoning_feedback":

                learned_reasoning.append({
                    "verdict": memory.get("verdict", "UNKNOWN"),
                    "confidence": memory.get("confidence", 0),
                    "lessons": memory.get("lessons", []),
                    "improvements": memory.get("improvements", [])
                })

            concept = memory.get(
                "question",
                "unknown"
            ).lower().strip()

            if concept not in concepts:

                concepts[concept] = {
                    "concept": concept,
                    "evidence_count": 0,
                    "strength_score": 0
                }

            concepts[concept]["evidence_count"] += 1
            concepts[concept]["strength_score"] += memory.get(
                "strength",
                1
            )

        learned_concepts = []

        for concept in concepts.values():

            concept["priority_score"] = (
                concept["evidence_count"]
                + concept["strength_score"]
            )

            if concept["priority_score"] >= 20:
                concept["importance"] = "HIGH"

            elif concept["priority_score"] >= 6:
                concept["importance"] = "MEDIUM"

            else:
                concept["importance"] = "LOW"

            concept["status"] = "learned"

            learned_concepts.append(concept)

        learned_concepts.sort(
            key=lambda x: x["priority_score"],
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