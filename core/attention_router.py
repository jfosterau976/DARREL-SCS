from core.attention_manager import attention_manager
from core.selective_activation_engine import selective_activation
from core.cognitive_memory import cognitive_memory


class AttentionRouter:

    def __init__(self):
        self.name = "SCS Attention Router V2"

    def calculate_state(self, attention, memories):

        priorities = attention.get("priorities", [])

        risk = "low"
        complexity = "low"
        memory_required = bool(memories)
        verification_required = False
        reflection_required = False

        for item in priorities:

            area = item.get("area", "")
            priority = item.get("priority", "")

            if priority == "high":
                risk = "high"
                verification_required = True

            if area in ["accuracy", "safety"]:
                complexity = "high"
                verification_required = True
                reflection_required = True

            elif area in ["creativity", "analysis"]:
                if complexity != "high":
                    complexity = "medium"

        return {
            "complexity": complexity,
            "risk": risk,
            "memory_required": memory_required,
            "verification_required": verification_required,
            "reflection_required": reflection_required
        }

    def route(self, request):

        attention = attention_manager.analyse_priority(request)

        memories = cognitive_memory.recall_relevant(request)

        state = self.calculate_state(
            attention,
            memories
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
            "status": "routing_complete"
        }


attention_router = AttentionRouter()