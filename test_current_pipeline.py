from core.orchestrated_scs_v2 import orchestrated_scs_v2

print("=== SCS V0.1 CURRENT PIPELINE TEST ===")

question = "How can SCS improve its reasoning process?"

result = orchestrated_scs_v2.think(question)

print("\n=== RESULT KEYS ===")

print(result.keys())

print("\n=== FULL RESULT ===")

print(result)