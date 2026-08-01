from core.coordinator import coordinator

print("=== SCS V0.1 VERIFIED COGNITIVE CYCLE ===")

result = coordinator.process(
    "Should we build a multi-agent AI system instead of relying on one large model?"
)

print("\n=== LEFT BRAIN ===")
print(result["left_brain"]["response"])

print("\n=== RIGHT BRAIN ===")
print(result["right_brain"]["response"])

print("\n=== SYNTHESIS ===")
print(result["synthesis"]["response"])

print("\n=== VERIFICATION ===")
print(result["verification"])

print("\n=== FINAL STATUS ===")
print(result["verification"]["status"])