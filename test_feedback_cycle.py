from core.coordinator import coordinator

print("=== SCS V0.1 FEEDBACK CYCLE ===")

result = coordinator.process(
    "Should SCS use multiple specialised AI agents instead of one large model?"
)

print("\n=== CYCLES ===")
print(result["cycles"])

print("\n=== INITIAL VERIFICATION ===")
print(result["results"]["verification"])

if "revision" in result["results"]:

    print("\n=== REVISION OCCURRED ===")
    print(result["results"]["final"]["response"])

    print("\n=== FINAL VERIFICATION ===")
    print(result["results"]["final_verification"])

else:

    print("\n=== NO REVISION REQUIRED ===")
    print(result["results"]["final"]["response"])

print("\n=== COMPLETE ===")