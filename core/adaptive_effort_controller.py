class AdaptiveEffortController:

    def __init__(self):
        self.name = "SCS Adaptive Effort Controller V1"


    def evaluate(self, signals):

        complexity = signals.get(
            "complexity",
            "low"
        )

        risk = signals.get(
            "risk",
            "low"
        )

        memory_count = signals.get(
            "memory_count",
            0
        )

        uncertainty = signals.get(
            "uncertainty",
            "low"
        )


        score = 0


        if complexity == "medium":
            score += 1

        elif complexity == "high":
            score += 2


        if risk == "high":
            score += 2


        if memory_count > 10:
            score += 1


        if uncertainty == "high":
            score += 2


        if score >= 4:

            effort = "high"

        elif score >= 2:

            effort = "medium"

        else:

            effort = "low"


        return {

            "controller": self.name,

            "effort_level": effort,

            "score": score,

            "signals": signals

        }


adaptive_effort_controller = AdaptiveEffortController()