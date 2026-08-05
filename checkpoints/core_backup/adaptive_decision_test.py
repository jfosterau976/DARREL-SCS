from core.decision_feedback_bridge import decision_feedback_bridge


def adaptive_decide(verification):

    strategy = decision_feedback_bridge.update_strategy(
        verification
    )

    return {
        "stage": "adaptive_decide",
        "strategy": strategy,
        "status": "updated"
    }


if __name__ == "__main__":

    review_case = {
        "metadata": {
            "verdict": "REVIEW",
            "target": "LEFT",
            "response": "Need empirical evidence"
        }
    }

    result = adaptive_decide(
        review_case
    )

    print(result)