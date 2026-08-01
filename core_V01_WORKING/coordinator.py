from agents.analysis_agent import analysis_agent
from agents.right_brain import right_brain
from agents.synthesis_agent import synthesis_agent
from agents.verifier_agent import verifier_agent


class Coordinator:

    def __init__(self):
        self.name = "Central Coordinator"


    def run_cycle(self, message):

        left_result = analysis_agent.run(message)

        right_result = right_brain.run(message)

        synthesis_result = synthesis_agent.synthesize(
            message,
            left_result,
            right_result
        )

        verification_result = verifier_agent.check(
            synthesis_result,
            left_result,
            right_result
        )

        return {
            "left_brain": left_result,
            "right_brain": right_result,
            "synthesis": synthesis_result,
            "verification": verification_result
        }


    def process(self, message):

        results = self.run_cycle(message)

        return {
            "coordinator": self.name,
            "status": "online",
            "input": message,
            "left_brain": results["left_brain"],
            "right_brain": results["right_brain"],
            "synthesis": results["synthesis"],
            "verification": results["verification"],
            "results": results
        }


coordinator = Coordinator()