
from core.pulse_router import pulse_router
from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_engine import synthesis_engine
from core.verifier_engine import verifier_engine
from core.decision_engine import decision_engine


class SelectivePulseEngine:

    def __init__(self):
        self.name = "SCS Selective Pulse Engine"

    def run(self, question, modules):

        result = {
            "system": self.name,
            "activated_modules": modules,
            "status": "active"
        }

        left = None
        right = None
        synthesis = None
        verification = None

        if "left_reasoning" in modules:
            left = left_brain.think(question)
            result["left"] = left

        if "right_reasoning" in modules:
            right = right_brain.think(question)
            result["right"] = right

        if "synthesis" in modules and left and right:
            synthesis = synthesis_engine.combine(
                left,
                right,
                question
            )
            result["synthesis"] = synthesis

        if "verifier" in modules and synthesis:
            verification = verifier_engine.verify(
                synthesis
            )
            result["verification"] = verification

        if synthesis and verification:
            decision = decision_engine.decide(
                question,
                synthesis,
                verification
            )
            result["decision"] = decision

        result["status"] = "selective_pulse_complete"

        return result


selective_pulse_engine = SelectivePulseEngine()