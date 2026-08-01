from core.memory_gate import memory_gate


class LearningCoordinator:

    def __init__(self):
        self.name = "SCS Learning Coordinator"


    def decide_learning_path(self, question):

        memory_result = memory_gate.evaluate(
            question
        )

        if memory_result.get("use_memory"):

            return {
                "mode": "memory_guided",
                "strategy": memory_result.get(
                    "strategy"
                ),
                "confidence": memory_result.get(
                    "confidence"
                )
            }


        return {
            "mode": "fresh_reasoning",
            "strategy": None,
            "confidence": 0
        }


learning_coordinator = LearningCoordinator()