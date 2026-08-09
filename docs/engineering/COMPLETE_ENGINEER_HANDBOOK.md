\# DARREL / SCS

\# COMPLETE ENGINEER HANDBOOK



Architecture • Build • Operations • Debugging • Testing • Takeover • V0.2 • V1 Direction



\## Purpose



Give an incoming engineer or Codex enough context to safely reproduce, understand, maintain, measure, debug, and continue DARREL without relying on chat history.



This repository handbook combines:



\- current verified implementation state

\- historical engineering lessons

\- operating procedures

\- debugging rules

\- testing discipline

\- provider architecture

\- memory rules

\- benchmark lessons

\- future architecture direction



For current implementation truth:

live reproducible code is authoritative.



For intended future architecture:

docs/engineering/V1\_ARCHITECTURE\_ROADMAP.md and ENGINEERING\_DECISIONS.md are authoritative.



Never put passwords, API keys, recovery codes, tokens, or other secrets in this handbook or Git.



\---



\# PART I — PROJECT ORIENTATION



\## 1. Project Identity



Public assistant:



DARREL



Nickname:



Dazza



Underlying technology:



Synthetic Cognitive System (SCS)



Current development target:



stabilize the V0.2 baseline and formally maintain the V0.2 â†’ V0.3 shadow boundary



DARREL is an experimental cognitive orchestration system.



It uses LLMs as reasoning engines but is intended to add value through:



\- selective routing

\- specialised cognitive roles

\- persistent state

\- synthesis

\- independent verification

\- learning feedback

\- provider choice

\- adaptive resource allocation

\- eventually learned routing and cognitive programming



DARREL is not the LLM.



\---



\## 2. Core Hypothesis



The hypothesis is not:



"Many agents are automatically smarter."



The hypothesis is:



An AI system may improve efficiency, persistence, adaptability and reasoning quality by estimating what cognition a task requires and activating only the minimum useful resources.



Core loop:



INPUT

→ estimate cognitive requirement

→ route

→ Selective Pulse

→ execute useful cognition

→ verify/evaluate

→ learn

→ improve future routing



A simple task should avoid unnecessary cognition.



A complex task may justify:



\- multiple perspectives

\- memory

\- planning

\- research

\- synthesis

\- verification

\- stronger models

\- deeper reasoning



\---



\## 3. Brain Analogy — Use Carefully



Left Brain, Right Brain, pulses, neurons and synapses are engineering metaphors.



They are useful only when they lead to measurable behavior.



Do not preserve a design simply because it sounds biologically plausible.



If a simpler architecture is:



\- faster

\- cheaper

\- easier to maintain

\- equally or more accurate



prefer the simpler implementation.



\---



\# PART II — WORKSTATION AND REPOSITORY



\## 4. Primary Locations



Current active project:



C:\\Projects\\DARREL\\DARREL-SCS



Older development location:



C:\\Users\\justi\\synthetic-cognitive-system



Preserve the older directory until it is deliberately audited.



Do not delete, rename, clean, or reorganise historical project trees casually.



\---



\## 5. Repository



GitHub:



jfosterau976/DARREL-SCS



Primary branch:



main



Current verified repository state must be checked before every major engineering session.



Useful commands:



git status



git log --oneline --decorate -20



Live code and Git history override stale documentation about implementation details.



\---



\## 6. PowerShell Entry



Enter project:



cd C:\\Projects\\DARREL\\DARREL-SCS



Expected location:



PS C:\\Projects\\DARREL\\DARREL-SCS>



\---



\## 7. Virtual Environment



Activate:



.\\.venv\\Scripts\\Activate.ps1



Expected prompt:



(.venv) PS C:\\Projects\\DARREL\\DARREL-SCS>



Known interpreter:



C:\\Projects\\DARREL\\DARREL-SCS\\.venv\\Scripts\\python.exe



Known current Python:



3.14.7



Do not recreate or delete .venv casually.



\---



\## 8. Environment Capture



Useful inspection commands:



python --version



where.exe python



pip list



pip freeze



ollama --version



ollama list



git status



git log --oneline --decorate -20



Codex may need narrowly scoped elevated permission to execute the repository Python interpreter because its managed Windows sandbox can block process creation.



This does not mean the virtual environment is broken.



\---



\# PART III — LIVE ARCHITECTURE



\## 9. Current Request Path



Current operational UI path:



dashboard/app.py

→ POST /process

→ coordinator.process()

→ pulse.run()

→ routing / activation

→ orchestration

→ reasoning modules

→ synthesis where selected

→ verification

→ reflection / learning where selected

→ final response



main.py is currently not the main cognitive request path.



SCS\_START.py is not the main cognitive request path.



Trace actual imports and runtime behavior before changing architecture.



\---



\## 10. Core Components



Current or historically live architecture includes:



\- dashboard / user input

\- coordinator

\- Selective Pulse Engine

\- routing / cognitive assessment

\- Left Brain

\- Right Brain

\- synthesis

\- verifier

\- planning

\- reflection

\- learning

\- persistent memory

\- provider interface

\- experimental/future Executive layer



Not every module should run on every request.



\---



\## 11. Known Core Files



Important files include:



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

core/neural\_routing\_layer.py

core/cognitive\_budget\_manager.py

scripts/test-darrel-safe.ps1



Other router/controller experiments have existed.



Examples:



\- attention\_router

\- tree\_router

\- cognitive\_controller

\- adaptive effort controllers

\- unified pulse experiments



Do not assume a file is live because its name sounds important.



Follow imports and callers.



\---



\# PART IV — SELECTIVE PULSE



\## 12. Selective Pulse Principle



Selective Pulse is one of DARREL's foundational ideas.



DARREL should not automatically execute:



Left Brain

\+ Right Brain

\+ synthesis

\+ verifier

\+ memory

\+ reflection

\+ learning

\+ Executive



for every request.



Instead:



INPUT

→ estimate required cognition

→ activate minimum useful resources

→ execute

→ verify where justified

→ learn/store where justified

→ OUTPUT



The goal is not maximum activity.



The goal is useful activity.



\---



\## 13. Current Cognitive Levels



Current known conceptual activation:



LOW:

\- left reasoning

\- verifier



MEDIUM:

\- left reasoning

\- right reasoning

\- synthesis

\- verifier



HIGH:

\- goal planning

\- left reasoning

\- right reasoning

\- synthesis

\- verifier

\- reflection

\- learning



Exact live code wins if this summary becomes stale.



\---



\## 14. Thinking Policy



LOW:

\- lightweight/no-think reasoning where possible



MEDIUM:

\- left/right can use lightweight reasoning

\- synthesis may use fuller reasoning



HIGH:

\- deeper reasoning may be justified



Corrective revision:

\- currently deliberately constrained



The system should use deeper cognition because it helps, not because it is available.



\---



\# PART V — PROVIDERS



\## 15. Provider Abstraction



Provider logic should live centrally in the shared LLM interface.



Individual cognitive modules should not directly hard-code provider APIs.



Provider independence is a core architectural rule.



\---



\## 16. Ollama / Qwen



Runtime:



Ollama



Known local model:



qwen3:1.7b



Known endpoint:



http://127.0.0.1:11434/api/generate



Known behavior includes:



\- stream false

\- temperature around 0.4

\- optional thinking

\- timing/token metrics



Local inference should remain supported because it provides:



\- offline operation

\- privacy

\- no per-call API cost

\- baseline comparison

\- fallback

\- experimental independence



\---



\## 17. Anthropic / Claude



Anthropic support is implemented through the common provider interface.



Current known model:



claude-sonnet-4-6



Provider selection may use:



SCS\_LLM\_PROVIDER=anthropic



Secret:



ANTHROPIC\_API\_KEY



Secrets must never be committed.



Anthropic failures may fall back to Ollama.



Fallback telemetry should distinguish:



\- requested provider

\- actual provider

\- fallback state

\- failure reason

\- timing

\- token metrics where available



Never hide a fallback as if the requested provider succeeded.



\---



\## 18. Provider Routing — Future



Provider selection should eventually become part of selective cognition.



Possible factors:



\- task type

\- complexity

\- latency

\- quality

\- cost

\- privacy

\- availability

\- specialization

\- historical success



Some tasks should use no LLM at all if deterministic tools are better.



\---



\# PART VI — MEMORY



\## 19. Persistent Memory



Persistent memory is protected system state.



Known files include:



scs\_memory.json

memory.json

message\_memory.json

memory/system\_memory.json

memory/improvement\_memory.json



There are also historical memory snapshots and backups.



Never:



\- delete memory casually

\- reset memory for convenience

\- empty memory during debugging

\- migrate memory blindly

\- stage scs\_memory.json without explicit review



Current learning is structured persistent experience and concepts.



It is not model-weight training.



IMPLEMENTED NOW:



core/cognitive\_memory.py accepts an explicit memory file or the SCS\_MEMORY\_FILE environment override. The safe runner redirects tests to temporary memory through this contract. Default production memory behavior is unchanged when no override is supplied.



\---



\## 20. Memory Relevance



Memory must be relevant, not merely available.



A major benchmark bug showed why this matters.



A generic AI-assistant prompt inherited high-strength historical SCS/multi-agent concepts even though those concepts were unrelated.



Root cause:



broad learned-memory injection with insufficient topical relevance filtering.



The fix added relevance gating.



Regression tests protect:



\- irrelevant strong concepts are not injected

\- relevant learned concepts can be injected



Strong evidence count must never override topical relevance.



\---



\## 21. Future Memory Direction



Approved future memory architecture may include:



\- working memory

\- episodic memory

\- semantic memory

\- procedural memory

\- user memory

\- project memory

\- hypothesis memory



Future memories may include economics metadata:



\- relevance

\- confidence

\- source quality

\- age

\- importance

\- usefulness

\- contradiction

\- reinforcement

\- decay

\- risk



\---



\# PART VII — VERIFICATION



\## 22. Verifier Principle



The verifier must genuinely be able to disagree.



A verifier that always approves reasoning is not a verifier.



\---



\## 23. Current Verification Flow



Current behavior:



initial result

→ verifier

→ PASS = return



or:



initial result

→ verifier REVIEW

→ one corrective revision

→ verifier again

→ stop



Unlimited recursive correction is intentionally avoided.



\---



\## 24. Future Verification



Potential future verifier modes:



\- logic

\- factual accuracy

\- mathematical correctness

\- hallucination

\- evidence adequacy

\- safety

\- contradiction

\- counterexample

\- assumption challenge

\- bias



Verifier depth should eventually be selective.



\---



\# PART VIII — DASHBOARD



\## 25. Dashboard Files



Backend:



dashboard/app.py



HTML:



dashboard/templates/index.html



JavaScript:



dashboard/static/js/app.js



\---



\## 26. Start Dashboard



From project root with venv active:



python dashboard\\app.py



Open the local Flask URL in Chrome.



Stop:



Ctrl+C



\---



\## 27. Presentation Principle



DARREL can generate large structured internal state.



Do not destroy useful internal diagnostics simply to make the UI shorter.



Correct design:



rich internal state

→ concise response/presentation boundary



Useful panels historically include:



\- Memory

\- Left Brain

\- Right Brain

\- Synthesis

\- Verifier

\- Executive



Expandable diagnostics can expose deeper state when needed.



\---



\# PART IX — KNOWN FAILURE HISTORY



\## 28. Wrong Verifier Contents



Historical incident:



core/verifier\_engine.py contained LeftBrain code.



Result:



ImportError / NameError failures.



Rule:



Verify exact file path before replacement.



After replacement:



\- inspect first lines

\- syntax/import test immediately



\---



\## 29. Zero-Byte Left Brain



Historical incident:



left\_brain.py was accidentally emptied.



Rule:



Protect checkpoints.



Check file size when a file unexpectedly fails imports.



\---



\## 30. Python Indentation



Manual copy/paste caused:



IndentationError



Rule:



Prefer complete valid functions/classes/files when manual replacement is unavoidable.



Run immediate syntax/import tests.



\---



\## 31. Schema Mismatch



Historical problem:



one module returned valid data but another expected a different dictionary structure.



Rule:



Implicit schemas are fragile.



Protect them with contract tests before refactoring.



\---



\## 32. PowerShell vs Python Confusion



Python code was previously pasted directly into PowerShell.



Rule:



Always distinguish:



RUN IN POWERSHELL



from:



PASTE INTO FILE



This is mandatory for operator instructions.



\---



\## 33. Ollama PATH Confusion



Ollama existed even when shell lookup initially failed.



Rule:



Verify installation/service/path before rewriting DARREL.



\---



\## 34. Missing Dependency



Search experiments previously failed because BeautifulSoup was missing.



Rule:



Capture environment and dependencies before rebuilding.



\---



\## 35. Frontend / Backend Mix-Up



JavaScript was once pasted into Python dashboard code.



Rule:



Always state:



FILE

PATH

LANGUAGE

ACTION



\---



\# PART X — BACKUPS AND CHECKPOINTS



\## 36. Historical Backups



The project contains numerous:



\- BEFORE\_\* files

\- \*\_checkpoint.py files

\- working checkpoint files

\- provider backups

\- memory snapshots

\- checkpoint directories



Do not clean these during routine development.



\---



\## 37. Preserve Before Deleting



Rule:



preserve

→ understand

→ archive

→ delete much later if justified



Git should become the main recovery mechanism, but historical backups remain useful until fully reconciled.



\---



\## 38. Stable Tags



Known important tags include:



v0.1-dell-stable



v0.2-pre-claude



v0.2-pre-benchmark



Protect stable rollback points.



\---



\# PART XI — DEVELOPMENT WORKFLOW



\## 39. One-Change Cycle



Every meaningful engineering change should follow:



DEFINE ONE OBJECTIVE

→ CHECKPOINT

→ CHANGE

→ TARGETED TEST

→ REGRESSION TEST

→ MEASURE

→ COMPARE

→ KEEP OR REVERT

→ DOCUMENT



Never bundle unrelated architecture changes before testing.



\---



\## 40. Before Changing Anything



Ask:



\- Can I reproduce current behavior?

\- Is there a checkpoint?

\- Do I know which file is live?

\- Do I understand the input/output contract?

\- What exact problem am I solving?

\- How will I measure improvement?

\- What regression protects the behavior?



\---



\## 41. Before Adding a Module



Ask:



\- What task class needs it?

\- Can an existing component solve it?

\- What is the latency/cost increase?

\- How will Pulse know when to activate it?

\- What benchmark proves benefit?

\- What happens when it is removed?



\---



\## 42. Before Adding Cloud Calls



Ask:



\- Does the task need a cloud model?

\- Can local inference solve it?

\- What is expected latency?

\- What is expected cost?

\- Is private context being sent externally?

\- What is the fallback?

\- Is provider selection visible in telemetry?



\---



\# PART XII — TESTING



\## 43. Testing Philosophy



Start with the smallest useful test.



Do not debug a huge cognitive run when a deterministic unit test can reveal the same issue.



\---



\## 44. Historical Smoke Tests



Simple:



2 + 2



Expected conceptually:



\- DARREL runs

\- Left Brain active

\- unnecessary modules skipped

\- answer 4



Architecture:



Should SCS be built as one giant AI model instead of multiple specialised AI agents?



Expected historically:



\- Left Brain

\- Right Brain

\- synthesis

\- verifier

\- selective activation



\---



\## 45. Current Test Inventory



Current handbook-era verified inventory includes:



tests/test\_smoke.py

\- 3 live-LLM smoke tests



tests/test\_contracts.py

\- 4 live-LLM/core contract tests



tests/test\_provider\_failures.py

\- 3 deterministic provider-failure tests



tests/test\_anthropic\_provider.py

\- 3 deterministic Anthropic/fallback tests



tests/test\_provider\_telemetry.py

\- 1 provider telemetry test



tests/test\_memory\_contract.py

\- 5 deterministic isolated memory tests



tests/test\_learned\_relevance.py

\- 2 deterministic learned-memory relevance tests

tests/test\_neural\_routing\_shadow.py

\- 6 deterministic Neural Routing shadow tests

tests/test\_cognitive\_budget\_shadow.py

\- 6 deterministic Cognitive Budget shadow tests



Verified full-suite result from the V0.2 hardening session:



20 / 20 passing



Historical measured full-suite time:



284.289 seconds



Current Codex safe deterministic subset:



13 / 13 passing



Current isolated shadow-layer suites:



\- Neural Routing V0.1: 6 / 6 passing

\- Cognitive Budget Manager V0.1: 6 / 6 passing



No persistent-memory or Git changes occurred.



\---



\## 46. Test Classification



The suite currently mixes:



FAST / DETERMINISTIC

and

LIVE / STATEFUL / LLM



This should be separated more clearly.



Safe tests should:



\- mock external providers

\- use temporary memory

\- avoid real persistent state

\- avoid unnecessary network calls

\- disable bytecode generation when useful

\- report duration

\- report Git state



\---



\## 47. Safe Test Automation



Implemented and committed script:



scripts/test-darrel-safe.ps1



Initial safe set:



tests.test\_anthropic\_provider

tests.test\_provider\_failures

tests.test\_memory\_contract

tests.test\_learned\_relevance



The runner should:



\- use repository .venv

\- use Python -B

\- set PYTHONDONTWRITEBYTECODE

\- return non-zero on failure

\- show PASS/FAIL

\- show elapsed time

\- show git status



The runner also redirects SCS\_MEMORY\_FILE to temporary memory and restores the previous environment afterward. The default production memory path is unchanged when no override is supplied.



\---



\# PART XIII — BENCHMARKING



\## 48. Why Benchmark



DARREL must prove that its extra cognition adds enough value to justify:



\- additional latency

\- additional tokens

\- additional provider cost

\- architectural complexity



\---



\## 49. Required Comparisons



Direct Qwen

vs

DARREL/Qwen



Direct Claude

vs

DARREL/Claude



Full DARREL

vs

no memory



Full DARREL

vs

no Right Brain



Full DARREL

vs

no synthesis



Full DARREL

vs

no verifier



Later:



rule router

vs

neural router



\---



\## 50. Benchmark Metrics



Track:



\- correctness

\- relevance

\- usefulness

\- reasoning quality

\- creativity where appropriate

\- unsupported claims

\- hallucinations

\- latency

\- tokens

\- provider cost

\- activated modules

\- verifier outcome

\- memory usefulness

\- corrective behavior



\---



\## 51. Benchmark Lesson



A 20-run benchmark using five prompts across four configurations demonstrated a central trade-off:



DARREL adds significant latency because multiple LLM calls execute.



The architecture appeared to provide relatively more value around the weaker local Qwen model than around Claude in some task classes.



This is a critical finding.



It suggests the system should become more selective rather than simply adding more cognition.



\---



\# PART XIV — POST-BENCHMARK ARCHITECTURE



\## 52. Main Performance Bottleneck



Sequential LLM inference dominates wall-clock latency.



A medium cognitive path can perform multiple LLM calls that do not always need to be sequential.



High-leverage optimizations include:



\- parallel Left/Right cognition

\- shorter handoffs

\- conditional synthesis

\- cheap verification gates

\- provider-capability-aware cognition

\- stopping unnecessary reasoning



\---



\## 53. Neural-Linked Dual Brain



Approved experimental direction:



\- run independent analytical and creative perspectives in parallel when selected

\- exchange compact structured state

\- measure agreement/disagreement

\- invoke synthesis only where useful

\- escalate verification where risk or uncertainty justifies it



The dual-brain metaphor is not sacred.



The important feature is independent cognitive diversity.



\---



\## 54. Shared Cognitive Workspace



Future modules should exchange compact structured state instead of repeatedly copying full reports.



Potential workspace fields:



\- task

\- claims

\- hypotheses

\- confidence

\- uncertainty

\- evidence

\- risks

\- objections

\- memory references

\- budget

\- verifier feedback

\- execution state

\- stopping state



\---



\## 55. Agreement / Conflict Gate



Future lightweight evaluation can determine:



HIGH AGREEMENT

→ deterministic merge / skip synthesis



MATERIAL DISAGREEMENT

→ synthesis



HIGH UNCERTAINTY

→ stronger verification or additional cognition



This should reduce unnecessary model calls.



\---



\## 56. Cheap Verification Gate



Not every answer requires an expensive full verifier call.



Future low-cost signals may estimate:



\- agreement

\- uncertainty

\- evidence quality

\- safety risk

\- contradiction



Full verification can then activate selectively.



\---



\## 57. Provider Capability Awareness



The stronger the underlying provider, the less additional orchestration may be necessary for some tasks.



Future DARREL should learn:



\- when local Qwen benefits strongly from extra cognition

\- when Claude already solves the problem well directly

\- when synthesis adds little value

\- when cloud escalation is worth the cost



\---



\# PART XV — NEURAL ROUTING



\## 58. Neural Routing Status



Neural Routing V0.1 shadow telemetry is implemented as a V0.3 experiment.



Production routing authority remains future work.



Do not give it production authority during V0.2.



\---



\## 59. Initial Neuron Concept



Current V0.1 uses 16 deterministic normalized cognitive signals and static versioned weights.



Exact V0.1 signals are request length, multi-part density, constraint density, question breadth, factual lookup, calculation, analysis, comparison, planning, creativity, decision support, risk, safety, uncertainty, verification, and memory relevance.



The broader future signal catalogue includes:



\- analysis

\- creativity

\- planning

\- risk

\- safety

\- uncertainty

\- memory relevance

\- research need

\- verification need

\- complexity

\- evidence need

\- mathematics

\- tool need

\- provider capability

\- latency sensitivity

\- cost sensitivity

\- privacy sensitivity

\- disagreement

\- confidence

\- escalation need



\---



\## 60. Shadow Mode Is Mandatory



Neural Routing V0.1 is observation-only.



Current router:

controls real execution.



Neural router:

predicts what it would activate.



Log both decisions.



Compare against measured outcomes.



Do not change production behavior until evidence supports promotion.



\---



\## 61. Unresolved Neural Details



Do not prematurely freeze:



\- activation function

\- thresholds

\- initial weights

\- learning rate

\- reward function

\- credit assignment

\- weight update rules

\- confidence calibration



These should be selected experimentally.



\---



\# PART XVI — V1 ARCHITECTURE



\## 62. Cognitive Intake Layer



Future input analysis should estimate:



\- task type

\- analysis need

\- creativity need

\- research need

\- planning need

\- memory relevance

\- uncertainty

\- safety

\- verification need

\- complexity

\- expected value of deeper cognition



\---



\## 63. Cognitive Budget Manager



Cognitive Budget Manager V0.1 now proposes this answer in shadow mode. It compares the proposal with observed usage but has authority=false and enforced=false.



Future production DARREL may explicitly control:



"How much cognition is this task worth?"



Budget dimensions may include:



\- latency

\- tokens

\- API cost

\- provider calls

\- compute

\- memory depth

\- module count

\- reasoning passes

\- verifier depth

\- research depth



\---



\## 64. Cognitive Compiler



Major future V0.4/V1 concept.



The Cognitive Compiler is not implemented and V0.4 has not started.



Instead of one fixed cognitive pipeline, DARREL should compile a temporary task-specific execution graph.



Examples:



Simple arithmetic:



calculator

→ verifier



Research:



search

→ evidence analysis

→ reasoning

→ verifier



High-risk planning:



planner

→ independent cognition

→ adversarial challenge

→ synthesis

→ safety verification



\---



\## 65. Stopping Intelligence



Future DARREL should estimate whether another cognitive step has positive expected value.



Continue signals:



\- contradiction

\- low confidence

\- missing evidence

\- verifier REVIEW

\- high safety risk

\- meaningful disagreement



Stop signals:



\- confidence high

\- agreement high

\- uncertainty low

\- evidence saturated

\- little expected benefit

\- budget exhausted



\---



\## 66. Cognitive Performance Ledger



Future DARREL should record:



\- task class

\- cognitive signals

\- route

\- execution graph

\- modules

\- providers

\- tools

\- memory

\- latency

\- tokens

\- cost

\- verifier result

\- revision

\- final outcome

\- lessons



This becomes evidence for learning better cognitive allocation.



\---



\## 67. Cognitive Economy



Every module/provider should eventually have:



\- estimated cost

\- historical benefit

\- task-specific usefulness



The system should optimize expected cognitive value.



\---



\## 68. Self-Experimentation



Future DARREL may run controlled experiments:



\- route A vs route B

\- synthesis vs none

\- memory vs none

\- provider A vs B

\- shallow vs deep verification

\- rule router vs neural router



This means evidence collection.



It does not mean unrestricted autonomous production self-modification.



\---



\## 69. Learned Cognitive Programs



Long-term DARREL may learn reusable reasoning strategies.



Example:



high-risk comparison

→ research both sides

→ skeptic

→ synthesis

→ evidence verifier



These may become procedural memory.



\---



\## 70. Signature V1 Idea



Estimate cognition

→ allocate resources

→ compile temporary cognitive program

→ execute

→ measure whether it helped

→ learn how to allocate cognition better next time



DARREL should evolve toward a learned operating system for intelligence.



\---



\# PART XVII — ENGINEER TAKEOVER / DAILY OPERATIONS



\## 71. Before Taking Over



An engineer should be able to:



\- open the project

\- activate the environment

\- identify Git state

\- run safe tests

\- start DARREL

\- trace live imports

\- identify memory

\- identify provider configuration

\- identify rollback points

\- distinguish implemented features from roadmap ideas



\---



\## 72. Recommended Two-PowerShell Workflow



PowerShell 1:



run DARREL server.



PowerShell 2:



use for:



\- Git

\- diagnostics

\- file inspection

\- Ollama checks

\- tests



This avoids interrupting the running dashboard.



\---



\## 73. Operator Command Format



When giving manual commands, use:



WHERE:

PowerShell



FOLDER:

C:\\Projects\\DARREL\\DARREL-SCS



RUN:

exact command



EXPECT:

what should happen



SEND BACK:

what evidence is required



Avoid ambiguous instructions.



\---



\## 74. Code Edit Format



Always state:



FILE:

exact path



ACTION:

REPLACE ENTIRE FILE



or:



CHANGE ONLY THIS SECTION



Never say "replace it" without defining the target.



\---



\## 75. Error Reporting



When a failure occurs, capture the complete traceback.



Inspect:



\- first failing project file

\- line number

\- exception

\- import chain



Tracebacks have repeatedly revealed the real execution path more reliably than assumptions.



\---



\# PART XVIII — ENGINEERING ROLES



\## 76. Lead Architect



ChatGPT currently acts as:



lead architect / engineering coordinator.



Responsibilities:



\- preserve architectural direction

\- choose engineering sequence

\- review evidence

\- prevent drift

\- coordinate GitHub/Codex workflow

\- maintain engineering knowledge



\---



\## 77. Codex



Codex is the local execution and repository engineering environment.



Responsibilities:



\- inspect live code

\- edit local files

\- run tests

\- diagnose environment issues

\- automate repetitive work

\- follow AGENTS.md



\---



\## 78. GitHub



GitHub is the durable shared engineering history.



Store:



\- code

\- tests

\- architecture docs

\- engineering decisions

\- safe automation

\- checkpoints



Never store secrets.



\---



\# PART XVIII-A — CURRENT IMPLEMENTATION BOUNDARY



IMPLEMENTED NOW:



\- V0.2 Selective Pulse production path

\- provider abstraction and fallback telemetry

\- verifier PASS / REVIEW and one corrective revision

\- memory relevance protection

\- memory-isolated safe regression runner



V0.3 SHADOW / EXPERIMENTAL:



\- Neural Routing V0.1 predicts complexity, risk, and module candidates from 16 signals

\- Cognitive Budget Manager V0.1 proposes diagnostic budgets and compares observed usage



Neither shadow layer controls production. The current Attention Router remains authoritative and the Selective Pulse Engine remains the final execution gatekeeper.



FUTURE:



\- V0.4 Cognitive Compiler and temporary execution graphs

\- production or learned Neural Routing authority

\- production Cognitive Budget enforcement and stopping

\- remaining V1 architecture



\---



\# PART XIX — CURRENT STATUS



\## 79. Current Verified V0.2 Hardening State



Verified work from the 9 August engineering session includes:



\- reproducible startup/import documentation

\- Anthropic provider integration

\- Ollama preservation

\- provider failure/fallback telemetry

\- verifier contract repair

\- meaningful PASS / REVIEW

\- corrective revision

\- isolated memory contract tests

\- learned-memory relevance fix

\- learned-relevance regression tests

\- complete automated suite reaching 20/20

\- protected pre-benchmark checkpoint

\- provider benchmarking

\- post-benchmark architecture planning

\- memory-isolated safe regression runner and SCS\_MEMORY\_FILE guard

\- Neural Routing V0.1 shadow telemetry with protected pre-change checkpoint

\- Cognitive Budget Manager V0.1 shadow telemetry with protected pre-change checkpoint

\- 13 / 13 safe regression tests, 6 / 6 Neural Routing tests, and 6 / 6 Cognitive Budget tests



Current milestone history:



\- 0521a8f â€” memory-isolated safe test runner

\- bef072e â€” Neural Routing shadow telemetry

\- 10504e5 â€” Cognitive Budget shadow telemetry

\- d56a570 â€” engineering knowledge base and V1 roadmap



Protected milestone checkpoints:



\- checkpoints/neural\_routing\_v0\_1\_pre

\- checkpoints/cognitive\_budget\_v0\_1\_pre



\---



\## 80. Current Immediate Priority



Finish and stabilize the V0.2 baseline while formally documenting the V0.2 â†’ V0.3 shadow boundary.



Order:



1\. synchronize docs/engineering with verified current code and Git history

2\. preserve the completed one-command safe test runner and memory isolation contract

3\. environment reproducibility

4\. provider validation

5\. benchmark repeatability

6\. telemetry

7\. documentation synchronization

8\. stable checkpoint

9\. continue V0.3 experiments only in measured shadow mode



Do not begin V0.4 implementation until the current boundary is reviewed and explicitly approved.



\---



\## 81. Frozen Until V0.2 Is Stable



Do not promote:



\- production Neural Routing

\- adaptive synaptic learning

\- uncontrolled new agent families

\- autonomous production code modification

\- major memory rewrite

\- major dashboard redesign

\- uncontrolled external tool expansion



\---



\# PART XX — SESSION CLOSEOUT



\## 82. Closeout Template



Date:



Objective:



Starting checkpoint:



Files changed:



Commands run:



Tests run:



Results:



Bugs found:



Fixes:



Performance before/after:



New checkpoint/commit:



Known risks:



Next objective:



Time spent:



\---



\# PART XXI — GOLDEN RULES



\## 83. Golden Rules



DARREL is not the LLM.



Selective cognition is fundamental.



Memory must be relevant, not merely available.



Verification must be able to disagree.



Pulse remains the executive gatekeeper.



Providers remain interchangeable.



Internal cognition may be rich while external output stays concise.



Never commit secrets.



Protect memory.



Protect stable checkpoints.



Measure before claiming improvement.



Do not add complexity merely because it sounds intelligent.



If a component does not improve measured behavior, simplify or remove it.



\---



\# 84. Final Engineering Principle



The engineer owns the implementation.



The hypothesis must remain falsifiable.



DARREL succeeds not because many modules ran.



DARREL succeeds when it makes a better decision about:



what cognition to use,

how much to use,

which resources should perform it,

when to verify,

when to stop,

and whether that cognition actually helped.



The long-term goal is a system that learns how to spend intelligence intelligently.

