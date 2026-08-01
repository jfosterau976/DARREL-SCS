from core.ooda_loop import ooda_loop
from core.decision_feedback_bridge import decision_feedback_bridge


def run_adaptive_test(question):

    print("\nSCS ADAPTIVE LOOP TEST")
    print("=" * 30)

    # First thought cycle

    observation = ooda_loop.observe(
        question
    )

    orientation = ooda_loop.orient(
        observation
    )

    first_decision = ooda_loop.decide(
        orientation
    )

    print("\nFIRST DECISION:")
    print(first_decision)


    # Simulated verifier feedback

    verification = {
        "metadata": {
            "verdict": "REVIEW",
            "target": "LEFT",
            "response": (
                "Need empirical evidence "
                "and real-world implementations."
            )
        }
    }


    # Feedback changes strategy

    new_strategy = decision_feedback_bridge.update_strategy(
        verification
    )


    print("\nADAPTIVE STRATEGY:")
    print(new_strategy)


    # Second cognitive decision

    adaptive_decision = ooda_loop.decide(
        orientation,
        new_strategy
    )


    print("\nSECOND DECISION:")
    print(adaptive_decision)



if __name__ == "__main__":

    run_adaptive_test(
        "Should SCS use multiple specialised AI agents?"
    )