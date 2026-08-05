from core.selective_pulse_engine import selective_pulse_engine


class SelfManagingSCS:

    def __init__(self):
        self.name = "SCS Self Managing System"


    def think(self, question):

        modules = [
            "goal_planning",
            "left_reasoning",
            "right_reasoning",
            "synthesis",
            "verifier",
            "learning"
        ]

        pulse = selective_pulse_engine.run(
            question,
            modules
        )


        return {

            "system": self.name,

            "question": question,

            "goal": question,

            "pulse": pulse,

            "left": pulse.get("left", {}),

            "right": pulse.get("right", {}),

            "synthesis": pulse.get("synthesis", {}),

            "verification": pulse.get("verification", {}),

            "decision": pulse.get("decision", {}),

            "learning": pulse.get(
                "learning",
                {}
            ),

            "status": "self_managing_complete"
        }


self_managing_scs = SelfManagingSCS()