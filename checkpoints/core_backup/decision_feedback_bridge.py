from core.feedback_controller import feedback_controller


class DecisionFeedbackBridge:

    def __init__(self):
        self.name = "SCS Decision Feedback Bridge"


    def update_strategy(self, verification):

        feedback = feedback_controller.process(
            verification
        )

        if feedback.get("status") != "processed":

            return {
                "left": True,
                "right": True,
                "synthesis": True,
                "verifier": True
            }


        return feedback["feedback"].get(
            "strategy",
            {
                "left": True,
                "right": False,
                "synthesis": False,
                "verifier": True
            }
        )


decision_feedback_bridge = DecisionFeedbackBridge()