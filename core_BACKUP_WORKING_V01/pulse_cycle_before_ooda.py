from core.pulse_router import pulse_router


def clean_agent_result(result, name):

    if isinstance(result, dict):

        if result.get("status") in [
            "timeout",
            "error"
        ]:
            return f"{name} unavailable for this pulse."

    return result



def run_pulse(question, feedback=None):

    print("\nSCS PULSE")
    print("Question:", question)

    decision = pulse_router.decide(
        question,
        feedback
    )

    print("\nROUTER DECISION:")
    print(decision)

    results = {}


    # LEFT BRAIN

    if decision["left"]:

        print("\n[LEFT BRAIN] ACTIVE")

        try:
            from agents.analysis_agent import analysis_agent

            results["left"] = analysis_agent.run(
                question
            )

            print("\n[LEFT BRAIN RESULT]")
            print(results["left"])

        except Exception as error:

            results["left"] = {
                "status": "error",
                "message": str(error)
            }

            print("\n[LEFT BRAIN ERROR]")
            print(error)

    else:

        print("\n[LEFT BRAIN] OFF")


    # RIGHT BRAIN

    if decision["right"]:

        print("\n[RIGHT BRAIN] ACTIVE")

        try:
            from agents.right_brain import right_brain

            results["right"] = right_brain.run(
                question
            )

            print("\n[RIGHT BRAIN RESULT]")
            print(results["right"])

        except Exception as error:

            results["right"] = {
                "status": "error",
                "message": str(error)
            }

            print("\n[RIGHT BRAIN ERROR]")
            print(error)

    else:

        print("\n[RIGHT BRAIN] OFF")


    # SYNTHESIS

    if decision["synthesis"]:

        print("\n[SYNTHESIS] ACTIVE")

        try:
            from agents.synthesis_agent import synthesis_agent

            left = clean_agent_result(
                results.get("left", ""),
                "LEFT BRAIN"
            )

            right = clean_agent_result(
                results.get("right", ""),
                "RIGHT BRAIN"
            )

            results["synthesis"] = synthesis_agent.synthesize(
                question,
                left,
                right
            )

            print("\n[SYNTHESIS RESULT]")
            print(results["synthesis"])

        except Exception as error:

            results["synthesis"] = {
                "status": "error",
                "message": str(error)
            }

            print("\n[SYNTHESIS ERROR]")
            print(error)

    else:

        print("\n[SYNTHESIS] OFF")


    # VERIFIER

    if decision["verifier"]:

        print("\n[VERIFIER] ACTIVE")

        try:
            from agents.verifier_agent import verifier_agent

            target = results.get(
                "synthesis",
                results.get(
                    "right",
                    results.get(
                        "left",
                        ""
                    )
                )
            )

            results["verification"] = verifier_agent.check(
                target
            )

            print("\n[VERIFICATION RESULT]")

            if hasattr(
                results["verification"],
                "to_dict"
            ):

                print(
                    results["verification"].to_dict()
                )

            else:

                print(
                    results["verification"]
                )

        except Exception as error:

            print("\n[VERIFIER ERROR]")
            print(error)


    else:

        print("\n[VERIFIER] OFF")


    return results



def run_targeted_cycle(question, max_pulses=3):

    print("\nSCS TARGETED PULSE CYCLE")
    print("=" * 30)

    feedback = None

    for pulse_number in range(
        1,
        max_pulses + 1
    ):

        print(
            f"\nPULSE {pulse_number}"
        )

        results = run_pulse(
            question,
            feedback
        )

        verification = results.get(
            "verification"
        )

        if verification and hasattr(
            verification,
            "to_dict"
        ):

            data = verification.to_dict()

            metadata = data.get(
                "metadata",
                {}
            )

            verdict = metadata.get(
                "verdict"
            )

            target = metadata.get(
                "target"
            )

            print(
                "\nVERIFICATION STATUS:",
                data.get("status")
            )

            print(
                "VERDICT:",
                verdict
            )

            print(
                "NEXT TARGET:",
                target
            )

            if verdict == "PASS":

                print(
                    "\nSCS RESULT VERIFIED."
                )

                break

            if target:

                feedback = {
                    "target": target
                }

        else:

            print(
                "\nNo verification result."
            )

            break


    print(
        "\nTOTAL PULSES:",
        pulse_number
    )



if __name__ == "__main__":

    run_targeted_cycle(
        "Should SCS use multiple specialised AI agents instead of one large model?"
    )