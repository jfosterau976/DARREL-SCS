class SynthesisAgent:

    def __init__(self):
        self.name = "SCS Synthesis Agent"
        self.role = "integration"

    def synthesize(self, question, left_result, right_result):

        left_text = getattr(left_result, "content", str(left_result))
        right_text = getattr(right_result, "content", str(right_result))

        return {
            "agent": self.name,
            "role": self.role,
            "status": "complete",
            "response": (
                "Combined reasoning:\n\n"
                "LEFT:\n" + left_text +
                "\n\nRIGHT:\n" + right_text
            ),
            "confidence": 0.75
        }


synthesis_agent = SynthesisAgent()