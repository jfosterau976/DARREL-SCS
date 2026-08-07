from core.pulse import pulse

question = "What is 2 plus 2?"

result = pulse.run(question)

verification = (
    result.get("execution", {})
    .get("results", {})
    .get("verifier", {})
    .get("output", {})
)

print("STATUS:", result.get("status"))
print("MODULES:", result.get("execution_plan", {}).get("modules_to_run"))
print("VERIFIER MODE:", verification.get("mode"))
print("VERDICT:", verification.get("verdict"))
print("CONFIDENCE:", verification.get("confidence"))