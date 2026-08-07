class CognitiveEffortController:

    def __init__(self):
        self.name = "SCS Cognitive Effort Controller V1"


    def calculate(self, cognitive_state):

        complexity = cognitive_state.get(
            "complexity",
            "low"
        )

        risk = cognitive_state.get(
            "risk",
            "low"
        )


        if risk == "high":

            effort = "high"


        elif complexity == "high":

            effort = "high"


        elif complexity == "medium":

            effort = "medium"


        else:

            effort = "low"


        return {

            "controller": self.name,

            "effort_level": effort,

            "reason": {
                "complexity": complexity,
                "risk": risk
            }

        }


cognitive_effort_controller = CognitiveEffortController()