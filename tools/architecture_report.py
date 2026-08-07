from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MODULE_FILE = ROOT / "docs" / "ENGINEERING_HANDBOOK" / "20_Module_Reference.md"
DEP_FILE = ROOT / "docs" / "ENGINEERING_HANDBOOK" / "21_Dependency_Map.md"
OUTPUT = ROOT / "docs" / "ENGINEERING_HANDBOOK" / "22_Architecture_Report.md"


def build():

    report = "# DARREL Architecture Report\n\n"

    report += "## Overview\n\n"
    report += "This report is automatically generated from the DARREL source code.\n\n"

    if MODULE_FILE.exists():
        report += "## Module Inventory\n\n"
        report += MODULE_FILE.read_text(encoding="utf-8")
        report += "\n\n"

    if DEP_FILE.exists():
        report += "## Dependency Map\n\n"
        report += DEP_FILE.read_text(encoding="utf-8")
        report += "\n\n"

    report += """
# Current Cognitive Pipeline

User
    │
    ▼
Dashboard
    │
    ▼
Coordinator
    │
    ▼
Pulse Engine
    │
 ┌──┴─────────────┐
 ▼                ▼
Left Brain    Right Brain
      │
      ▼
  Synthesis
      │
      ▼
 Verification
      │
      ▼
 Reflection
      │
      ▼
  Learning
      │
      ▼
 Executive
      │
      ▼
 Dashboard
"""

    OUTPUT.write_text(report, encoding="utf-8")

    print("Created:", OUTPUT)


if __name__ == "__main__":
    build()