from core.ooda_loop import ooda_loop
from core.learning_coordinator import learning_coordinator
from core.decision_engine import decision_engine


class SCSExecutive:

    def __init__(self):
        self.name = "SCS Executive Controller"

    def process(
        self,
        question,
        synthesis=None,
        verification=None
    ):

        observation = ooda_loop.observe(
            question
        )

        orientation = ooda_loop.orient(
            observation
        )

        learning_path = learning_coordinator.decide_learning_path(
            question
        )

        ooda_decision = ooda_loop.decide(
            orientation
        )

        executive_decision = None

        if synthesis and verification:

            executive_decision = decision_engine.decide(
                question,
                synthesis,
                verification
            )

        return {

            "system": self.name,

            "question": question,

            "observation": observation,

            "orientation": orientation,

            "learning_path": learning_path,

            "ooda_decision": ooda_decision,

            "executive_decision": executive_decision,

            "status": "executive_complete"

        }


scs_executive = SCSExecutive()