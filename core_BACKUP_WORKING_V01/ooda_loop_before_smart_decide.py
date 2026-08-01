class OODA_Loop:

    def __init__(self):
        self.name = "SCS OODA Executive Loop"


    def observe(self, situation):

        return {
            "stage": "observe",
            "input": situation,
            "status": "observed"
        }


    def orient(self, observation):

        return {
            "stage": "orient",
            "context": observation,
            "status": "oriented"
        }


    def decide(self, orientation):

        return {
            "stage": "decide",
            "decision": "run cognitive pulse",
            "context": orientation,
            "status": "decision_made"
        }


    def act(self, decision):

        return {
            "stage": "act",
            "action": decision,
            "status": "executed"
        }


ooda_loop = OODA_Loop()