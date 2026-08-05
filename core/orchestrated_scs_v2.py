from core.self_managing_scs import self_managing_scs


class OrchestratedSCSV2:

    def __init__(self):
        self.name = "SCS Orchestrated Cognitive System V2"


    def think(self, question):

        print("SCS V2 THINK RUNNING")

        result = self_managing_scs.think(question)

        print("PULSE RESULT:", result)

        return {
            "question": question,

            "base_result": result,

            "answer": {
                "left": result.get("left", result.get("answer", {}).get("left", {})),
                "right": result.get("right", result.get("answer", {}).get("right", {})),
                "synthesis": result.get("synthesis", result.get("answer", {}).get("synthesis", {})),
                "verification": result.get("verification", result.get("answer", {}).get("verification", {}))
            }
        }


orchestrated_scs_v2 = OrchestratedSCSV2()