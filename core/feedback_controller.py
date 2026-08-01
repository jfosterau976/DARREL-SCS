from core.feedback_interpreter import feedback_interpreter


class FeedbackController:

    def __init__(self):
        self.name = "SCS Feedback Controller"


    def process(self, verification):

        if not verification:

            return {
                "status": "no_feedback"
            }

        result = feedback_interpreter.interpret(
            verification
        )

        return {
            "status": "processed",
            "feedback": result
        }


feedback_controller = FeedbackController()