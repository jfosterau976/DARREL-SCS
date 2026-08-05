from core.cognitive_orchestrator import cognitive_orchestrator
from core.selective_activation_engine import selective_activation
from core.self_managing_scs import self_managing_scs
from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_engine import synthesis_engine
from core.verifier_engine import verifier_engine
from core.cognitive_output_formatter import cognitive_output_formatter


class OrchestratedSCSV2:

    def __init__(self):
        self.name = "SCS Orchestrated Cognitive System V2"


    def think(self, question):

        print("SCS V2 THINK RUNNING")

        base_result = self_managing_scs.think(question)


        left_result = left_brain.think(question)

        print("LEFT DEBUG:", left_result)


        right_result = right_brain.think(question)


        formatted_reasoning = cognitive_output_formatter.format(
            left_result,
            right_result
        )


        formatted_left = formatted_reasoning["left"]
        formatted_right = formatted_reasoning["right"]
        print("FORMATTED LEFT DEBUG:", formatted_left)
        print("FORMATTED RIGHT DEBUG:", formatted_right)


        synthesis_result = synthesis_engine.combine(
            formatted_left,
            formatted_right,
            question
        )


        verification_result = verifier_engine.verify(
            synthesis_result
        )


        print("SYNTHESIS DEBUG:", synthesis_result)
        print("VERIFICATION DEBUG:", verification_result)


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

            "answer": {
            "left": formatted_left,
            "right": formatted_right,
            "synthesis": synthesis_result,
            "verification": verification_result
        },

        "base_result": {
            **base_result,
            "pulse": {
                "system": "SCS Selective Pulse Engine",
                "status": "selective_pulse_complete",
                "activated_modules": activation["activated_modules"],
                "left": formatted_left,
                "right": formatted_right,
                "synthesis": synthesis_result,
                "verification": verification_result
       }
   },



            "left_reasoning": formatted_left,

            "right_reasoning": formatted_right,


            "synthesis": synthesis_result,

            "verification": verification_result,


            "status": "orchestrated_v2_complete"
        }



orchestrated_scs_v2 = OrchestratedSCSV2()