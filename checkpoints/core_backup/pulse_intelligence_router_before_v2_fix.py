class PulseIntelligenceRouter:

    def __init__(self):
        self.name = "SCS Pulse Intelligence Router"


    def route(self, question):

        q = question.lower()

        modules = []

        if any(word in q for word in [
            "should",
            "risk",
            "decision",
            "compare"
        ]):
            modules.extend([
                "left_reasoning",
                "right_reasoning",
                "synthesis",
                "verifier"
            ])

        elif any(word in q for word in [
            "idea",
            "create",
            "design",
            "invent"
        ]):
            modules.extend([
                "right_reasoning",
                "synthesis",
                "verifier"
            ])

        else:
            modules.extend([
                "memory",
                "left_reasoning",
                "verifier"
            ])

        return {
            "router": self.name,
            "question": question,
            "activated_modules": modules,
            "pulse_type": "adaptive"
        }


pulse_router = PulseIntelligenceRouter()