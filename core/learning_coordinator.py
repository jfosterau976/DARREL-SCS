from core.cognitive_memory import cognitive_memory


class LearningCoordinator:

    def __init__(self):
        self.name = "SCS Learning Coordinator"

    def decide_learning_path(self, question):

        memories = cognitive_memory.recall_relevant(
            question
        )

        if len(memories) >= 3:

            mode = "memory_guided"

        elif len(memories) > 0:

            mode = "assisted"

        else:

            mode = "exploration"

        return {

            "system": self.name,

            "mode": mode,

            "memory_matches": len(memories),

            "memory_context": memories,

            "status": "learning_path_selected"

        }


learning_coordinator = LearningCoordinator()