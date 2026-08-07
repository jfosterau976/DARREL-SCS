from core.self_managing_scs import self_managing_scs


class OrchestratedSCSV2:

    def __init__(self):
        self.name = "SCS Orchestrated Cognitive System V2"

    def think(self, question):

        print("\n=== SCS V2 THINKING ===")

        result = self_managing_scs.think(question)

        return {

            "question": question,

            "system": self.name,

            "status": result.get("status"),

            "activated_modules": result.get(
                "activated_modules",
                []
            ),

            "base_result": result,

            "answer": {

                "left": result.get("left", {}),

                "right": result.get("right", {}),

                "synthesis": result.get("synthesis", {}),

                "verification": result.get(
                    "verification",
                    {}
                )

            }

        }


orchestrated_scs_v2 = OrchestratedSCSV2()