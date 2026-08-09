class CognitiveBudgetManager:

    VERSION = "cognitive-budget-v0.1"

    BUDGETS = {
        "microscopic": {
            "latency_ms": 2000,
            "total_tokens": 1024,
            "api_cost_class": "minimal",
            "model_calls": 1,
            "memory_lookups": 0,
            "tool_calls": 0,
            "modules": 2,
            "verification_passes": 1,
            "correction_passes": 0,
        },
        "light": {
            "latency_ms": 6000,
            "total_tokens": 2048,
            "api_cost_class": "low",
            "model_calls": 2,
            "memory_lookups": 1,
            "tool_calls": 0,
            "modules": 3,
            "verification_passes": 1,
            "correction_passes": 1,
        },
        "standard": {
            "latency_ms": 20000,
            "total_tokens": 4096,
            "api_cost_class": "moderate",
            "model_calls": 4,
            "memory_lookups": 1,
            "tool_calls": 1,
            "modules": 4,
            "verification_passes": 2,
            "correction_passes": 1,
        },
        "deep": {
            "latency_ms": 60000,
            "total_tokens": 8192,
            "api_cost_class": "high",
            "model_calls": 7,
            "memory_lookups": 2,
            "tool_calls": 2,
            "modules": 7,
            "verification_passes": 2,
            "correction_passes": 2,
        },
    }

    def propose(self, request, cognitive_state, neural_signals=None):
        cognitive_state = cognitive_state or {}
        neural_signals = neural_signals or {}
        complexity = cognitive_state.get("complexity", "medium")
        risk = cognitive_state.get("risk", "low")

        extra_need = max(
            neural_signals.get("analysis_intent", 0),
            neural_signals.get("planning_intent", 0),
            neural_signals.get("creativity_intent", 0),
            neural_signals.get("uncertainty", 0),
            neural_signals.get("verification_intent", 0),
        )

        if risk == "high" or complexity == "high":
            tier = "deep"
        elif complexity == "medium":
            tier = "standard"
        elif extra_need > 0:
            tier = "light"
        else:
            tier = "microscopic"

        return {
            "mode": "shadow",
            "version": self.VERSION,
            "status": "proposed",
            "authority": False,
            "enforced": False,
            "tier": tier,
            "limits": dict(self.BUDGETS[tier]),
            "inputs": {
                "complexity": complexity,
                "risk": risk,
                "request_length": len(str(request or "")),
                "extra_need": round(float(extra_need), 4),
            },
            "stop_conditions": [
                "authoritative execution completes",
                "verification passes without unresolved critical issues",
                "correction-pass proposal is reached",
                "additional cognition has no demonstrated benefit",
            ],
        }

    def compare(self, proposal, actual_usage):
        limits = proposal.get("limits", {})
        actual_usage = actual_usage or {}
        measured_dimensions = (
            "latency_ms",
            "total_tokens",
            "model_calls",
            "modules",
            "verification_passes",
            "correction_passes",
        )
        overruns = []
        utilization = {}

        for dimension in measured_dimensions:
            actual = actual_usage.get(dimension)
            limit = limits.get(dimension)

            if actual is None or limit is None:
                utilization[dimension] = None
                continue

            utilization[dimension] = round(
                actual / limit if limit else 0.0,
                4,
            )

            if actual > limit:
                overruns.append({
                    "dimension": dimension,
                    "actual": actual,
                    "limit": limit,
                })

        return {
            **proposal,
            "status": "compared",
            "actual_usage": dict(actual_usage),
            "comparison": {
                "within_budget": not overruns,
                "overruns": overruns,
                "utilization": utilization,
                "unmeasured": [
                    dimension
                    for dimension in (
                        "api_cost",
                        "memory_lookups",
                        "tool_calls",
                    )
                    if actual_usage.get(dimension) is None
                ],
            },
        }

    def error_record(self, stage, error):
        return {
            "mode": "shadow",
            "version": self.VERSION,
            "status": "error",
            "authority": False,
            "enforced": False,
            "stage": stage,
            "error_type": type(error).__name__,
        }


cognitive_budget_manager = CognitiveBudgetManager()
