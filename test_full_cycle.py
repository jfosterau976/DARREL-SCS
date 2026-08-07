from core.coordinator import coordinator

print("=== SCS V0.1 FULL COGNITIVE CYCLE ===")

question = "Should SCS use multiple specialised AI agents instead of one large model?"

result = coordinator.process(question)

print("\n=== LEFT BRAIN ===")
print(result["left_brain"])

print("\n=== RIGHT BRAIN ===")
print(result["right_brain"])

print("\n=== SYNTHESIS ===")
print(result["synthesis"])

print("\n=== VERIFICATION ===")
print(result["verification"])

print("\n=== REFLECTION ===")
print(result["reflection"])

print("\n=== LEARNING ===")
print(result["learning"])

print("\n=== EXECUTIVE ===")
print(result["executive"])

print("\n=== STATUS ===")
print(result["status"])