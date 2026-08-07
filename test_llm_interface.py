from core.llm_interface import llm_interface


print("MODEL:", llm_interface.model_name)

result = llm_interface.generate(
    "Answer in two short sentences: What is selective attention in an AI system?"
)

print("STATUS:", result.get("status"))
print("FALLBACK:", result.get("fallback"))
print("RESPONSE:")
print(result.get("response"))
print("ERROR:", result.get("error"))