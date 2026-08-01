from core.left_brain import left_brain
from core.right_brain import right_brain
from agents.synthesis_agent import synthesis_agent
from agents.verifier_agent import verifier_agent


class SCS:

    def __init__(self):

        self.name = "Synthetic Cognitive System"
        self.version = "V0.1"

    def think(self, question):

        print("\n=== SCS COGNITIVE CYCLE ===")
        print("QUESTION:", question)

        # 1. Parallel perspectives
        print("\n[1] LEFT BRAIN — ANALYSIS")
        left_result = left_brain.think(question)

        print("[2] RIGHT BRAIN — CREATIVITY")
        right_result = right_brain.think(question)

        # 2. Synthesis
        print("\n[3] SYNTHESIS")
        synthesis_result = synthesis_agent.synthesize(
            question,
            left_result,
            right_result
        )

        # 3. Verification
        print("\n[4] VERIFICATION")
        verification_result = verifier_agent.check(
            synthesis_result
        )

        return {
            "question": question,
            "left_brain": left_result.to_dict(),
            "right_brain": right_result.to_dict(),
            "synthesis": synthesis_result.to_dict(),
            "verification": verification_result.to_dict()
        }


scs = SCS()