from core.cognitive_orchestrator import cognitive_orchestrator
from core.selective_activation_engine import selective_activation
from core.self_managing_scs import self_managing_scs


class OrchestratedSCSV2:

    def __init__(self):
        self.name = "SCS Orchestrated Cognitive System V2"


    def think(self, question):

        base_result = self_managing_scs.think(question)

        complexity = "high"
        risk = "high"

        activation = selective_activation.activate(
            complexity,
            risk
        )

        orchestration = cognitive_orchestrator.decide(
            "balanced",
            base_result["goal"],
            complexity
        )

        return {
            "system": self.name,
            "question": question,
            "activation": activation,
            "orchestration": orchestration,
            "answer": base_result.get("pulse", {}),
            "base_result": base_result,
            "status": "orchestrated_v2_complete"
        }


orchestrated_scs_v2 = OrchestratedSCSV2()