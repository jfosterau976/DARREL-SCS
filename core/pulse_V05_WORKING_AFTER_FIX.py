from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_agent import synthesis_agent
from core.verifier_engine import verifier_engine
from core.pulse_router import pulse_router


class PulseController:

    def __init__(self):
        self.name = "SCS Pulse Controller"
        self.version = "V0.5"

    def run(self, question, feedback=None):

        print("\n=== SCS PULSE ===")
        print("Question:", question)

        if feedback:
            print("\nFEEDBACK RECEIVED:")
            print(feedback)

        decision = pulse_router.decide(question)

        print("\nROUTER DECISION:")
        print(decision)

        left_result = None
        right_result = None
        synthesis_result = None
        verification_result = None

        # LEFT BRAIN
        if decision["left"]:

            print("\n[LEFT BRAIN] ACTIVE")

            if feedback:
                left_question = (
                    f"{question}\n\n"
                    f"VERIFIER FEEDBACK:\n{feedback}\n\n"
                    "Revise your analysis specifically "
                    "to address this feedback."
                )
            else:
                left_question = question

            left_result = left_brain.think(
                left_question
            )

        # RIGHT BRAIN
        if decision["right"]:

            print("\n[RIGHT BRAIN] ACTIVE")

            if feedback:
                right_question = (
                    f"{question}\n\n"
                    f"VERIFIER FEEDBACK:\n{feedback}\n\n"
                    "Revise your exploration specifically "
                    "to address this feedback."
                )
            else:
                right_question = question

            right_result = right_brain.think(
                right_question
            )

        # SYNTHESIS
        if decision["synthesis"]:

            print("\n[SYNTHESIS] ACTIVE")

            if left_result is None:
                left_result = left_brain.think(question)

            if right_result is None:
                right_result = right_brain.think(question)

            synthesis_result = synthesis_agent.synthesize(
                question,
                left_result,
                right_result
            )

        # VERIFICATION
        if decision["verifier"]:

            print("\n[VERIFIER] ACTIVE")

            target_result = (
                synthesis_result
                or right_result
                or left_result
            )

            if target_result is not None:

                verification_result = verifier_engine.verify(
                    target_result
                )

        return {
            "question": question,
            "decision": decision,

            "left_brain": (
                left_result.to_dict()
                if hasattr(left_result, "to_dict")
                else left_result
            ),

            "right_brain": (
                right_result.to_dict()
                if hasattr(right_result, "to_dict")
                else right_result
            ),

            "synthesis": (
                synthesis_result.to_dict()
                if hasattr(synthesis_result, "to_dict")
                else synthesis_result
            ),

            "verification": (
                verification_result.to_dict()
                if hasattr(verification_result, "to_dict")
                else verification_result
            )
        }


pulse_controller = PulseController()