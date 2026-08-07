import os
import subprocess
import sys
import importlib.util


results = []


def record(name, passed, details=""):
    results.append((name, passed, details))

    status = "PASS" if passed else "FAIL"

    print(f"[{status}] {name}")

    if details:
        print(f"       {details}")


def run_command(name, command):

    try:

        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300
        )

        passed = completed.returncode == 0

        details = (
            completed.stdout.strip()
            if passed
            else completed.stderr.strip()
        )

        record(
            name,
            passed,
            details[-500:]
        )

        return passed

    except Exception as error:

        record(
            name,
            False,
            str(error)
        )

        return False


print()
print("=" * 55)
print("DARREL FULL SYSTEM VALIDATION")
print("=" * 55)
print()


record(
    "Python Runtime",
    sys.version_info.major == 3
)

record(
    "Virtual Environment",
    os.path.exists(".venv")
)

record(
    "Core Folder",
    os.path.isdir("core")
)

record(
    "Agents Folder",
    os.path.isdir("agents")
)

record(
    "Dashboard Folder",
    os.path.isdir("dashboard")
)

record(
    "Memory Database",
    os.path.isfile("scs_memory.json")
)

record(
    "requirements.txt",
    os.path.isfile("requirements.txt")
)

record(
    "Flask Installed",
    importlib.util.find_spec("flask") is not None
)


run_command(
    "Git Status",
    [
        "git",
        "status",
        "--short"
    ]
)


run_command(
    "Compile Active Python",
    [
        sys.executable,
        "-m",
        "compileall",
        "-q",
        "-x",
        ".*(BACKUP|backup|before_orchestrator_fix).*",
        "core",
        "agents",
        "plugins",
        "dashboard"
    ]
)


run_command(
    "Selective Routing",
    [
        sys.executable,
        "test_selective_routing.py"
    ]
)


run_command(
    "Pulse Engine",
    [
        sys.executable,
        "test_pulse_engine.py"
    ]
)


run_command(
    "Full Cognitive Cycle",
    [
        sys.executable,
        "test_full_cycle.py"
    ]
)


run_command(
    "LLM Interface",
    [
        sys.executable,
        "test_llm_interface.py"
    ]
)


try:

    models = subprocess.check_output(
        [
            "ollama",
            "list"
        ],
        text=True,
        timeout=30
    )

    record(
        "Ollama qwen3:1.7b",
        "qwen3:1.7b" in models
    )

    record(
        "Ollama qwen3:4b",
        "qwen3:4b" in models
    )

except Exception as error:

    record(
        "Ollama Models",
        False,
        str(error)
    )


passed_count = sum(
    1
    for _, passed, _ in results
    if passed
)

failed_count = len(results) - passed_count


print()
print("=" * 55)
print("VALIDATION SUMMARY")
print("=" * 55)

print(
    f"PASS: {passed_count}"
)

print(
    f"FAIL: {failed_count}"
)

print()


if failed_count == 0:

    print(
        "DARREL STATUS: READY FOR DEVELOPMENT"
    )

else:

    print(
        "DARREL STATUS: ATTENTION REQUIRED"
    )


print("=" * 55)