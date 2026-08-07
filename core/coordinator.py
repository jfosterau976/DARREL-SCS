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

        duration_seconds = round(
            time.perf_counter() - start_time,
            3
        )

        activated_modules = pulse_result.get(
            "execution_plan",
            {}
        ).get(
            "modules_to_run",
            []
        )

        cognitive_state = pulse_result.get(
            "cognitive_state",
            {}
        )

        relevant_memories = pulse_result.get(
            "relevant_memories",
            []
        )

        executive_decision = (
            executive.get(
                "executive_decision",
                {}
            )
            if isinstance(
                executive.get(
                    "executive_decision"
                ),
                dict
            )
            else {}
        )

        telemetry = {

            "system": {
                "name": self.name,
                "status": "workspace_complete",
                "started_at": started_at,
                "duration_seconds": duration_seconds
            },

            "pulse": {
                "status": pulse_result.get(
                    "status"
                ),
                "version": pulse_result.get(
                    "version"
                ),
                "complexity": cognitive_state.get(
                    "complexity"
                ),
                "risk": cognitive_state.get(
                    "risk"
                ),
                "memory_required": cognitive_state.get(
                    "memory_required"
                ),
                "verification_required": cognitive_state.get(
                    "verification_required"
                ),
                "reflection_required": cognitive_state.get(
                    "reflection_required"
                ),
                "activated_modules": activated_modules,
                "module_count": len(
                    activated_modules
                )
            },

            "memory": {
                "total_memories": memory.get(
                    "total_memories",
                    0
                ),
                "relevant_memories": len(
                    relevant_memories
                ),
                "top_relevant_memories": (
                    relevant_memories[:3]
                )
            },

            "left_brain": {
                "status": left.get(
                    "status"
                ),
                "mode": left.get(
                    "mode"
                ),
                "confidence": left.get(
                    "confidence"
                ),
                "model": left.get(
                    "llm",
                    {}
                ).get(
                    "model"
                ),
                "llm_status": left.get(
                    "llm",
                    {}
                ).get(
                    "status"
                ),
                "fallback": left.get(
                    "llm",
                    {}
                ).get(
                    "fallback"
                )
            },

            "right_brain": {
                "status": right.get(
                    "status"
                ),
                "mode": right.get(
                    "mode"
                ),
                "confidence": right.get(
                    "confidence"
                ),
                "model": right.get(
                    "llm",
                    {}
                ).get(
                    "model"
                ),
                "llm_status": right.get(
                    "llm",
                    {}
                ).get(
                    "status"
                ),
                "fallback": right.get(
                    "llm",
                    {}
                ).get(
                    "fallback"
                )
            },

            "synthesis": {
                "status": synthesis.get(
                    "status"
                ),
                "mode": synthesis.get(
                    "mode"
                ),
                "model": synthesis.get(
                    "llm",
                    {}
                ).get(
                    "model"
                ),
                "llm_status": synthesis.get(
                    "llm",
                    {}
                ).get(
                    "status"
                ),
                "fallback": synthesis.get(
                    "llm",
                    {}
                ).get(
                    "fallback"
                )
            },

            "verification": {
                "mode": verification.get(
                    "mode"
                ),
                "verdict": verification.get(
                    "verdict"
                ),
                "confidence": verification.get(
                    "confidence"
                )
            },

            "reflection": {
                "status": reflection.get(
                    "status"
                )
            },

            "learning": {
                "status": learning.get(
                    "status"
                ),
                "verdict": learning.get(
                    "verdict"
                ),
                "confidence": learning.get(
                    "confidence"
                )
            },

            "executive": {
                "status": executive.get(
                    "status"
                ),
                "decision": executive_decision.get(
                    "decision"
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