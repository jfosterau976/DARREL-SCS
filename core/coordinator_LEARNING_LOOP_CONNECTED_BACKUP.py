from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_agent import synthesis_agent
from core.verifier_engine import verifier_engine
from core.reflection_agent import reflection_agent
from core.memory_consolidator import memory_consolidator
from core.learning_feedback import learning_feedback


class Coordinator:

    def __init__(self):

        self.name = "Central Cognitive Workspace"

        self.workspace = {}

    def process(self, request):

        print("\n🧠 Coordinator Workspace Active")

        # Load consolidated memory first
        memory_context = memory_consolidator.consolidate()

        self.workspace["memory"] = memory_context

        # Activate analytical reasoning
        left_result = left_brain.analyse(
            request,
            memory_context.get("concepts", [])
        )

        # Activate creative reasoning
        right_result = right_brain.create(
            request
        )

        # Store agent outputs
        self.workspace["left_brain"] = left_result
        self.workspace["right_brain"] = right_result

        # Synthesis combines both brains + learned reasoning
        synthesis = synthesis_agent.synthesize(
            request,
            left_result,
            right_result
        )

        self.workspace["synthesis"] = synthesis

        # Verification checks synthesis
        verification = verifier_engine.verify(
            synthesis
        )

        self.workspace["verification"] = verification

        # Reflection learns from verification
        reflection = reflection_agent.reflect(
            verification
        )

        self.workspace["reflection"] = reflection


        # Learning feedback stores reasoning experience
        feedback = learning_feedback.evaluate(
            {
                "synthesis": synthesis,
                "verification": verification,
                "reflection": reflection
            }
        )

        self.workspace["learning_feedback"] = feedback

        self.workspace["reflection"] = reflection

        return {
            "coordinator": self.name,
            "status": "workspace_complete",
            "input": request,
            "workspace": self.workspace,
            "agents_used": [
                "left_brain",
                "right_brain",
                "synthesis_agent",
                "verifier_agent",
                "reflection_agent",
                "learning_feedback"
            ]
        }


coordinator = Coordinator()