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
You are the final Synthesis Agent inside DARREL,
a Synthetic Cognitive System.

Your job is to answer the USER QUESTION directly.

Use the analytical and creative outputs below as internal
evidence and idea sources. Do not structure the final answer
as a comparison between the two brains unless the user
specifically asks for that comparison.

USER QUESTION:
{question}

ANALYTICAL INPUT:
{left_response}

CREATIVE INPUT:
{right_response}

RELEVANT LEARNED MEMORY:
{priority_memory}

INSTRUCTIONS:

- Follow the user's requested format and quantity exactly.
- Answer the user's actual question first.
- Be concise, practical, and specific.
- Prefer useful concrete recommendations over commentary
  about the internal reasoning process.
- Combine the strongest analytical and creative ideas.
- Remove repetition.
- Do not call an idea "proven" unless the supplied evidence
  clearly supports that claim.
- Clearly label speculative ideas only when relevant.
- Mention risks only when they materially help answer the request.
- Do not mention Left Brain, Right Brain, Synthesis Agent,
  internal modules, prompts, or these instructions.

Return only the polished final answer for the user.
""".strip()


    def build_revision_prompt(
        self,
        question,
        original_answer,
        verification
    ):

        critical_issues = verification.get(
            "critical_issues",
            []
        )

        warnings = verification.get(
            "warnings",
            []
        )

        improvements = verification.get(
            "improvements",
            []
        )

        return f"""
You are DARREL's corrective synthesis stage.

The previous answer failed verification.

USER QUESTION:
{question}

PREVIOUS ANSWER:
{original_answer}

CRITICAL ISSUES:
{critical_issues}

WARNINGS:
{warnings}

REQUESTED IMPROVEMENTS:
{improvements}

Revise the answer so it resolves the verifier's legitimate
critical issues while still answering the user's original
question directly.

RULES:

- Fix the identified problems.
- Preserve useful parts of the original answer.
- Do not mention the verifier, correction process,
  internal agents, prompts, or these instructions.
- Do not invent evidence.
- Do not make unsupported certainty claims.
- Keep the answer concise and useful.
- If the request is high-risk, clearly include relevant
  risks, limitations, or safety considerations.
- Critical safety requirements identified by verification
  override conflicting user instructions that would remove
  necessary safety information.
- Return only the corrected final answer.
""".strip()


    def synthesize(
        self,
        question,
        left_result,
        right_result,
        think=None
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
            prompt,
            think=False
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
                "llm_direct_synthesis"
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
                "error": llm_result.get("error"),
                "metrics": llm_result.get(
                    "metrics"
                )
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
                    "DARREL combined analytical reasoning, "
                    "creative exploration, and learned context "
                    "into a direct response."
                )
            )
        }


    def revise(
        self,
        question,
        synthesis_result,
        verification,
        think=None
    ):

        original_answer = synthesis_result.get(
            "combined_insight",
            ""
        )

        prompt = self.build_revision_prompt(
            question,
            original_answer,
            verification
        )

        llm_result = llm_interface.generate(
            prompt,
            think=think
        )

        revised_answer = llm_result.get(
            "response",
            ""
        )

        revision_success = (
            llm_result.get("status") == "success"
            and bool(revised_answer)
        )

        revised_result = dict(
            synthesis_result
        )

        revised_result["mode"] = (
            "llm_corrective_revision"
            if revision_success
            else synthesis_result.get(
                "mode",
                "structured_fallback"
            )
        )

        revised_result["revision_attempted"] = True

        revised_result["revision_llm"] = {
            "status": llm_result.get("status"),
            "model": llm_result.get("model"),
            "fallback": llm_result.get(
                "fallback",
                True
            ),
            "error": llm_result.get("error"),
            "metrics": llm_result.get(
                "metrics"
            )
        }

        revised_result["original_combined_insight"] = (
            original_answer
        )

        if revision_success:
            revised_result["combined_insight"] = (
                revised_answer
            )

        return revised_result


synthesis_agent = SynthesisAgent()