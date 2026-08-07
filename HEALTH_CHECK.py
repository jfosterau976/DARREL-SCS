import os
import subprocess
import importlib.util


def check(title, passed, details=""):

    status = "PASS" if passed else "FAIL"

    print(f"[{status}] {title}")

    if details:
        print(f"      {details}")


print("=" * 45)
print("DARREL SYSTEM HEALTH CHECK")
print("=" * 45)
print()

# Python

check(
    "Python",
    True
)

# Virtual Environment

check(
    "Virtual Environment",
    os.path.exists(".venv")
)

# requirements

check(
    "requirements.txt",
    os.path.exists("requirements.txt")
)

# Memory

check(
    "Memory Database",
    os.path.exists("scs_memory.json")
)

# Dashboard

check(
    "Dashboard",
    os.path.exists("dashboard")
)

# Core folder

check(
    "Core Modules",
    os.path.exists("core")
)

# Ollama

try:

    version = subprocess.check_output(
        ["ollama", "--version"],
        text=True
    ).strip()

    check(
        "Ollama",
        True,
        version
    )

except Exception:

    check(
        "Ollama",
        False
    )

# Models

try:

    models = subprocess.check_output(
        ["ollama", "list"],
        text=True
    )

    check(
        "qwen3:1.7b",
        "qwen3:1.7b" in models
    )

    check(
        "qwen3:4b",
        "qwen3:4b" in models
    )

except Exception:

    check(
        "LLM Models",
        False
    )

# Flask

check(
    "Flask Installed",
    importlib.util.find_spec("flask") is not None
)

print()
print("=" * 45)
print("Health Check Complete")
print("=" * 45)