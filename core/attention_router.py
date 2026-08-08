from core.attention_manager import attention_manager
from core.selective_activation_engine import selective_activation
from core.cognitive_memory import cognitive_memory


class AttentionRouter:

    def __init__(self):

        self.name = "SCS Adaptive Attention Router V3"


    def classify_request(self, request):

        text = request.lower()

        simple_patterns = [
            "what is",
            "who is",
            "when is",
            "where is",
            "calculate",
            "plus",
            "minus",
            "times",
            "equals"
        ]

        creative_patterns = [
            "design",
            "invent",
            "create",
            "future",
            "idea",
            "strategy"
        ]

        high_risk_patterns = [
            "medical",
            "health",
            "safety",
            "security",
            "legal",
            "risk"
        ]


        if any(x in text for x in high_risk_patterns):

            return "high"


        if any(x in text for x in creative_patterns):

            return "medium"


        if any(x in text for x in simple_patterns):

            return "low"


        return "medium"



    def calculate_state(self, attention, memories, request):


        complexity = self.classify_request(request)


        risk = "low"

        verification_required = True

        reflection_required = False


        if complexity == "high":

            risk = "high"
            reflection_required = True


        memory_required = False


        if complexity in ["medium", "high"]:

            memory_required = True


        return {

            "complexity": complexity,

            "risk": risk,

            "memory_required": memory_required,

            "verification_required": verification_required,

            "reflection_required": reflection_required

        }



    def route(self, request):


        attention = attention_manager.analyse_priority(
            request
        )


        memories = []


        state = self.calculate_state(
            attention,
            memories,
            request
        )


        activation = selective_activation.activate(
            state["complexity"],
            state["risk"]
        )


        return {

            "router": self.name,

            "request": request,

            "attention": attention,

            "memory_signals": {

                "relevant_memories": len(memories)

            },

            "cognitive_state": state,

            "activation": activation,

            "selected_modules": activation.get(
                "activated_modules",
                []
            ),

            "status": "adaptive_routing_complete"

        }



attention_router = AttentionRouter()