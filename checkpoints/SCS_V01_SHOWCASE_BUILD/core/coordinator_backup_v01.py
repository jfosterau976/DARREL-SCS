from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_agent import synthesis_agent
from core.verifier_engine import verifier_engine


class Coordinator:

    def __init__(self):

        self.name = "Central Cognitive Workspace"

        self.workspace = {}


    def process(self, request):

        print("\n🧠 Coordinator Workspace Active")


        # Activate reasoning agent
        left_result = left_brain.analyse(request)


        # Activate creative agent
        right_result = right_brain.create(request)


        # Store agent outputs
        self.workspace["left_brain"] = left_result
        self.workspace["right_brain"] = right_result


        # Synthesis reads workspace
        synthesis = synthesis_agent.synthesize([
            left_result,
            right_result
        ])


        self.workspace["synthesis"] = synthesis


        # Verification checks synthesis
        verification = verifier_engine.verify(
            synthesis
        )


        self.workspace["verification"] = verification


        return {

            "coordinator": self.name,

            "status": "workspace_complete",

            "input": request,

            "workspace": self.workspace,

            "agents_used": [
                "left_brain",
                "right_brain",
                "synthesis_agent",
                "verifier_agent"
            ]

        }


coordinator = Coordinator()