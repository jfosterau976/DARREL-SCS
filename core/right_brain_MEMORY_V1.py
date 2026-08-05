from core.memory_consolidator import memory_consolidator


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


        creative_context = self.apply_learned_reasoning(
            learned_concepts
        )


        return {

            "agent": self.name,

            "role": self.role,

            "status": "complete",

            "confidence": 0.75,

            "memory_context": creative_context,

            "learned_reasoning_context": creative_context,

            "analysis": {

                "creative_recommendation":
                    "Explore ambitious ideas while balancing practical execution.",

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