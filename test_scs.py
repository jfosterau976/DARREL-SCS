import time
from core.llm_interface import LLMInterface

print("START")

llm = LLMInterface("Test Model", "local")

print("CONNECTING")
print(llm.connect())

print("GENERATING")
start = time.time()

result = llm.generate(
    "Reply with exactly: SCS TEST OK"
)

elapsed = time.time() - start

print("SECONDS:", round(elapsed, 2))
print("RESULT:", result)
print("DONE")