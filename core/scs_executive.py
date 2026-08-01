from core.ooda_loop import ooda_loop
from core.learning_coordinator import learning_coordinator


class SCSExecutive:

    def __init__(self):
        self.name = "SCS Executive Controller"


    def process(self, question):

        observation = ooda_loop.observe(
            question
        )

        orientation = ooda_loop.orient(
            observation
        )

        learning_path = learning_coordinator.decide_learning_path(
            question
        )


        if learning_path.get("mode") == "memory_guided":

            decision = ooda_loop.decide(
                orientation,
                {
                    "left": True,
                    "right": False,
                    "synthesis": True,
                    "verifier": True
                }
            )

        else:

            decision = ooda_loop.decide(
                orientation
            )


        return {
            "question": question,
            "learning_path": learning_path,
            "decision": decision
        }


scs_executive = SCSExecutive()