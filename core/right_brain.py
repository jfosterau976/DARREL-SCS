from core.memory_consolidator import memory_consolidator
from core.llm_interface import llm_interface


class RightBrain:

    def __init__(self):

        self.name = "Right Brain Model"
        self.role = "creative_thinking"

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
        creative_context
    ):

        return f"""
You are the creative Right Brain of DARREL,
a Synthetic Cognitive System.

Explore the user's request imaginatively,
but remain practical and useful.

USER REQUEST:
{request}

RELEVANT MEMORY:
{memory_context}

LEARNED CONCEPTS:
{creative_context}

Return a concise creative response containing:

1. Alternative perspectives
2. New or unconventional ideas
3. Opportunities
4. Future scenarios
5. Potential combinations of technologies or approaches
6. Creative recommendation

Avoid repeating obvious analytical points.
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

        creative_context = self.apply_learned_reasoning(
            learned_concepts
        )

        memory_context = self.build_memory_context(
            memories
        )

        prompt = self.build_prompt(
            request,
            memory_context,
            creative_context[:5]
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
                "llm_creative_reasoning"
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

            "learned_reasoning_context": creative_context,

            "analysis": {

                "creative_recommendation": (
                    llm_response
                    if llm_success
                    else
                    "Explore ambitious ideas while balancing practical execution."
                ),

                "future_scenarios": [
                    "Successful adoption and growth",
                    "Market competition increases",
                    "Technology evolves rapidly"
                ],

                "innovation_ideas": [
                    "Create new user experiences",
                    "Combine existing technologies in new ways",
                    "Build systems that improve over time"
                ],

                "opportunities": [
                    f"Explore new possibilities around: {request}",
                    "Consider unconventional approaches",
                    "Look for future advantages"
                ]
            }
        }

    def create(self, request, memories=None):
        return self.think(request, memories)

    def analyse(self, request, memories=None):
        return self.think(request, memories)

    def analyze(self, request, memories=None):
        return self.think(request, memories)


right_brain = RightBrain()