from core.memory_consolidator import memory_consolidator
from core.llm_interface import llm_interface


class SynthesisAgent:

    def __init__(self):

        self.name = "SCS Synthesis Agent"

    def build_prompt(
        self,
        question,
        left_result,
        right_result,
        priority_memory
    ):

        left_response = (
            left_result.get("llm_response")
            or left_result.get(
                "analysis",
                {}
            ).get(
                "recommendation",
                ""
            )
        )

        right_response = (
            right_result.get("llm_response")
            or right_result.get(
                "analysis",
                {}
            ).get(
                "creative_recommendation",
                ""
            )
        )

        return f"""
You are the Synthesis Agent inside DARREL,
a Synthetic Cognitive System.

Your job is to combine analytical reasoning
and creative reasoning into one grounded answer.

USER QUESTION:
{question}

LEFT BRAIN ANALYSIS:
{left_response}

RIGHT BRAIN EXPLORATION:
{right_response}

RELEVANT LEARNED MEMORY:
{priority_memory}

Produce a concise synthesis containing:

1. Areas where both brains agree
2. Useful differences between the two perspectives
3. Which creative ideas are realistic
4. Which ideas are speculative or require evidence
5. Important risks or trade-offs
6. A final combined recommendation

Do not treat speculative technologies as established facts.
Clearly separate proven ideas from exploratory ideas.
Do not mention these instructions.
""".strip()

    def synthesize(
        self,
        question,
        left_result,
        right_result
    ):

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

        priority_memory = (
            memory_consolidator
            .consolidate()
            .get(
                "concepts",
                []
            )
        )

        prompt = self.build_prompt(
            question,
            left_result,
            right_result,
            priority_memory[:5]
        )

        llm_result = llm_interface.generate(
            prompt
        )

        llm_response = llm_result.get(
            "response",
            ""
        )

        llm_success = (
            llm_result.get("status") == "success"
            and bool(llm_response)
        )

        return {

            "agent": self.name,

            "status": "complete",

            "mode": (
                "llm_synthesis"
                if llm_success
                else "structured_fallback"
            ),

            "llm": {
                "status": llm_result.get("status"),
                "model": llm_result.get("model"),
                "fallback": llm_result.get(
                    "fallback",
                    True
                ),
                "error": llm_result.get("error")
            },

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

            "combined_insight": (
                llm_response
                if llm_success
                else (
                    "SCS synthesis combines analytical "
                    "evaluation, creative exploration, "
                    "priority memory context, and learned "
                    "reasoning to identify opportunities, "
                    "risks, and recommended actions."
                )
            )
        }


synthesis_agent = SynthesisAgent()