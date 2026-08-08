import time
from datetime import datetime

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

        start_time = time.perf_counter()

        started_at = datetime.now().isoformat(
            timespec="seconds"
        )


        # Run Pulse Engine

        pulse_result = pulse.run(question)


        execution = pulse_result.get(
            "execution",
            {}
        )


        results = execution.get(
            "results",
            {}
        )


        activated_modules = pulse_result.get(
            "execution_plan",
            {}
        ).get(
            "modules_to_run",
            []
        )


        # Extract outputs

        left = results.get(
            "left_reasoning",
            {}
        ).get(
            "output",
            {}
        )

        right = results.get(
            "right_reasoning",
            {}
        ).get(
            "output",
            {}
        )

        synthesis = results.get(
            "synthesis",
            {}
        ).get(
            "output",
            {}
        )

        verification = results.get(
            "verifier",
            {}
        ).get(
            "output",
            {}
        )


        reflection = results.get(
            "reflection",
            {}
        ).get(
            "output",
            {}
        )

        learning = results.get(
            "learning",
            {}
        ).get(
            "output",
            {}
        )


        # Respect Pulse decisions

        if (
            "reflection" in activated_modules
            and verification
            and not reflection
        ):

            reflection = reflection_agent.reflect(
                verification
            )


        if (
            "learning" in activated_modules
            and verification
            and not learning
        ):

            learning = learning_feedback.evaluate({

                "synthesis": synthesis,

                "verification": verification,

                "reflection": reflection

            })


        if "memory" in activated_modules:

            memory = memory_consolidator.consolidate()

        else:

            memory = {

                "status": "skipped",

                "reason": "not_required"

            }


        if "executive" in activated_modules:

            executive = scs_executive.process(

                question,

                synthesis,

                verification

            )

        else:

            executive = {

                "status": "skipped",

                "reason": "not_required"

            }



        duration_seconds = round(

            time.perf_counter() - start_time,

            3

        )


        cognitive_state = pulse_result.get(

            "cognitive_state",

            {}

        )


        telemetry = {

            "system": {

                "name": self.name,

                "status": "workspace_complete",

                "started_at": started_at,

                "duration_seconds": duration_seconds

            },

            "pulse": {

                "complexity": cognitive_state.get(
                    "complexity"
                ),

                "risk": cognitive_state.get(
                    "risk"
                ),

                "activated_modules": activated_modules,

                "module_count": len(
                    activated_modules
                )

            }

        }


        return {

            "system": self.name,

            "status": "workspace_complete",

            "question": question,

            "pulse": pulse_result,

            "activated_modules": activated_modules,

            "memory": memory,

            "left_brain": left,

            "right_brain": right,

            "synthesis": synthesis,

            "verification": verification,

            "reflection": reflection,

            "learning": learning,

            "executive": executive,

            "telemetry": telemetry

        }


coordinator = Coordinator()