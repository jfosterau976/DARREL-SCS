from core.coordinator import coordinator

print("=== SCS V0.1 FULL COGNITIVE CYCLE ===")

result = coordinator.process(
    "Should SCS use multiple specialised AI agents instead of one large model?"
)

print("\n=== LEFT BRAIN ===")
print(result["left_brain"]["response"])

print("\n=== RIGHT BRAIN ===")
print(result["right_brain"]["response"])

print("\n=== SYNTHESIS ===")
print(result["synthesis"]["response"])

print("\n=== STATUS ===")
print(result["synthesis"]["status"])