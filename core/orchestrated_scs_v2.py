from core.cognitive_orchestrator import cognitive_orchestrator
from core.selective_activation_engine import selective_activation
from core.self_managing_scs import self_managing_scs
from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_engine import synthesis_engine
from core.verifier_engine import verifier_engine


class OrchestratedSCSV2:

    def __init__(self):
        self.name = "SCS Orchestrated Cognitive System V2"


    def think(self, question):
       
        print("SCS V2 THINK RUNNING")

        base_result = self_managing_scs.think(question)

        base_result = self_managing_scs.think(question)

        left_result = left_brain.think(question)
        print("LEFT DEBUG:", vars(left_result))

        right_result = right_brain.think(question)

        synthesis_result = synthesis_engine.combine(
            left_result,
            right_result,
            question
        )

        verification_result = verifier_engine.verify(
            synthesis_result
        )

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

            "left_reasoning": vars(left_result),
            "right_reasoning": vars(right_result),
            "synthesis": synthesis_result,
            "verification": verification_result,

            "status": "orchestrated_v2_complete"
        }


orchestrated_scs_v2 = OrchestratedSCSV2()