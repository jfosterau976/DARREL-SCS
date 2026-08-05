from core.left_cognitive_engine import left_engine
from core.right_cognitive_engine import right_engine
from core.synthesis_engine import synthesis_engine
from core.verifier_engine import verifier_engine


class SelectivePulseEngine:

    def __init__(self):
        self.name = "SCS Selective Pulse Engine"


    def run(self, question, modules):

        result = {
            "system": self.name,
            "question": question,
            "activated_modules": modules
        }

        left = None
        right = None
        synthesis = None
        verification = None


        if "left_reasoning" in modules:
            left = left_engine.analyze(question)
            result["left"] = left


        if "right_reasoning" in modules:
            right = right_engine.imagine(question)
            result["right"] = right


        if "synthesis" in modules and left and right:
            synthesis = synthesis_engine.combine(
                left,
                right
            )
            result["synthesis"] = synthesis


        if "verifier" in modules and synthesis:
            verification = verifier_engine.verify(
                synthesis
            )
            result["verification"] = verification


        result["status"] = "selective_pulse_complete"

        return result


selective_pulse_engine = SelectivePulseEngine()