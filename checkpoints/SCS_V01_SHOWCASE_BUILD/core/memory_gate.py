from core.memory_advisor import memory_advisor


class MemoryGate:

    def __init__(self):
        self.name = "SCS Memory Gate"


    def evaluate(self, question):

        advice = memory_advisor.advise(
            question
        )

        if advice.get("status") != "memory_found":

            return {
                "use_memory": False,
                "reason": "no_memory"
            }


        similarity = advice.get(
            "similarity",
            0
        )

        strategy = advice.get(
            "recommended_strategy"
        )


        if similarity >= 3 and strategy:

            return {
                "use_memory": True,
                "reason": "strong_match",
                "strategy": strategy,
                "confidence": similarity
            }


        return {
            "use_memory": False,
            "reason": "weak_match",
            "confidence": similarity
        }


memory_gate = MemoryGate()