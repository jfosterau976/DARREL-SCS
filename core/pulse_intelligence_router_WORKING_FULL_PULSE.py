class PulseIntelligenceRouter:

    def __init__(self):
        self.name = "SCS Pulse Intelligence Router V2"

    def route(self, question):
        q = question.lower().strip()

        # Default V2 cognitive pulse:
        # Left + Right + Synthesis + Verification
        modules = [
            "memory",
            "left_reasoning",
            "right_reasoning",
            "synthesis",
            "verifier"
        ]

        # Creative questions can prioritise right reasoning,
        # but still retain synthesis and verification.
        if any(word in q for word in [
            "idea", "create", "design", "invent", "brainstorm"
        ]):
            modules = [
                "memory",
                "right_reasoning",
                "left_reasoning",
                "synthesis",
                "verifier"
            ]

        return {
            "router": self.name,
            "question": question,
            "activated_modules": modules,
            "pulse_type": "v2_full_cognitive"
        }


pulse_router = PulseIntelligenceRouter()