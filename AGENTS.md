\# DARREL / SCS Engineering Instructions



\## Project Identity



DARREL (nickname: Dazza) is the public-facing assistant.



The underlying technology is the Synthetic Cognitive System (SCS).



DARREL is not a single LLM. LLMs are interchangeable reasoning resources inside the wider SCS architecture.



\## Source of Truth



For current implementation state:

\- live reproducible code is authoritative



For intended architecture and future direction:

\- docs/engineering is authoritative



Do not assume roadmap features are already implemented.



\## Required Reading Before Architectural Work



Before making architectural changes, read:



1\. docs/engineering/CURRENT\_BUILD\_STATUS.md

2\. docs/engineering/MASTER\_ENGINEERING\_HANDOVER.md

3\. docs/engineering/COMPLETE\_ENGINEER\_HANDBOOK.md

4\. docs/engineering/SENIOR\_ENGINEER\_FAQ.md

5\. docs/engineering/V1\_ARCHITECTURE\_ROADMAP.md

6\. docs/engineering/ENGINEERING\_DECISIONS.md



If any of these files are missing, report that before architectural work.



\## Core Engineering Rules



\- One controlled engineering objective at a time.

\- Protect stable checkpoints before major changes.

\- Measure whether each change improves the system.

\- Prefer the smallest change that advances the core hypothesis.

\- Do not add complexity unless it produces measurable benefit.

\- Preserve provider independence.

\- Preserve the Selective Pulse Engine as the final executive activation gate.

\- Memory must be relevant, not merely available.

\- Verification must be able to disagree with reasoning outputs.

\- Internal cognition may be rich while user-facing output remains concise.

\- Prefer selective cognition over activating every module on every request.



\## Current Architectural Direction



DARREL's long-term direction is:



Input

→ estimate required cognition

→ allocate a cognitive budget

→ build a temporary cognitive execution program

→ activate only useful modules/providers/tools/memory

→ execute

→ synthesize when needed

→ verify/adversarially challenge when justified

→ decide whether more thinking is worthwhile

→ produce final output

→ record outcome

→ learn how to allocate cognition better next time



\## Selective Pulse Engine



The Selective Pulse Engine remains the executive gatekeeper.



Future routing systems, including neural routing, may recommend activation but do not directly bypass the Pulse Engine.



\## Neural Routing



Future Neural Routing should begin in shadow mode.



Initial design:

\- approximately 10–20 cognitive signal neurons

\- signals may represent analysis, creativity, uncertainty, risk, safety, planning, memory relevance, research need, verification need and related cognitive requirements

\- weighted connections route signals toward modules/providers

\- weights may adapt from measured outcomes later

\- current router remains authoritative during shadow testing

\- Pulse Engine makes the final activation decision



Do not promote Neural Routing to production authority without benchmark evidence.



\## V1 Direction



Important future architecture includes:



\- Cognitive Intake Layer

\- Cognitive Budget Manager

\- Cognitive Compiler

\- temporary cognitive execution graphs

\- specialist modules that remain inactive unless useful

\- provider-aware cognition

\- parallel independent cognition where appropriate

\- hierarchical memory

\- memory economics and relevance

\- adversarial verification modes

\- cognitive opposition / skeptic reasoning

\- stopping intelligence

\- Cognitive Performance Ledger

\- routing outcome learning

\- shadow experiments and A/B evaluation

\- executive resolution/compression

\- learned reusable cognitive strategies



The central long-term idea is:



Estimate cognition

→ allocate resources

→ compile a temporary cognitive program

→ execute

→ measure whether the cognition helped

→ learn how to allocate cognition better next time



DARREL should evolve toward a learned operating system for intelligence.



\## Safety / Repository Protection



Never:

\- delete persistent memory unless explicitly instructed

\- overwrite or clear memory files casually

\- run destructive Git clean/reset commands

\- delete checkpoint or backup files without explicit review

\- expose API keys, tokens, passwords or secrets

\- store secrets in Git

\- silently modify unrelated files

\- commit or push unless explicitly instructed



Persistent memory files must be treated as protected state.



\## Testing



Prefer isolated deterministic tests first.



Mock external providers when testing provider behavior.



Avoid touching real persistent memory in safe regression tests.



Use the repository virtual environment:

C:\\Projects\\DARREL\\DARREL-SCS\\.venv\\Scripts\\python.exe



When possible:

\- disable bytecode generation for clean diagnostic runs

\- report exact tests run

\- report pass/fail

\- report duration

\- report repository changes

\- report Git status



\## Git Discipline



Before committing:

\- inspect git status

\- stage only intended files

\- do not stage scs\_memory.json unless explicitly instructed

\- do not stage unrelated backups/checkpoints

\- use descriptive DARREL versioned commit messages

\- preserve rollback points



\## Engineering Priority



Current priority is to finish and stabilize V0.2 before promoting major V0.3/V1 architecture.



Future concepts may be documented and prototyped in isolation, but must not destabilize the stable baseline.



\## Benchmarking Principle



Compare:

\- direct model baseline

\- full DARREL

\- DARREL without selected modules

\- alternative provider/model routes

\- later rule router versus neural router



Track:

\- output quality

\- correctness

\- latency

\- token use

\- provider cost

\- module activation

\- verifier result

\- memory usefulness

\- corrective revision behavior

\- final outcome



Architecture decisions should be evidence-driven.



\## Working Relationship



ChatGPT acts as lead architect / engineering coordinator.



Codex acts as the local execution and repository engineering environment.



GitHub acts as versioned source control and shared engineering history.



When architectural intent is unclear, stop and report the ambiguity rather than inventing a new direction.

