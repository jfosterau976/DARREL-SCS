class VerifierEngine:

    def __init__(self):

        self.name = "SCS Verification Engine"


    def verify(self, result):

        checks = [
            "Check final answer exists",
            "Check answer has useful substance",
            "Check evidence requirements",
            "Check safety risks",
            "Check possible improvements",
            "Check learned reasoning usage"
        ]

        question = result.get(
            "question",
            ""
        )

        final_answer = (
            result.get("combined_insight")
            or result.get("llm_response")
            or ""
        )

        learned_reasoning = (
            result.get("learned_reasoning")
            or result.get("reasoning_context")
            or []
        )

        priority_memory = (
            result.get("priority_memory")
            or result.get("memory_context")
            or []
        )

        analytical = result.get(
            "analytical_summary",
            {}
        )

        creative = result.get(
            "creative_summary",
            {}
        )

        evidence = analytical.get(
            "evidence",
            []
        )

        critical_issues = []
        warnings = []
        improvements = []

        if not isinstance(final_answer, str) or not final_answer.strip():

            critical_issues.append(
                "Final answer is missing"
            )

        answer_lower = str(
            final_answer
        ).lower()

        question_lower = str(
            question
        ).lower()

        high_risk_terms = [
            "health",
            "healthcare",
            "medical",
            "diagnosis",
            "treatment",
            "legal",
            "financial",
            "safety"
        ]

        high_risk_request = any(
            term in question_lower
            for term in high_risk_terms
        )

        risk_markers = [
            "risk",
            "risks",
            "limitation",
            "limitations",
            "safety",
            "caution",
            "trade-off",
            "trade-offs"
        ]

        risk_analysis_present = any(
            marker in answer_lower
            for marker in risk_markers
        )

        if (
            high_risk_request
            and not risk_analysis_present
        ):

            critical_issues.append(
                "High-risk request lacks explicit risk analysis"
            )

        if analytical and not evidence:

            warnings.append(
                "No explicit evidence checks were supplied"
            )

        if not learned_reasoning:

            warnings.append(
                "No learned reasoning was used"
            )

        if not priority_memory:

            warnings.append(
                "No priority memory context was used"
            )

        if critical_issues:

            verdict = "REVIEW"
            confidence = 0.95

            improvements.extend(
                critical_issues
            )

        else:

            verdict = "PASS"

            if warnings:
                confidence = 0.80
            else:
                confidence = 0.95

        improvements.extend(
            warnings
        )

        if not improvements:

            improvements.append(
                "No material verification issues detected"
            )

        if learned_reasoning:

            learning_status = "learned_context_used"

        else:

            learning_status = "no_learned_context"

        return {

            "module": self.name,

            "mode": "verification",

            "checks": checks,

            "learning_status": learning_status,

            "learned_reasoning_reviewed": learned_reasoning,

            "priority_memory_reviewed": priority_memory[:5],

            "analytical_reviewed": analytical,

            "creative_reviewed": creative,

            "high_risk_request": high_risk_request,

            "risk_analysis_present": risk_analysis_present,

            "critical_issues": critical_issues,

            "warnings": warnings,

            "verdict": verdict,

            "confidence": confidence,

            "improvements": improvements

        }


verifier_engine = VerifierEngine()