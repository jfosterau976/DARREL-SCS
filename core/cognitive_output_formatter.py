class CognitiveOutputFormatter:

    def __init__(self):
        self.name = "SCS Cognitive Output Formatter"


    def format_left(self, left):

        return {
            "module": left.get(
                "agent",
                "SCS Left Cognitive Engine"
            ),
            "mode": left.get(
                "role",
                "analytical_reasoning"
            ),
            "confidence": left.get(
                "confidence",
                0
            ),
            "analysis": left.get(
                "analysis",
                {}
            )
        }


    def format_right(self, right):

        return {
            "module": right.get(
                "agent",
                "SCS Right Cognitive Engine"
            ),
            "mode": right.get(
                "role",
                "creative_thinking"
            ),
            "confidence": right.get(
                "confidence",
                0
            ),
            "analysis": right.get(
                "analysis",
                {}
            )
        }


    def format(self, left, right):

        return {
            "left": self.format_left(left),
            "right": self.format_right(right)
        }


cognitive_output_formatter = CognitiveOutputFormatter()