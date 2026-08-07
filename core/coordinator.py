from core.pulse import pulse
from core.memory_consolidator import memory_consolidator
from core.reflection_agent import reflection_agent
from core.learning_feedback import learning_feedback
from core.scs_executive import scs_executive


class Coordinator:

    def __init__(self):
        self.name = "SCS Central Coordinator"

    def process(self, question):

        print("\n=== SCS COORDINATOR ===")

        pulse_result = pulse.run(question)

        execution = pulse_result.get(
            "execution",
            {}
        )

        results = execution.get(
            "results",
            {}
        )

        left = results.get(
            "left_reasoning",
            {}
        ).get("output", {})

        right = results.get(
            "right_reasoning",
            {}
        ).get("output", {})

        synthesis = results.get(
            "synthesis",
            {}
        ).get("output", {})

        verification = results.get(
            "verifier",
            {}
        ).get("output", {})

        reflection = results.get(
            "reflection",
            {}
        ).get("output", {})

        learning = results.get(
            "learning",
            {}
        ).get("output", {})

        if verification and not reflection:
            reflection = reflection_agent.reflect(
                verification
            )

        if verification and not learning:
            learning = learning_feedback.evaluate({
                "synthesis": synthesis,
                "verification": verification,
                "reflection": reflection
            })

        memory = memory_consolidator.consolidate()

        executive = scs_executive.process(
            question,
            synthesis,
            verification
        )

        return {
            "system": self.name,
            "status": "workspace_complete",
            "question": question,
            "pulse": pulse_result,
            "activated_modules": pulse_result.get(
                "execution_plan",
                {}
            ).get("modules_to_run", []),
            "memory": memory,
            "left_brain": left,
            "right_brain": right,
            "synthesis": synthesis,
            "verification": verification,
            "reflection": reflection,
            "learning": learning,
            "executive": executive
        }


coordinator = Coordinator()