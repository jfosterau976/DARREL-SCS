class SelectiveActivationEngine:

    def __init__(self):
        self.name = "SCS Selective Activation Engine"

    def activate(self, complexity, risk):

        if complexity == "high" or risk == "high":

            modules = [
                "goal_planning",
                "left_reasoning",
                "right_reasoning",
                "synthesis",
                "verifier",
                "reflection",
                "learning"
            ]

        elif complexity == "medium":

            modules = [
                "left_reasoning",
                "right_reasoning",
                "synthesis",
                "verifier"
            ]

        else:

            modules = [
                "left_reasoning",
                "verifier"
            ]

        return {
            "system": self.name,
            "complexity": complexity,
            "risk": risk,
            "activated_modules": modules,
            "activation_mode": "selective",
            "status": "activation_complete"
        }


selective_activation = SelectiveActivationEngine()