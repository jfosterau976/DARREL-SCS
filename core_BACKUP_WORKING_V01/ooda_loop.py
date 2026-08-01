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

        question = observation.get("input", "").lower()

        if any(word in question for word in [
            "creative",
            "idea",
            "story",
            "design",
            "brainstorm"
        ]):
            context_type = "creative"

        elif any(word in question for word in [
            "analyse",
            "analyze",
            "research",
            "compare",
            "evidence",
            "should",
            "why"
        ]):
            context_type = "analytical"

        else:
            context_type = "general"

        return {
            "stage": "orient",
            "context": observation,
            "context_type": context_type,
            "status": "oriented"
        }

    def decide(self, orientation, adaptive_strategy=None):

        context_type = orientation.get("context_type", "general")
        if adaptive_strategy:
            return {
                "stage": "decide",
                "decision": "run adaptive cognitive pulse",
                "strategy": adaptive_strategy,
                "context": orientation,
                "status": "adaptive_decision_made"
            }
        if context_type == "creative":
            strategy = {
                "left": False,
                "right": True,
                "synthesis": True,
                "verifier": False
            }

        elif context_type == "analytical":
            strategy = {
                "left": True,
                "right": False,
                "synthesis": False,
                "verifier": True
            }

        else:
            strategy = {
                "left": True,
                "right": True,
                "synthesis": True,
                "verifier": True
            }

        return {
            "stage": "decide",
            "decision": "run cognitive pulse",
            "strategy": strategy,
            "context": orientation,
            "status": "decision_made"
        }

    def act(self, decision):

        return {
            "stage": "act",
            "action": decision,
            "strategy": decision.get("strategy", {}),
            "status": "executed"
        }


ooda_loop = OODA_Loop()