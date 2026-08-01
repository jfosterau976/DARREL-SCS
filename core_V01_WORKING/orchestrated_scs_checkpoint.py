
from core.cognitive_orchestrator import cognitive_orchestrator
from core.self_managing_scs import self_managing_scs


class OrchestratedSCS:

    def __init__(self):
        self.name = "SCS Orchestrated Cognitive System"


    def think(self, question):

        result = self_managing_scs.think(question)

        orchestration = cognitive_orchestrator.decide(
            "balanced",
            result["goal"],
            "high"
        )

        return {
            "system": self.name,
            "base_scs_result": result,
            "orchestration": orchestration,
            "status": "orchestrated_complete"
        }


orchestrated_scs = OrchestratedSCS()