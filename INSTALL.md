# DARREL / SCS Installation Guide

## Project

Synthetic Cognitive System (SCS)

Public assistant name: DARREL

Current stable version: SCS V0.1

---

## 1. Required Programs

Install these on a clean Windows computer:

* Google Chrome
* Python 3.14 64-bit
* Git
* Visual Studio Code
* Ollama

When installing Python, make sure:

* Python is added to PATH
* `py.exe` launcher is installed

---

## 2. Copy the Project

Copy the entire folder:

`synthetic-cognitive-system`

Do not copy only individual Python files.

The project copy must include:

* core
* agents
* memory
* plugins
* skills
* dashboard
* darrel_ui_demo
* backups
* test files
* requirements.txt
* scs_memory.json

The `.venv` folder does not need to be transferred because it should be recreated on the new computer.

---

## 3. Open PowerShell

Go to the project folder.

Example:

`cd C:\Users\<USERNAME>\synthetic-cognitive-system`

---

## 4. Create the Python Virtual Environment

Run:

`python -m venv .venv`

Activate it:

`.\.venv\Scripts\activate`

The PowerShell prompt should then begin with:

`(.venv)`

---

## 5. Install Python Packages

Run:

`python -m pip install --upgrade pip`

Then:

`pip install -r requirements.txt`

---

## 6. Install Ollama Models

Check Ollama:

`ollama --version`

Install the main DARREL model:

`ollama pull qwen3:1.7b`

Install the larger test model:

`ollama pull qwen3:4b`

Check installed models:

`ollama list`

Expected models include:

* qwen3:1.7b
* qwen3:4b

DARREL currently uses:

`qwen3:1.7b`

---

## 7. Test the LLM Connection

Run:

`python test_llm_interface.py`

Expected:

* MODEL: qwen3:1.7b
* STATUS: success
* FALLBACK: False
* A generated model response

---

## 8. Test Selective Routing

Run:

`python test_selective_routing.py`

Expected:

Simple:

* left_reasoning
* verifier

Medium:

* left_reasoning
* right_reasoning
* synthesis
* verifier

High:

* goal_planning
* left_reasoning
* right_reasoning
* synthesis
* verifier
* reflection
* learning

All listed modules should show:

`executed`

---

## 9. Test the Full Cognitive System

Run:

`python test_full_cycle.py`

Expected final result:

`=== STATUS ===`

`workspace_complete`

---

## 10. Start the DARREL Dashboard

From the main project folder run:

`python dashboard\app.py`

Then open Chrome:

`http://127.0.0.1:5000`

The dashboard should connect to the Python SCS backend.

---

## 11. Important Project Data

Do not lose:

`scs_memory.json`

This contains DARREL's persistent SCS memory.

Also keep the entire:

`backups`

folder.

Important stable checkpoint:

`backups\SCS_V0.1_FINAL_STABLE`

Other later stable checkpoints may also exist and should be retained.

---

## 12. Current LLM

Provider:

Ollama

Current main model:

`qwen3:1.7b`

Available larger model:

`qwen3:4b`

Ollama API:

`http://127.0.0.1:11434/api/generate`

---

## 13. Development Rules

When modifying SCS:

1. Work on one feature at a time.
2. Prefer replacing complete small files instead of patching many lines.
3. Test after a related group of changes.
4. If a test fails, stop and fix it before continuing.
5. Create a checkpoint after important stable milestones.
6. Do not modify stable backup folders.
7. Keep SCS V0.1 available as a rollback point while developing V0.2.

---

## 14. Recovery

If the active project becomes damaged, restore from:

`backups\SCS_V0.1_FINAL_STABLE`

Do not overwrite the stable backup while troubleshooting.

---

## 15. Current Development Direction

SCS V0.1 is the stable architecture prototype.

SCS V0.2 development begins with:

* Local LLM integration
* Genuine Left Brain reasoning
* Genuine Right Brain reasoning
* Improved synthesis
* Improved verification
* Live cognitive telemetry
* Pulse history
* Improved measurable learning

DARREL should remain compatible with the stable V0.1 architecture while V0.2 is developed.
