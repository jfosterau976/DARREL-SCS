from core.attention_manager import attention_manager
from core.selective_activation_engine import selective_activation


class AttentionRouter:

    def __init__(self):
        self.name = "SCS Attention Router V1"


    def calculate_state(self, attention):

        priorities = attention.get(
            "priorities",
            []
        )


        risk = "low"
        complexity = "low"


        for item in priorities:

            if item.get("priority") == "high":

                risk = "high"


            if item.get("area") in [
                "accuracy",
                "safety"
            ]:

                complexity = "high"


            elif item.get("area") == "creativity":

                if complexity != "high":
                    complexity = "medium"


        return {
            "complexity": complexity,
            "risk": risk
        }


    def route(self, request):

        attention = attention_manager.analyse_priority(
            request
        )


        state = self.calculate_state(
            attention
        )


        activation = selective_activation.activate(
            state["complexity"],
            state["risk"]
        )


        return {

            "router": self.name,

            "request": request,

            "attention": attention,

            "cognitive_state": state,

            "activation": activation,

            "status": "routing_complete"

        }


attention_router = AttentionRouter()