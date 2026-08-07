from core.cognitive_memory import cognitive_memory


class LearningFeedback:

    def __init__(self):

        self.name = "SCS Learning Feedback"
        self.history = []


    def evaluate(self, performance):

        lessons = []


        if performance.get("synthesis"):

            lessons.append(
                "Synthesis successfully combined agent outputs"
            )


        if performance.get("verification"):

            lessons.append(
                "Verification layer completed"
            )


        if performance.get("decision"):

            lessons.append(
                "Decision layer completed"
            )


        score = len(lessons) / 3


        experience = {

            "performance": performance,

            "score": score,

            "lessons": lessons

        }


        self.history.append(experience)


        memory_result = cognitive_memory.remember(
            experience
        )


        return {

            "system": self.name,

            "status": "feedback_complete",

            "performance_score": score,

            "lessons": lessons,

            "memory": memory_result,

            "experiences_stored": len(self.history)

        }


    def recall_lessons(self):

        return self.history



learning_feedback = LearningFeedback()