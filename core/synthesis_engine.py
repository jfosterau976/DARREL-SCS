from agents.synthesis_agent import SynthesisAgent


class SynthesisEngine:

    def __init__(self):
        self.name = "SCS Synthesis Engine"
        self.agent = SynthesisAgent()

    def combine(self, left_result, right_result, question=""):
        result = self.agent.synthesize(
            question,
            left_result,
            right_result
        )

        return {
            "module": self.name,
            "mode": "synthesis",
            "combined_reasoning": result,
            "confidence": 0.75,
            "status": "active"
        }


synthesis_engine = SynthesisEngine()