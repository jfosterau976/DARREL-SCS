from core.memory_consolidator import memory_consolidator


class SynthesisAgent:

    def __init__(self):

        self.name = "SCS Synthesis Agent"


    def synthesize(self, question, left_result, right_result):

        left_analysis = left_result.get(
            "analysis",
            {}
        )

        right_analysis = right_result.get(
            "analysis",
            {}
        )

        learned_reasoning = left_result.get(
            "reasoning_context",
            []
        )


        priority_memory = memory_consolidator.consolidate().get(
            "concepts",
            []
        )


        return {

            "question": question,


            "analytical_summary": {

                "main_points": left_analysis.get(
                    "problem_breakdown",
                    []
                ),

                "risks": left_analysis.get(
                    "risk_analysis",
                    []
                ),

                "evidence": left_analysis.get(
                    "evidence_check",
                    []
                ),

                "recommendation": left_analysis.get(
                    "recommendation",
                    ""
                )

            },


            "creative_summary": {

                "ideas": right_analysis.get(
                    "innovation_ideas",
                    []
                ),

                "opportunities": right_analysis.get(
                    "opportunities",
                    []
                ),

                "future_scenarios": right_analysis.get(
                    "future_scenarios",
                    []
                ),

                "recommendation": right_analysis.get(
                    "creative_recommendation",
                    ""
                )

            },


            "learned_reasoning": learned_reasoning,


            "priority_memory": priority_memory[:5],


            "combined_insight":

                "SCS synthesis combines analytical "
                "evaluation, creative exploration, "
                "priority memory context, and learned "
                "reasoning to identify opportunities, "
                "risks, and recommended actions."

        }


synthesis_agent = SynthesisAgent()