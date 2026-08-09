\# DARREL / Synthetic Cognitive System (SCS)

\# Master Engineering Handover



\## Purpose



This file is the concise repository-native handover for DARREL / SCS.



It bridges:

\- the historical engineering handover

\- the current verified V0.2 implementation

\- the new V1 architecture direction



It is designed to be readable by Codex, GitHub users, and future engineers.



For current implementation truth:

\- live reproducible code wins



For future architectural intent:

\- docs/engineering/V1\_ARCHITECTURE\_ROADMAP.md

\- docs/engineering/ENGINEERING\_DECISIONS.md



For current known implementation state:

\- docs/engineering/CURRENT\_BUILD\_STATUS.md



Current synchronization baseline:



\- 177e500 — synchronized V0.2 to V0.3 engineering boundary



\- d56a570 â€” engineering knowledge base and V1 roadmap

\- 10504e5 â€” Cognitive Budget Manager V0.1 shadow telemetry

\- bef072e â€” Neural Routing V0.1 shadow telemetry

\- 0521a8f â€” memory-isolated safe test runner



\---



\# 1. Project Identity



Public assistant:



DARREL



Nickname:



Dazza



Underlying technology/project:



Synthetic Cognitive System (SCS)



DARREL is not intended to be a chatbot wrapped around one LLM.



The core experiment is whether selective activation, specialised cognitive modules, persistent memory, verification, learning feedback, provider choice, and eventually adaptive routing can produce measurable benefits over a direct LLM call.



The LLM is a reasoning engine DARREL can use.



It is not DARREL itself.



\---



\# 2. Core Hypothesis



The central hypothesis is not:



"More agents are automatically smarter."



The hypothesis is:



An AI system may improve efficiency, persistence, adaptability, and reasoning quality if it can estimate what cognition is required and activate only the minimum useful resources.



Conceptually:



INPUT

→ estimate cognitive requirement

→ route

→ Selective Pulse

→ execute useful cognition

→ verify/evaluate

→ learn

→ improve future routing decisions



A simple task should avoid expensive unnecessary cognition.



A complex task may justify:

\- multiple perspectives

\- memory

\- research

\- stronger providers

\- synthesis

\- deeper verification

\- planning

\- reflection



Selective cognition is fundamental.



\---



\# 3. Current Authoritative Project



Primary project:



C:\\Projects\\DARREL\\DARREL-SCS



Older development tree:



C:\\Users\\justi\\synthetic-cognitive-system



The older tree must be preserved until fully audited.



Do not delete, rename, clean, or merge historical trees casually.



Current repository:



jfosterau976/DARREL-SCS



Primary branch:



main



The actual live filesystem, imports, tests, and reproducible runtime behavior override historical documentation when they disagree.



\---



\# 4. Current Known Execution Path



Current operational UI path:



dashboard/app.py

→ POST /process

→ core/coordinator.py

→ core/pulse.py

→ routing / activation

→ orchestration

→ registered cognitive modules

→ verification / learning where activated

→ final response



Historical orchestration has included:



core/pulse\_orchestrator\_V3.py



Module registration has included:



core/module\_registry\_setup.py



Do not assume filenames alone are authoritative.



Trace imports and runtime execution.



main.py is not the primary cognitive request path.



SCS\_START.py is not the primary cognitive request path.



\---



\# 5. Current Core Architecture



Current conceptual architecture includes:



\- Dashboard / user input

\- Central Coordinator

\- Selective Pulse Engine

\- routing / cognitive assessment

\- Left Brain / analytical reasoning

\- Right Brain / creative or exploratory reasoning

\- Synthesis

\- Verifier

\- Reflection

\- Learning

\- Persistent Memory

\- provider abstraction

\- experimental/future Executive layer



Not every module should run on every request.



The Selective Pulse Engine remains the architectural gatekeeper.



\---



\# 6. Selective Pulse Engine



This is one of DARREL's foundational architecture ideas.



DARREL should not automatically run:



Left Brain

\+ Right Brain

\+ synthesis

\+ verifier

\+ memory

\+ reflection

\+ learning

\+ Executive



for every question.



Instead:



INPUT

→ assess cognitive requirement

→ activate minimum useful resources

→ generate cognition

→ verify where justified

→ learn/store where justified

→ OUTPUT



The goal is not maximum cognitive activity.



The goal is useful cognitive activity.



\---



\# 7. Known Core Files



Important current or historically live files include:



core/coordinator.py

core/pulse.py

core/pulse\_orchestrator\_V3.py

core/module\_registry.py

core/module\_registry\_setup.py

core/left\_brain.py

core/right\_brain.py

core/synthesis\_agent.py

core/verifier\_engine.py

core/reflection\_agent.py

core/learning\_extractor.py

core/learning\_feedback.py

core/memory\_consolidator.py

core/scs\_executive.py

core/llm\_interface.py

core/goal\_planning\_engine.py



Other router/controller files may exist.



Examples historically include:



\- attention\_router

\- tree\_router

\- cognitive controllers

\- effort controllers

\- unified pulse experiments



Do not assume a file is live simply because it exists.



\---



\# 8. Dashboard



Key dashboard files:



dashboard/app.py

dashboard/templates/index.html

dashboard/static/js/app.js



Important historical warning:



A previous manual-edit incident placed JavaScript into the Python backend.



When directing manual changes, always specify:



FILE

ACTION

LANGUAGE

RUN METHOD



Do not make the operator guess where code belongs.



\---



\# 9. Local Environment



Repository virtual environment:



C:\\Projects\\DARREL\\DARREL-SCS\\.venv



Known Python version:



3.14.7



Activation:



.\\.venv\\Scripts\\Activate.ps1



Expected PowerShell prompt begins:



(.venv) PS C:\\Projects\\DARREL\\DARREL-SCS>



Known local inference:



Ollama



Known local model:



qwen3:1.7b



Do not recreate or upgrade the environment casually.



Capture and test before changing dependencies.



\---



\# 10. Provider Architecture



The provider abstraction belongs centrally in:



core/llm\_interface.py



Cognitive modules should not hard-code individual provider APIs.



Current architecture supports:



\- Ollama / Qwen

\- Anthropic / Claude



Future providers may include other model or tool systems.



Provider choice should eventually become part of selective cognition.



Potential future factors:



\- task complexity

\- latency

\- cost

\- privacy

\- availability

\- historical quality

\- specialization



Cloud does not replace local.



Local inference remains valuable for:



\- offline operation

\- privacy

\- no per-call API cost

\- fallback

\- baseline comparison

\- experimental independence



\---



\# 11. Secrets



Never hard-code:



\- API keys

\- passwords

\- recovery codes

\- tokens

\- account credentials



Secrets must not be committed to Git.



Environment-based secret handling is preferred.



If an external service requires login, the project owner logs in directly.



Do not ask for personal passwords.



\---



\# 12. Anthropic / Claude



Anthropic provider support is now implemented through the shared provider interface.



Ollama support remains preserved.



Current Anthropic default model is:



claude-sonnet-4-6



Provider failures may fall back to Ollama.



Fallbacks must be visible in telemetry.



Never make fallback behavior look like the originally requested provider succeeded.



Track:



\- requested provider

\- actual provider

\- fallback state

\- reason

\- latency

\- token metrics where available



\---



\# 13. Persistent Memory



Persistent memory is valuable system state.



Known active files include multiple memory stores, including:



scs\_memory.json

memory.json

message\_memory.json

memory/system\_memory.json

memory/improvement\_memory.json



There are also memory snapshots and backups.



Never:



\- delete memory casually

\- empty memory for debugging

\- overwrite memory without backup

\- migrate memory blindly

\- stage scs\_memory.json casually



Current learning is structured persistent experience and concepts.



It is not model-weight training.



IMPLEMENTED NOW:



core/cognitive\_memory.py accepts an explicit memory file or the SCS\_MEMORY\_FILE environment override. The safe runner uses this to redirect test writes to temporary memory. Default production memory behavior is unchanged when no override is supplied.



\---



\# 14. Memory Relevance



Memory must be relevant, not merely available.



A strong memory that is unrelated to the current task must not be injected simply because it has high importance or historical frequency.



A learned-memory contamination issue was found during benchmarking.



The issue caused generic prompts to receive unrelated historical SCS concepts.



A relevance gate was added to protect against this.



Regression tests now protect:



\- irrelevant strong learning not being injected

\- relevant learned concepts being available when appropriate



This principle is foundational.



\---



\# 15. Verification



Verification must be independent enough to disagree.



The verifier must not become a rubber stamp.



Current V0.2 behavior supports meaningful:



PASS

REVIEW



Current corrective pattern:



initial result

→ verifier

→ if REVIEW, one corrective revision

→ verifier again

→ stop



Avoid unlimited recursive correction loops.



\---



\# 16. Engineering Discipline



For every meaningful engineering change:



CHECKPOINT

→ ONE OBJECTIVE

→ CHANGE

→ TEST

→ MEASURE

→ COMPARE

→ KEEP OR REVERT



Never assume an architectural change improves DARREL.



Prove it.



\---



\# 17. Testing



Automated tests now cover areas including:



\- smoke behavior

\- contracts

\- corrective revision

\- provider failures

\- Anthropic provider behavior

\- provider telemetry

\- memory contracts

\- learned relevance



Safe deterministic tests should:



\- mock providers

\- avoid external calls

\- avoid persistent memory writes

\- use the repository virtual environment

\- disable bytecode generation where appropriate

\- report duration

\- inspect Git state after execution



Current verified V0.3 stabilization test state after deterministic provider-telemetry observation hardening:



37 safe deterministic tests passed

0 failed



No repository or persistent memory changes occurred during that run.



The safe suite includes provider, provider-telemetry, offline provider-diagnostic, telemetry-snapshot, memory, learned-relevance, and benchmark-result-contract coverage.



The safe runner also compares the protected-memory hash, length, and timestamp before and after execution. A change or fingerprint failure returns exit code 3 without attempting to rewrite memory. Redirected unittest output preserves the true process exit code.



Additional isolated shadow-layer results:



\- Neural Routing V0.1: 10 / 10 passed

\- Cognitive Budget Manager V0.1: 11 / 11 passed



Combined safe and shadow verification: 58 / 58 passed in 0.037 seconds of unittest time and 0.278 seconds of runner elapsed time.



The mocked provider-failure matrix explicitly covers connection, HTTP, timeout, malformed-response, empty-response, missing-metrics, primary-to-fallback failure, provider identity, and unexpected-error behavior.



Coordinator provider telemetry defensively copies and normalizes malformed metric mappings, known numeric counters, fallback flags, and missing provider identities after execution. Per-call additive data-quality metadata identifies any normalized fields. Provider selection, request, response, and fallback behavior are unchanged.



Neural Routing comparison telemetry defensively normalizes malformed nested observation inputs and identifies normalized fields through additive data-quality metadata. This reliability behavior does not grant routing authority.



Cognitive Budget comparison telemetry defensively normalizes malformed or non-finite numeric observations and reports affected fields. It does not enforce limits or alter production execution.



The benchmark result contract can discover files from directories with an optional pattern and emit human or machine-readable validation summaries. Validation is read-only, rejects non-finite numeric metrics, and returns non-zero for invalid or undiscovered artifacts. The 20 timestamped historical files pass; baseline\_results.json and results.json remain legacy incompatible aggregates.



\---



\# 18. Benchmarking



DARREL must be tested against direct model baselines.



Required or intended comparisons include:



Direct Qwen

vs

DARREL/Qwen



Direct Claude

vs

DARREL/Claude



Full DARREL

vs

DARREL without memory



Full DARREL

vs

DARREL without Right Brain



Full DARREL

vs

DARREL without synthesis



Full DARREL

vs

DARREL without verifier



Later:



rule-routed DARREL

vs

neural-routed DARREL



Track:



\- correctness

\- relevance

\- reasoning quality

\- creativity where relevant

\- unsupported claims

\- latency

\- tokens

\- provider cost

\- module activation

\- verifier outcome

\- memory usefulness

\- corrective behavior



Complexity without measurable benefit is a project risk.



\---



\# 19. Stable Checkpoints



Important rollback points include:



v0.1-dell-stable



v0.2-pre-claude



v0.2-pre-benchmark



Protected milestone checkpoint directories include:



checkpoints/neural\_routing\_v0\_1\_pre

checkpoints/cognitive\_budget\_v0\_1\_pre



Do not move or delete stable tags casually.



Checkpoint before risky changes involving:



\- routing

\- Pulse

\- memory

\- verifier

\- provider architecture

\- module registry

\- major schema changes



\---



\# 20. Current V0.2 State



Significant V0.2 hardening already completed includes:



\- authoritative import-path cleanup

\- Anthropic provider integration

\- Ollama preservation

\- provider-aware telemetry

\- provider fallback behavior

\- meaningful verifier PASS / REVIEW

\- corrective revision loop

\- separate corrective timing

\- automated regression tests

\- contract tests

\- provider failure tests

\- provider telemetry tests

\- memory contract tests

\- learned relevance tests

\- learned-memory contamination repair

\- benchmarking work

\- stable Git checkpoints

\- memory-isolated one-command safe regression runner

\- persistent-memory path isolation through SCS\_MEMORY\_FILE



Current V0.3 shadow / experimental work includes:



\- Neural Routing V0.1 prediction and comparison telemetry

\- Cognitive Budget Manager V0.1 proposal and observed-usage comparison telemetry



Current committed V0.3 stabilization support also includes a read-only development preflight, explicit safe/shadow/all test classification, configuration-only credential-redacted provider diagnostics, a benchmark result/capture contract, defensive telemetry snapshots, and fail-open shadow-contract reassertion. These milestones are protected by commits 601cd91, 611a773, 6dbcbd1, and c3974a6; mocked-resource cleanup is protected by 24e1a74.



These support changes do not grant routing or budget authority. V0.4 Cognitive Compiler implementation has not started.



Neither shadow layer has production authority. The current Attention Router remains authoritative and the Selective Pulse Engine remains the final execution gatekeeper.



Current implementation details should always be verified against the repository before changing code.



\---



\# 21. Current Priority



Current engineering priority is:



Finish and stabilize the V0.2 baseline while formally documenting the V0.2 â†’ V0.3 shadow boundary.



Near-term sequence:



1\. synchronize docs/engineering with current code and Git history

2\. preserve the completed one-command safe regression runner and memory isolation contract

3\. environment reproducibility

4\. provider validation

5\. benchmark repeatability

6\. telemetry

7\. documentation synchronization

8\. stable checkpoint

9\. continue V0.3 experiments only in measured shadow mode



The safe runner, Neural Routing shadow telemetry, and Cognitive Budget shadow telemetry are already implemented. Do not describe them as merely planned, and do not describe either shadow layer as production authority.



Do not jump directly into production Neural Routing.



\---



\# 22. Neural Routing



Neural Routing V0.1 is implemented as V0.3 shadow / experimental telemetry.



Production Neural Routing authority remains future architecture.



Current V0.1 implementation:



16 deterministic normalized cognitive signals.



Exact implemented signals are request length, multi-part density, constraint density, question breadth, factual lookup, calculation, analysis, comparison, planning, creativity, decision support, risk, safety, uncertainty, verification, and memory relevance.



The broader roadmap signal catalogue includes:



\- analysis

\- creativity

\- risk

\- safety

\- planning

\- memory relevance

\- uncertainty

\- research requirement

\- verification requirement

\- complexity

\- evidence need

\- tool need



Current static weighted predictions cover:



\- modules

\- complexity

\- risk



Provider, memory-system, tool, and learned-weight recommendations remain future work.



The implementation uses shadow mode.



The current router remains authoritative.



The Neural Router predicts only.



The Selective Pulse Engine remains final execution authority.



\---



\# 23. Neural Routing Shadow Mode



Current V0.1 process:



INPUT

→ current router makes live decision

→ neural router receives same task/signals

→ neural router predicts route

→ prediction logged

→ outcome compared

→ no production behavior changed



Only benchmark evidence should justify increased Neural Routing authority.



\---



\# 24. Post-Benchmark Architecture Direction



The project direction has expanded beyond the original handover.



Approved direction now contains implemented, shadow, and future states.



V0.3 SHADOW / EXPERIMENTAL:



\- Neural Routing V0.1 telemetry

\- Cognitive Budget Manager V0.1 telemetry



FUTURE V0.4+ / V1:



\- Cognitive Intake Layer

\- Cognitive Compiler

\- temporary cognitive execution graphs

\- Shared Cognitive Workspace

\- parallel independent cognition

\- provider-aware cognition

\- hierarchical memory

\- memory economics

\- adversarial verification

\- cognitive opposition

\- stopping intelligence

\- Cognitive Performance Ledger

\- cognitive economy

\- self-experimentation

\- production/learned Shadow Brain authority

\- production Cognitive Budget enforcement

\- Executive Resolution layer

\- learned reusable cognitive programs



These are documented in:



docs/engineering/V1\_ARCHITECTURE\_ROADMAP.md



Future items are approved direction, not current implementation.



\---



\# 25. Cognitive Compiler Direction



A major future V0.4/V1 concept is the Cognitive Compiler.



It is not implemented and V0.4 has not started.



DARREL should eventually compile a temporary cognitive program suited to each task.



Instead of one fixed pipeline:



task

→ assess cognition

→ allocate budget

→ compile execution graph

→ execute selected resources

→ evaluate

→ stop or continue

→ learn from outcome



Examples:



Simple arithmetic:

calculator

→ verifier



Research:

research

→ evidence analysis

→ reasoning

→ verifier



High-risk planning:

planning

→ independent reasoning

→ adversarial challenge

→ synthesis

→ safety verification



This is a signature future direction.



\---



\# 26. Cognitive Budget Direction



The Cognitive Budget Manager V0.1 now proposes diagnostic budgets in shadow mode. It records authority=false and enforced=false and cannot limit, stop, reroute, or otherwise change production execution.



Future DARREL may explicitly control:



"How much cognition is this task worth?"



Budget may include:



\- latency

\- model calls

\- tokens

\- API cost

\- local compute

\- memory depth

\- verifier depth

\- research depth

\- reasoning passes



Simple tasks should consume minimal cognitive budget.



Deeper cognition should justify its cost.



\---



\# 27. Stopping Intelligence



DARREL should eventually learn when more thinking is no longer worth the cost.



Continue signals may include:



\- unresolved contradiction

\- low confidence

\- missing evidence

\- verifier REVIEW

\- high safety risk

\- strong disagreement



Stop signals may include:



\- high confidence

\- independent agreement

\- low uncertainty

\- evidence saturation

\- low expected benefit of another reasoning step

\- budget exhaustion



The ability to stop intelligently is a core V1 direction.



\---



\# 28. Cognitive Performance Ledger



Future DARREL should record what cognition was used and whether it helped.



Potential fields:



\- task class

\- cognitive signals

\- route

\- modules

\- provider

\- tools

\- memory

\- latency

\- tokens

\- cost

\- verifier outcome

\- revision behavior

\- final result

\- outcome

\- lessons



This evidence should eventually improve future cognitive allocation.



\---



\# 29. Development Philosophy



Do not fall in love with the brain analogy.



Fall in love with measurable behavior.



Left Brain, Right Brain, neurons, synapses, and pulses are engineering metaphors.



If a simpler design performs better:



use the simpler design.



If a component does not earn its cost:



question it.



Preserve the Selective Pulse hypothesis while remaining willing to change individual mechanisms.



\---



\# 30. Operator Usability



Do not turn DARREL into a system only an engineer understands.



The operator should retain a simple workflow.



Target eventually:



1\. open project

2\. activate environment

3\. start required local services

4\. start DARREL

5\. open dashboard



Later automation should reduce this further.



\---



\# 31. When Giving Operator Commands



Use explicit instructions.



Example:



WHERE:

PowerShell



FOLDER:

C:\\Projects\\DARREL\\DARREL-SCS



RUN:

python dashboard\\app.py



EXPECT:

describe expected output



SEND BACK:

state exactly what evidence is needed



Do not make the operator debug ambiguous instructions.



\---



\# 32. When Giving Operator Code



Always specify:



FILE:

exact path



ACTION:

REPLACE ENTIRE FILE



or:



CHANGE ONLY THIS SECTION



Never leave the target ambiguous.



\---



\# 33. Preserve Before Deleting



Historical DARREL development contains:



\- duplicate implementations

\- obsolete-looking modules

\- checkpoints

\- backup files

\- partially superseded experiments

\- implicit schema contracts



Some apparently old files may contain the only known-good implementation of a component.



Rule:



preserve first

→ understand second

→ archive third

→ delete much later



\---



\# 34. Do Not Trust File Count



Do not judge DARREL by:



\- how many Python files exist

\- whether a filename sounds important

\- whether comments claim something is live

\- whether an LLM generates an impressive paragraph



Judge the system by:



\- actual execution

\- measurable architecture value

\- reproducibility

\- tests

\- latency

\- quality

\- selective activation

\- memory usefulness

\- verifier independence

\- outcome evidence



\---



\# 35. Technical Takeover Rule



A technical takeover is complete when an engineer can independently:



\- start DARREL

\- reproduce baseline behavior

\- explain the live import graph

\- identify persistent state

\- identify dependencies

\- run regression tests

\- explain provider behavior

\- roll back safely

\- distinguish current implementation from future architecture



Codex has now completed a significant portion of this inspection.



\---



\# 36. Final Decision Rule



When a new engineering question appears, resolve it in this order:



1\. inspect live code

2\. reproduce behavior

3\. inspect tests

4\. inspect persistent/environment state

5\. consult CURRENT\_BUILD\_STATUS.md

6\. consult ENGINEERING\_DECISIONS.md

7\. consult this handover

8\. consult V1\_ARCHITECTURE\_ROADMAP.md

9\. consult historical project material if needed



Then add verified knowledge back into repository documentation.



The goal is to reduce dependence on oral or chat history over time.



\---



\# 37. Final Message to Future Engineers



Protect the working build.



Challenge assumptions.



Measure everything.



Keep providers interchangeable.



Allow verification to disagree.



Keep memory selective.



Keep cognition selective.



Do not preserve complexity for its own sake.



DARREL is not the LLM.



The LLM is an engine DARREL can use.



The Synthetic Cognitive System is everything deciding:



when

why

how

how deeply

with which resources

and whether



that engine — and the rest of DARREL's cognition — should fire.



The long-term architecture is:



Estimate cognition

→ allocate resources

→ compile a temporary cognitive program

→ execute

→ measure whether it helped

→ learn how to allocate cognition better next time.



DARREL should evolve toward a learned operating system for intelligence.

