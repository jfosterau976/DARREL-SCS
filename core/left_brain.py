from core.llm_interface import LLMInterface
from core.cognitive_message import create_message


class LeftBrain:

    def __init__(self):
        self.name = "Left Brain"
        self.role = "analysis"

        self.llm = LLMInterface(
            "Left Brain Model",
            "local"
        )

    def think(self, question):

        prompt = f"""
You are the analytical component of the
Synthetic Cognitive System (SCS).

Question:
{question}

Focus on:
- facts
- assumptions
- advantages
- disadvantages
- risks
- practical considerations

Do not invent missing information.

Keep the analysis concise.
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
            confidence=0.85,
            metadata={
                "model": "Left Brain Model",
                "provider": "local"
            }
        )


left_brain = LeftBrain()