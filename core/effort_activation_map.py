class EffortActivationMap:

    def __init__(self):
        self.name = "SCS Effort Activation Map V1"


    def activate(self, effort_level):

        if effort_level == "high":

            modules = [
                "left_reasoning",
                "right_reasoning",
                "memory",
                "synthesis",
                "verifier",
                "reflection",
                "learning"
            ]


        elif effort_level == "medium":

            modules = [
                "left_reasoning",
                "right_reasoning",
                "memory",
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

            "effort_level": effort_level,

            "activated_modules": modules,

            "activation_count": len(modules)

        }


effort_activation_map = EffortActivationMap()