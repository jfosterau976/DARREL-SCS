from core.left_cognitive_engine import left_engine
from core.right_cognitive_engine import right_engine
from core.synthesis_engine import synthesis_engine
from core.verifier_engine import verifier_engine


class CognitivePulseV1:

    def __init__(self):
        self.name = "SCS Cognitive Pulse V1"


    def run(self, question):

        left_result = left_engine.analyze(question)

        right_result = right_engine.imagine(question)

        synthesis_result = synthesis_engine.combine(
            left_result,
            right_result
        )

        verification_result = verifier_engine.verify(
            synthesis_result
        )


        return {
            "system": self.name,
            "question": question,
            "left": left_result,
            "right": right_result,
            "synthesis": synthesis_result,
            "verification": verification_result
        }


cognitive_pulse = CognitivePulseV1()