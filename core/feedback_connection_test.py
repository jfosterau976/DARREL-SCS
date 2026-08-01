from core.feedback_interpreter import feedback_interpreter


def test_feedback():

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

    result = feedback_interpreter.interpret(
        verification
    )

    print("FEEDBACK TEST RESULT:")
    print(result)


if __name__ == "__main__":
    test_feedback()