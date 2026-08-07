from core.pulse import pulse


tests = [
    {
        "name": "SIMPLE",
        "question": "What is 2 plus 2?"
    },
    {
        "name": "MEDIUM",
        "question": "Should SCS use multiple specialised AI agents?"
    },
    {
        "name": "HIGH",
        "question": "Analyse the safety risks of designing an AI healthcare assistant."
    }
]


for test in tests:

    result = pulse.run(test["question"])

    state = result.get("cognitive_state", {})

    modules = result.get(
        "execution_plan",
        {}
    ).get(
        "modules_to_run",
        []
    )

    execution_results = result.get(
        "execution",
        {}
    ).get(
        "results",
        {}
    )

    print("\n" + "=" * 50)
    print(test["name"])
    print("QUESTION:", test["question"])
    print("COMPLEXITY:", state.get("complexity"))
    print("RISK:", state.get("risk"))
    print("MODULES:", modules)

    for module_name, module_result in execution_results.items():
        print(
            module_name,
            "=",
            module_result.get("status")
        )