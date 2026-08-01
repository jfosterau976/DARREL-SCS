from core.left_brain import left_brain
from core.right_brain import right_brain
from core.persistent_memory import persistent_memory

from agents.synthesis_agent import synthesis_agent
from agents.verifier_agent import verifier_agent


class Coordinator:

    def __init__(self):
        self.name = "Central Coordinator"
        self.status = "online"
        self.max_revision_cycles = 1

    def run_cycle(self, message):

        left_result = left_brain.think(message)

        right_result = right_brain.think(message)

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

        cycle_count = 1

        results = self.run_cycle(message)

        # -----------------------------------------
        # FEEDBACK LOOP
        # -----------------------------------------

        if (
            results["verification"]["status"] == "needs_review"
            and cycle_count <= self.max_revision_cycles
        ):

            feedback = results["verification"].get(
                "warnings",
                []
            )

            revision_message = (
                f"{message}\n\n"
                "A previous cognitive cycle produced a result "
                "that requires review.\n\n"
                f"Verifier feedback:\n{feedback}\n\n"
                "Reconsider the problem. Correct unsupported "
                "assumptions and produce a stronger answer."
            )

            cycle_count += 1

            revised = self.run_cycle(revision_message)

            results["revision"] = revised

            results["final"] = revised["synthesis"]

            results["final_verification"] = revised["verification"]

        else:

            results["final"] = results["synthesis"]

            results["final_verification"] = results["verification"]

        # -----------------------------------------
        # MEMORY
        # -----------------------------------------

        try:
            persistent_memory.remember(
                message,
                {
                    "cycles": cycle_count,
                    "results": results
                }
            )
        except Exception:
            pass

        return {
            "coordinator": self.name,
            "status": self.status,
            "input": message,
            "cycles": cycle_count,
            "results": results
        }


coordinator = Coordinator()