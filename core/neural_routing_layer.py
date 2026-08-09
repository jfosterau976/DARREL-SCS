import math
import re


class NeuralRoutingLayer:

    VERSION = "neural-routing-v0.1"

    SIGNAL_NAMES = (
        "request_length",
        "multi_part_density",
        "constraint_density",
        "question_breadth",
        "factual_lookup_intent",
        "calculation_intent",
        "analysis_intent",
        "comparison_intent",
        "planning_intent",
        "creativity_intent",
        "decision_intent",
        "risk_intent",
        "safety_intent",
        "uncertainty",
        "verification_intent",
        "memory_relevance_intent",
    )

    TERM_GROUPS = {
        "factual_lookup_intent": (
            "what is", "who is", "when is", "where is",
            "define", "explain",
        ),
        "calculation_intent": (
            "calculate", "plus", "minus", "times",
            "equals", "sum", "percentage",
        ),
        "analysis_intent": (
            "analyse", "analyze", "evaluate", "assess",
            "reason", "investigate",
        ),
        "comparison_intent": (
            "compare", "versus", "instead", "advantages",
            "disadvantages", "trade-offs", "tradeoffs",
        ),
        "planning_intent": (
            "plan", "roadmap", "steps", "strategy",
            "schedule", "implement",
        ),
        "creativity_intent": (
            "create", "design", "invent", "innovate",
            "idea", "future",
        ),
        "decision_intent": (
            "should", "recommend", "choose", "decide",
            "best", "prioritise", "prioritize",
        ),
        "risk_intent": (
            "risk", "medical", "healthcare", "legal",
            "security", "financial", "high impact",
        ),
        "safety_intent": (
            "safe", "safety", "harm", "danger",
            "protect", "limitation",
        ),
        "uncertainty": (
            "uncertain", "unknown", "maybe", "possibly",
            "confidence", "ambiguous",
        ),
        "verification_intent": (
            "verify", "evidence", "facts", "accuracy",
            "validate", "check",
        ),
        "memory_relevance_intent": (
            "remember", "memory", "previous", "history",
            "learned", "recall",
        ),
    }

    CONSTRAINT_TERMS = (
        "must", "must not", "do not", "only", "without",
        "required", "preserve", "keep",
    )

    MULTI_PART_TERMS = (
        "and", "then", "also", "first", "second", "finally",
    )

    def extract_signals(self, request):
        text = str(request or "").lower().strip()
        tokens = re.findall(r"[a-z0-9']+", text)

        signals = {
            "request_length": self._clamp(len(tokens) / 80),
            "multi_part_density": self._density(
                text, tokens, self.MULTI_PART_TERMS, 5
            ),
            "constraint_density": self._density(
                text, tokens, self.CONSTRAINT_TERMS, 4
            ),
            "question_breadth": self._clamp(
                (
                    text.count("?")
                    + text.count(";")
                    + text.count("\n")
                    + len(re.findall(r"\b(?:and|or|versus)\b", text))
                ) / 6
            ),
        }

        for signal_name, terms in self.TERM_GROUPS.items():
            signals[signal_name] = float(
                self._term_hits(text, tokens, terms) > 0
            )

        return {
            name: round(signals[name], 4)
            for name in self.SIGNAL_NAMES
        }

    def predict(self, request):
        signals = self.extract_signals(request)

        complexity_scores = {
            "low": (
                0.45
                + 1.45 * signals["factual_lookup_intent"]
                + 1.80 * signals["calculation_intent"]
                + 0.20 * (1 - signals["request_length"])
            ),
            "medium": (
                0.85
                + 1.05 * signals["analysis_intent"]
                + 1.15 * signals["comparison_intent"]
                + 0.95 * signals["planning_intent"]
                + 1.00 * signals["creativity_intent"]
                + 0.75 * signals["decision_intent"]
                + 0.40 * signals["multi_part_density"]
                + 0.35 * signals["constraint_density"]
                + 0.25 * signals["request_length"]
            ),
            "high": (
                0.25
                + 1.80 * signals["risk_intent"]
                + 1.60 * signals["safety_intent"]
                + 0.65 * signals["uncertainty"]
                + 0.55 * signals["verification_intent"]
                + 0.40 * signals["planning_intent"]
                + 0.35 * signals["constraint_density"]
                + 0.30 * signals["question_breadth"]
            ),
        }

        complexity = max(complexity_scores, key=complexity_scores.get)

        risk_score = max(
            signals["risk_intent"],
            signals["safety_intent"],
            min(
                1.0,
                0.50 * signals["uncertainty"]
                + 0.25 * signals["verification_intent"],
            ),
        )
        risk = "high" if risk_score >= 0.75 else "low"

        if risk == "high":
            complexity = "high"

        return {
            "mode": "shadow",
            "version": self.VERSION,
            "status": "predicted",
            "authority": False,
            "signals": signals,
            "prediction": {
                "complexity": complexity,
                "risk": risk,
                "modules": self._modules_for_route(complexity, risk),
                "confidence": self._confidence(
                    complexity_scores, complexity
                ),
                "complexity_scores": {
                    name: round(score, 4)
                    for name, score in complexity_scores.items()
                },
                "risk_score": round(risk_score, 4),
            },
        }

    def compare(self, shadow_prediction, routing, execution):
        prediction = shadow_prediction.get("prediction", {})
        cognitive_state = routing.get("cognitive_state", {})
        activation = routing.get("activation", {})
        predicted_modules = prediction.get("modules", [])
        authoritative_modules = activation.get("activated_modules", [])
        predicted_set = set(predicted_modules)
        authoritative_set = set(authoritative_modules)
        union = predicted_set | authoritative_set
        results = execution.get("results", {})
        verification = results.get("verifier", {}).get("output", {})
        failed_modules = [
            name
            for name, result in results.items()
            if result.get("status") in {
                "dependency_missing", "execution_error", "module_not_found"
            }
        ]

        return {
            **shadow_prediction,
            "mode": "shadow",
            "version": self.VERSION,
            "status": "compared",
            "authority": False,
            "authoritative": {
                "complexity": cognitive_state.get("complexity"),
                "risk": cognitive_state.get("risk"),
                "modules": list(authoritative_modules),
            },
            "comparison": {
                "complexity_match": (
                    prediction.get("complexity")
                    == cognitive_state.get("complexity")
                ),
                "risk_match": (
                    prediction.get("risk") == cognitive_state.get("risk")
                ),
                "exact_module_match": predicted_set == authoritative_set,
                "module_jaccard": round(
                    len(predicted_set & authoritative_set) / len(union)
                    if union else 1.0,
                    4,
                ),
                "false_positives": sorted(
                    predicted_set - authoritative_set
                ),
                "false_negatives": sorted(
                    authoritative_set - predicted_set
                ),
            },
            "outcome": {
                "execution_status": execution.get("status"),
                "executed_modules": execution.get("executed_modules", []),
                "failed_modules": failed_modules,
                "verification_verdict": verification.get("verdict"),
                "verification_confidence": verification.get(
                    "confidence", 0
                ),
                "correction_attempted": execution.get(
                    "correction_attempted", False
                ),
            },
        }

    def _modules_for_route(self, complexity, risk):
        if complexity == "high" or risk == "high":
            return [
                "goal_planning", "left_reasoning", "right_reasoning",
                "synthesis", "verifier", "reflection", "learning",
            ]

        if complexity == "medium":
            return [
                "left_reasoning", "right_reasoning", "synthesis", "verifier"
            ]

        return ["left_reasoning", "verifier"]

    def _confidence(self, scores, winner):
        exponentials = {
            name: math.exp(score)
            for name, score in scores.items()
        }
        total = sum(exponentials.values())
        return round(exponentials[winner] / total, 4) if total else 0.0

    def _density(self, text, tokens, terms, scale):
        return self._clamp(self._term_hits(text, tokens, terms) / scale)

    def _term_hits(self, text, tokens, terms):
        token_set = set(tokens)
        hits = 0

        for term in terms:
            if " " in term or "-" in term:
                if term in text:
                    hits += 1
            elif term in token_set:
                hits += 1

        return hits

    def _clamp(self, value):
        return max(0.0, min(1.0, float(value)))


neural_routing_layer = NeuralRoutingLayer()
