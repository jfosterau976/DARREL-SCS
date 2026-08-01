from core.memory_retriever import memory_retriever


class MemoryAdvisor:

    def __init__(self):
        self.name = "SCS Memory Advisor"


    def advise(self, question):

        memories = memory_retriever.search(
            question
        )

        if not memories:

            return {
                "status": "no_memory",
                "strategy": None
            }


        best = max(
            memories,
            key=lambda item: item.get(
                "similarity",
                0
            )
        )


        memory = best.get(
            "memory",
            {}
        )


        return {
            "status": "memory_found",
            "similarity": best.get(
                "similarity",
                0
            ),
            "previous_result": memory.get(
                "result"
            ),
            "recommended_strategy": memory.get(
                "strategy"
            )
        }


memory_advisor = MemoryAdvisor()