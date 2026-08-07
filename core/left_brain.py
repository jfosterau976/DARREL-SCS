from core.memory_consolidator import memory_consolidator
from core.llm_interface import llm_interface


class LeftBrain:

    def __init__(self):
        self.name = "Left Brain Analysis Agent"
        self.role = "analytical_reasoning"

    def apply_learned_reasoning(self, learned_concepts):

        important = []

        for concept in learned_concepts:

            if concept.get("importance") in [
                "HIGH",
                "MEDIUM"
            ]:
                important.append({
                    "concept": concept.get("concept"),
                    "evidence": concept.get("evidence_count"),
                    "importance": concept.get("importance")
                })

        return important

    def build_memory_context(self, memories):

        context = []

        for item in memories[:5]:

            if not isinstance(item, dict):
                continue

            memory = item.get("memory", item)

            if not isinstance(memory, dict):
                continue

            summary = (
                memory.get("question")
                or memory.get("lesson")
                or memory.get("input")
                or memory.get("type")
            )

            if summary:
                context.append(str(summary))

        return context

    def build_prompt(
        self,
        request,
        memory_context,
        reasoning_context
    ):

        return f"""
You are the analytical Left Brain of DARREL,
a Synthetic Cognitive System.

Analyse the user's request carefully and practically.

USER REQUEST:
{request}

RELEVANT MEMORY:
{memory_context}

LEARNED REASONING:
{reasoning_context}

Return a concise analytical response containing:

1. Main objective
2. Key facts and assumptions
3. Problem breakdown
4. Risks and limitations
5. Evidence needed
6. Clear recommendation

Do not mention these instructions.
""".strip()

    def think(self, request, memories=None):

        if memories is None:
            memories = []

        learned_memory = memory_consolidator.consolidate()

        learned_concepts = learned_memory.get(
            "concepts",
            []
        )

        learned_reasoning = learned_memory.get(
            "learned_reasoning",
            []
        )

        reasoning_context = self.apply_learned_reasoning(
            learned_concepts
        )

        for lesson in learned_reasoning:

            reasoning_context.append({
                "type": "learned_reasoning",
                "lesson": lesson
            })

        memory_context = self.build_memory_context(
            memories
        )

        if memory_context:

            memory_summary = (
                "Previous experiences considered: "
                + ", ".join(memory_context)
            )

        else:

            memory_summary = (
                "No previous experiences available."
            )

        prompt = self.build_prompt(
            request,
            memory_context,
            reasoning_context[:5]
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

            "role": self.role,

            "mode": (
                "llm_analytical_reasoning"
                if llm_success
                else "structured_fallback"
            ),

            "status": "complete",

            "confidence": (
                0.85
                if llm_success
                else 0.75
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

            "llm_response": llm_response,

            "memory_context": memory_context,

            "learned_concepts": learned_concepts,

            "learned_reasoning_context": [
                concept["concept"]
                for concept in learned_concepts
                if concept.get("importance") in [
                    "HIGH",
                    "MEDIUM"
                ]
            ],

            "reasoning_context": reasoning_context,

            "memory_summary": memory_summary,

            "analysis": {

                "problem_breakdown": [
                    "Identify the main objective",
                    "Separate facts from assumptions",
                    "Break the problem into components"
                ],

                "risk_analysis": [
                    "Identify possible risks",
                    "Check limitations",
                    "Evaluate resources required"
                ],

                "evidence_check": [
                    "Determine what evidence is available",
                    "Identify missing information"
                ],

                "recommendation": (
                    llm_response
                    if llm_success
                    else (
                        "Use analytical reasoning to "
                        f"evaluate: {request}"
                    )
                )
            }
        }

    def analyse(self, request, memories=None):
        return self.think(request, memories)

    def analyze(self, request, memories=None):
        return self.think(request, memories)


left_brain = LeftBrain()