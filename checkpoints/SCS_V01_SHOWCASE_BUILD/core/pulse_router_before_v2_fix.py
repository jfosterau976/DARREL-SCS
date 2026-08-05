class PulseRouter:

    def __init__(self):
        self.name = "SCS Pulse Router"

    def decide(self, question, feedback=None):

        text = question.lower().strip()

        decision = {
            "left": False,
            "right": False,
            "synthesis": False,
            "verifier": False
        }

        # -------------------------------------------------
        # FEEDBACK HAS HIGHEST PRIORITY
        # -------------------------------------------------

        if feedback:

            target = str(
                feedback.get("target", "")
            ).upper()

            if target == "LEFT":
                decision["left"] = True

            elif target == "RIGHT":
                decision["right"] = True

            elif target == "SYNTHESIS":
                decision["synthesis"] = True

            # Verification is only needed when
            # feedback specifically asks for it.
            if target in {"LEFT", "RIGHT", "SYNTHESIS"}:
                decision["verifier"] = True

            return decision

        # -------------------------------------------------
        # SIMPLE QUESTIONS
        # ONE MODEL CALL
        # -------------------------------------------------

        simple_words = [
            "what is",
            "who is",
            "when is",
            "where is",
            "define",
            "convert",
            "calculate",
            "how much is"
        ]

        if any(word in text for word in simple_words):

            decision["left"] = True

            return decision

        # -------------------------------------------------
        # CREATIVE QUESTIONS
        # RIGHT BRAIN + SYNTHESIS
        # NO VERIFIER UNLESS NEEDED
        # -------------------------------------------------

        creative_words = [
            "idea",
            "creative",
            "imagine",
            "invent",
            "unusual",
            "brainstorm",
            "design"
        ]

        if any(word in text for word in creative_words):

            decision["right"] = True
            decision["synthesis"] = True

            return decision

        # -------------------------------------------------
        # ANALYTICAL QUESTIONS
        # LEFT BRAIN + VERIFIER
        # -------------------------------------------------

        analytical_words = [
            "analyse",
            "analyze",
            "compare",
            "why",
            "evidence",
            "risk",
            "cost",
            "should",
            "evaluate",
            "verify",
            "claim",
            "likely",
            "benefit",
            "drawback"
        ]

        if any(word in text for word in analytical_words):

            decision["left"] = True
            decision["verifier"] = True

            return decision

        # -------------------------------------------------
        # COMPLEX QUESTIONS
        # FULL COGNITIVE ROUTE
        # -------------------------------------------------

        decision["left"] = True
        decision["right"] = True
        decision["synthesis"] = True
        decision["verifier"] = True

        return decision


pulse_router = PulseRouter()