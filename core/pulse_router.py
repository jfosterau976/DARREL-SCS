class PulseRouter:

    def __init__(self):
        self.name = "SCS Pulse Router V2"

    def decide(self, question, feedback=None):
        decision = {
            "left": True,
            "right": True,
            "synthesis": True,
            "verifier": True
        }

        # Feedback can selectively reduce the pulse later.
        if feedback:
            target = str(feedback.get("target", "")).upper()

            if target == "LEFT":
                decision = {
                    "left": True,
                    "right": False,
                    "synthesis": False,
                    "verifier": False
                }

            elif target == "RIGHT":
                decision = {
                    "left": False,
                    "right": True,
                    "synthesis": False,
                    "verifier": False
                }

            elif target == "SYNTHESIS":
                decision = {
                    "left": True,
                    "right": True,
                    "synthesis": True,
                    "verifier": True
                }

        return decision

    def route(self, question, feedback=None):
        decision = self.decide(question, feedback)

        modules = []

        if decision["left"]:
            modules.append("left_reasoning")

        if decision["right"]:
            modules.append("right_reasoning")

        if decision["synthesis"]:
            modules.append("synthesis")

        if decision["verifier"]:
            modules.append("verifier")

        return {
            "question": question,
            "activated_modules": modules,
            "routing_mode": "v2_full_cognitive",
            "status": "routing_complete"
        }


pulse_router = PulseRouter()