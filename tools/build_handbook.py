from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HANDBOOK = ROOT / "docs" / "ENGINEERING_HANDBOOK"

CHAPTERS = {

    "00_Master_Index.md":
"""# DARREL Engineering Handbook

Version: 1.0 Foundation

This handbook is the authoritative engineering reference
for the DARREL Synthetic Cognitive System.

""",

    "01_Executive_Summary.md":
"""# Executive Summary

DARREL is a Synthetic Cognitive System (SCS).

Mission:
Build a modular, observable,
verifiable cognitive architecture.

""",

    "02_Vision_and_Philosophy.md":
"""# Vision & Philosophy

Architecture before implementation.

Reasoning must remain observable.

Verification remains independent.

Memory supports reasoning.

The Pulse Engine controls cognition.

""",

    "03_System_Architecture.md":
"""# System Architecture

User

↓

Dashboard

↓

Coordinator

↓

Pulse Engine

↓

Memory

↓

Left Brain

↓

Right Brain

↓

Synthesis

↓

Verification

↓

Reflection

↓

Learning

↓

Executive

""",

    "04_Cognitive_Blueprint.md":
"""# Cognitive Blueprint

(To be expanded.)

""",

    "05_Subsystem_Specifications.md":
"""# Subsystem Specifications

Every subsystem will contain:

Purpose

Responsibilities

Inputs

Outputs

Dependencies

Failure Modes

Recovery

Validation

Future Evolution

""",

    "06_Data_and_Memory.md":
"""# Memory System

(To be expanded.)

""",

    "07_Pulse_Engine.md":
"""# Pulse Engine

(To be expanded.)

""",

    "08_Telemetry.md":
"""# Telemetry

(To be expanded.)

""",

    "09_Dashboard_and_UI.md":
"""# Dashboard

(To be expanded.)

""",

    "10_Developer_Guide.md":
"""# Developer Guide

(To be expanded.)

""",

    "11_Testing_and_Validation.md":
"""# Testing

(To be expanded.)

""",

    "12_Release_Process.md":
"""# Release Process

Develop

↓

Validate

↓

Commit

↓

Push

↓

Release

""",

    "13_Roadmap.md":
"""# Roadmap

V0.2

V0.3

V1.0

""",

    "14_Engineering_Log.md":
"""# Engineering Log

Date

Objective

Changes

Validation

Next Steps

""",

    "15_Project_Constitution.md":
"""# DARREL Constitution

DARREL is a Synthetic Cognitive System.

The Pulse Engine controls cognition.

Reasoning is observable.

Verification is independent.

""",
}


def build():

    HANDBOOK.mkdir(
        parents=True,
        exist_ok=True
    )

    (HANDBOOK / "ADR").mkdir(
        exist_ok=True
    )

    (HANDBOOK / "diagrams").mkdir(
        exist_ok=True
    )

    for filename, contents in CHAPTERS.items():

        file = HANDBOOK / filename

        if not file.exists():

            file.write_text(
                contents,
                encoding="utf-8"
            )

            print("Created:", filename)

        else:

            print("Exists :", filename)

    adr = HANDBOOK / "ADR" / "ADR-000_TEMPLATE.md"

    if not adr.exists():

        adr.write_text(
"""# ADR Template

Decision

Context

Alternatives

Trade-offs

Consequences

Review

""",
            encoding="utf-8"
        )

        print("Created ADR template")

    print()
    print("=========================")
    print("HANDBOOK READY")
    print("=========================")

def scan_project():

    print()
    print("=========================")
    print("SCANNING PROJECT")
    print("=========================")

    folders = [
        "core",
        "agents",
        "dashboard",
        "memory",
        "plugins",
        "skills"
    ]

    report = "# Project File Inventory\n\n"

    for folder in folders:

        path = ROOT / folder

        report += f"## {folder}\n\n"

        if path.exists():

            for file in sorted(path.rglob("*.py")):

                report += f"- {file.relative_to(ROOT)}\n"

        report += "\n"

    inventory = HANDBOOK / "16_Project_Inventory.md"

    inventory.write_text(
        report,
        encoding="utf-8"
    )

    print("Created: 16_Project_Inventory.md")
if __name__ == "__main__":
    build()
    scan_project()