from core.memory_consolidator import memory_consolidator
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
                important.append(
                    {
                        "concept": concept.get("concept"),
                        "evidence": concept.get("evidence_count"),
                        "importance": concept.get("importance")
                    }
                )

        return important
    def think(self, request, memories=None):

        if memories is None:
            memories = []

        learned_memory = memory_consolidator.consolidate()

        learned_concepts = learned_memory.get(
            "concepts",
            []
        )

        reasoning_context = self.apply_learned_reasoning(
            learned_concepts
        )
        memory_context = []

        for item in memories[:5]:

            if isinstance(item, dict):

                memory = item.get(
                    "memory",
                    item
                )

                if isinstance(memory, dict):

                    question = memory.get(
                        "question",
                        ""
                    )

                    if question:
                        memory_context.append(question)


        if memory_context:

            memory_summary = (
                "Previous experiences considered: "
                + ", ".join(memory_context)
            )

        else:

            memory_summary = (
                "No previous experiences available."
            )


        return {

            "agent": self.name,

            "role": self.role,

            "mode": self.role,

            "status": "complete",

            "confidence": 0.75,

            "memory_context": memory_context,

            "learned_concepts": learned_concepts,

            "learned_reasoning_context": [
                concept["concept"]
                for concept in learned_concepts
                if concept.get("importance") in ["HIGH", "MEDIUM"]
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

                "recommendation":
                    f"Use analytical reasoning to evaluate: {request}"
            }
        }


    def analyse(self, request, memories=None):
        return self.think(request, memories)


    def analyze(self, request, memories=None):
        return self.think(request, memories)


left_brain = LeftBrain()