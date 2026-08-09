import math
from collections.abc import Mapping


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
        normalized_fields = []
        cognitive_state = self._mapping(
            cognitive_state,
            "cognitive_state",
            normalized_fields,
        )
        neural_signals = self._mapping(
            neural_signals if neural_signals is not None else {},
            "neural_signals",
            normalized_fields,
        )
        complexity = cognitive_state.get("complexity", "medium")
        risk = cognitive_state.get("risk", "low")

        if (
            not isinstance(complexity, str)
            or complexity not in {"low", "medium", "high"}
        ):
            complexity = "medium"
            normalized_fields.append("cognitive_state.complexity")

        if not isinstance(risk, str) or risk not in {"low", "high"}:
            risk = "low"
            normalized_fields.append("cognitive_state.risk")

        extra_need = max(
            self._normalized_signal(
                neural_signals.get("analysis_intent"),
                "neural_signals.analysis_intent",
                normalized_fields,
            ),
            self._normalized_signal(
                neural_signals.get("planning_intent"),
                "neural_signals.planning_intent",
                normalized_fields,
            ),
            self._normalized_signal(
                neural_signals.get("creativity_intent"),
                "neural_signals.creativity_intent",
                normalized_fields,
            ),
            self._normalized_signal(
                neural_signals.get("uncertainty"),
                "neural_signals.uncertainty",
                normalized_fields,
            ),
            self._normalized_signal(
                neural_signals.get("verification_intent"),
                "neural_signals.verification_intent",
                normalized_fields,
            ),
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
            "data_quality": {
                "valid": not normalized_fields,
                "normalized_fields": sorted(set(normalized_fields)),
            },
            "stop_conditions": [
                "authoritative execution completes",
                "verification passes without unresolved critical issues",
                "correction-pass proposal is reached",
                "additional cognition has no demonstrated benefit",
            ],
        }

    def compare(self, proposal, actual_usage):
        normalized_fields = []
        proposal_record = self._mapping(
            proposal,
            "proposal",
            normalized_fields,
        )
        self._preserve_data_quality(
            proposal_record,
            "proposal.data_quality",
            normalized_fields,
        )
        limits = self._mapping(
            proposal_record.get("limits", {}),
            "proposal.limits",
            normalized_fields,
        )
        actual_record = self._mapping(
            actual_usage,
            "actual_usage",
            normalized_fields,
        )
        normalized_limits = dict(limits)
        normalized_actual = dict(actual_record)
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
            actual = self._nonnegative_number(
                actual_record.get(dimension),
                f"actual_usage.{dimension}",
                normalized_fields,
            )
            limit = self._nonnegative_number(
                limits.get(dimension),
                f"proposal.limits.{dimension}",
                normalized_fields,
            )

            if dimension in actual_record:
                normalized_actual[dimension] = actual

            if dimension in limits:
                normalized_limits[dimension] = limit

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
            **proposal_record,
            "mode": "shadow",
            "version": self.VERSION,
            "status": "compared",
            "authority": False,
            "enforced": False,
            "limits": normalized_limits,
            "actual_usage": normalized_actual,
            "data_quality": {
                "valid": not normalized_fields,
                "normalized_fields": sorted(set(normalized_fields)),
            },
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
                    if normalized_actual.get(dimension) is None
                ],
            },
        }

    def _mapping(self, value, field, normalized_fields):
        if isinstance(value, Mapping):
            return value

        normalized_fields.append(field)
        return {}

    def _normalized_signal(self, value, field, normalized_fields):
        if value is None:
            return 0.0

        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(float(value))
        ):
            normalized_fields.append(field)
            return 0.0

        normalized = float(value)

        if normalized < 0:
            normalized_fields.append(field)
            return 0.0

        if normalized > 1:
            normalized_fields.append(field)
            return 1.0

        return normalized

    def _preserve_data_quality(self, record, field, normalized_fields):
        if "data_quality" not in record:
            return

        quality = record.get("data_quality")

        if not isinstance(quality, Mapping):
            normalized_fields.append(field)
            return

        fields = quality.get("normalized_fields", [])

        if not isinstance(fields, (list, tuple)):
            normalized_fields.append(f"{field}.normalized_fields")
            return

        valid_fields = [
            item
            for item in fields
            if isinstance(item, str) and item
        ]
        normalized_fields.extend(valid_fields)

        if len(valid_fields) != len(fields):
            normalized_fields.append(f"{field}.normalized_fields")

        if quality.get("valid") is False and not valid_fields:
            normalized_fields.append(field)

    def _nonnegative_number(self, value, field, normalized_fields):
        if value is None:
            return None

        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(float(value))
            or value < 0
        ):
            normalized_fields.append(field)
            return None

        return value

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
