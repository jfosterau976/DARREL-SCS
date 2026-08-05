from core.llm_interface import LLMInterface
from core.cognitive_message import create_message


class RightBrain:

    def __init__(self):
        self.name = "Right Brain"
        self.role = "creative_exploration"

        self.llm = LLMInterface(
            "Right Brain Model",
            "local"
        )

    def think(self, question):

        prompt = f"""
You are the creative exploration component of
the Synthetic Cognitive System (SCS).

Question:
{question}

Explore:
- unusual possibilities
- alternative approaches
- unexpected connections
- opportunities
- risks others might miss

Be creative, but clearly identify uncertainty.
Do not invent facts.

Keep the response concise.
"""

        response = self.llm.generate(prompt)

        content = response.get(
            "response",
            ""
        )

        return create_message(
            self.name,
            self.role,
            content,
            confidence=0.70,
            metadata={
                "model": "Right Brain Model",
                "provider": "local"
            }
        )


right_brain = RightBrain()