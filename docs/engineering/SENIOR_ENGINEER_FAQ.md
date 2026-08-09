\# DARREL / SCS

\# Senior Engineer FAQ \& Decision Bridge



\## Purpose



This file answers the most important engineering questions a new senior engineer or Codex instance is likely to ask before changing DARREL.



It combines:

\- verified takeover knowledge

\- known technical debt

\- locked engineering decisions

\- current V0.2 status

\- future architecture boundaries



Status meanings:



VERIFIED

= directly supported by live code, tests, runtime evidence, Git history, or current Codex inspection.



RECONSTRUCTED

= strongly supported by project history but should still be checked against the current repository.



DESIGN DECISION

= intended architecture or engineering rule, not necessarily current implementation.



FUTURE DIRECTION

= approved future work that must not be mistaken for a completed feature.



\---



\# 1. What is the single most important thing to understand about DARREL?



Status: DESIGN DECISION



Do not confuse architectural richness with architectural value.



DARREL can easily become a slower and more expensive wrapper around ordinary LLM calls if extra cognition is activated without measurable benefit.



Preserve the Selective Pulse hypothesis.



Require every:

\- module

\- model call

\- memory mechanism

\- synthesis step

\- verifier step

\- future neural-routing feature



to earn its complexity through evidence.



\---



\# 2. What is DARREL?



Status: DESIGN DECISION



DARREL, nickname Dazza, is the public-facing assistant.



The underlying system is the Synthetic Cognitive System (SCS).



DARREL is not one LLM.



LLMs are interchangeable reasoning engines/resources inside DARREL.



\---



\# 3. What is the central SCS hypothesis?



Status: DESIGN DECISION



The system should estimate what cognition is required and activate the minimum useful resources.



Long-term direction:



INPUT

→ estimate cognition

→ allocate resources

→ compile a cognitive program

→ execute selected cognition

→ evaluate

→ decide whether more cognition is worthwhile

→ produce output

→ learn from the outcome



The goal is selective cognition, not maximum cognition.



\---



\# 4. What exact project folder is currently authoritative?



Status: VERIFIED



Current project:



C:\\Projects\\DARREL\\DARREL-SCS



Older development tree:



C:\\Users\\justi\\synthetic-cognitive-system



The older tree must remain preserved until deliberately audited.



\---



\# 5. What repository is authoritative?



Status: VERIFIED



GitHub repository:



jfosterau976/DARREL-SCS



Primary branch:



main



Live reproducible code and current Git state override historical documentation when implementation details disagree.



\---



\# 6. What is the current known live execution chain?



Status: VERIFIED



Current operational path:



dashboard/app.py

→ POST /process

→ coordinator.process()

→ pulse.run()

→ routing / activation

→ orchestration

→ cognitive modules

→ verification / learning where selected

→ final response



Historical runtime evidence also identified:



core/pulse\_orchestrator\_V3.py

core/module\_registry\_setup.py



Exact downstream calls must always be checked from the current code.



\---



\# 7. Which files are definitely live?



Status: RECONSTRUCTED / VERIFIED IN PART



Files strongly supported by current architecture and observed execution include:



core/coordinator.py

core/pulse.py

core/llm\_interface.py

core/left\_brain.py

core/right\_brain.py

core/synthesis\_agent.py

core/verifier\_engine.py

core/reflection\_agent.py

core/learning\_extractor.py

core/learning\_feedback.py

core/memory\_consolidator.py

core/goal\_planning\_engine.py

core/module\_registry\_setup.py



Never infer authority from filenames alone.



Follow actual imports and callers.



\---



\# 8. Which files may look important but be experimental or obsolete?



Status: RECONSTRUCTED



Historical examples include:



\- attention\_router

\- tree\_router

\- cognitive\_controller

\- adaptive effort controllers

\- older pulse implementations

\- old agent implementations

\- checkpoint copies

\- BEFORE\_\* files

\- working backups



Do not delete these merely because they appear redundant.



\---



\# 9. Should checkpoint and backup files be deleted?



Status: DESIGN DECISION



No.



Not during routine engineering.



Historical backups have previously rescued working implementations.



Rule:



preserve

→ understand

→ archive deliberately

→ delete much later, if ever



\---



\# 10. What is the ugliest technical debt?



Status: VERIFIED HISTORICALLY



Implicit dictionary contracts between modules.



Several parts of DARREL expect particular:



\- keys

\- nesting

\- status values

\- confidence values

\- result structures



A valid module response has previously been misinterpreted because another component expected a different structure.



These contracts should remain protected by regression tests before major refactoring.



\---



\# 11. What fragile interfaces deserve special protection?



Status: DESIGN DECISION



High-risk interfaces include:



\- coordinator → pulse

\- pulse → orchestration

\- router → activation plan

\- reasoning modules → synthesis

\- synthesis → verifier

\- verifier → corrective revision

\- provider layer → modules

\- memory retrieval → reasoning

\- learning → persistent state

\- dashboard backend → browser frontend



Do not change these interfaces casually.



\---



\# 12. What is the Selective Pulse Engine?



Status: DESIGN DECISION / CURRENT CORE



It is the executive activation gatekeeper.



DARREL should not activate every cognitive module for every request.



The Pulse Engine decides which cognition actually runs.



Future routers may recommend activation.



They do not bypass Pulse.



\---



\# 13. Can Neural Routing replace the Pulse Engine?



Status: DESIGN DECISION



No.



Neural Routing may recommend routes.



The Selective Pulse Engine remains final execution authority.



\---



\# 14. Is Neural Routing currently production-ready?



Status: VERIFIED FUTURE BOUNDARY



No.



Neural Routing V0.1 shadow telemetry is implemented, but production Neural Routing authority remains frozen until evidence and explicit approval justify promotion.



The current implementation operates in shadow mode.



\---



\# 15. What does Neural Routing shadow mode mean?



Status: DESIGN DECISION



The current router controls the real run.



The Neural Routing V0.1 layer receives the same request and predicts complexity, risk, and module candidates from 16 deterministic normalized signals.



Its decision is logged and compared.



It does not alter production execution.



\---



\# 16. How many initial cognitive neurons are planned?



Status: DESIGN DECISION



Neural Routing V0.1 currently implements 16 deterministic normalized cognitive signals with static versioned weights.



Possible signals include:



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

\- mathematical reasoning

\- provider capability

\- latency budget

\- cost sensitivity

\- privacy sensitivity

\- disagreement

\- confidence

\- escalation need



Production thresholds, adaptive learning, provider routing, and broader signal design remain deliberately unlocked for future experiments.



\---



\# 17. Are activation functions and learning rates already decided?



Status: DESIGN DECISION



No.



Do not invent or freeze:



\- activation functions

\- thresholds

\- learning rates

\- reward functions

\- weight update rules



before controlled experimentation.



\---



\# 18. What is the most important current architectural risk?



Status: DESIGN DECISION



Complexity without measurable benefit.



Every major architectural component should be benchmarked against simpler alternatives.



\---



\# 19. What must DARREL be compared against?



Status: DESIGN DECISION



Required baselines include:



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

DARREL without verification



Later:



rule router

vs

neural router



\---



\# 20. What should benchmarking measure?



Status: DESIGN DECISION



At minimum:



\- correctness

\- relevance

\- usefulness

\- reasoning quality

\- creativity where relevant

\- unsupported claims

\- hallucinations

\- latency

\- tokens

\- provider cost

\- activated modules

\- verifier result

\- memory usefulness

\- corrective behavior



\---



\# 21. Does DARREL need to outperform a direct LLM on every task?



Status: DESIGN DECISION



No.



That would be the wrong success criterion.



DARREL should learn when extra cognition is worth using and when it is not.



For some simple tasks, the correct SCS behavior may be to behave almost like a direct model or deterministic tool.



For complex tasks, additional cognition may justify its cost.



\---



\# 22. What is the most important future capability?



Status: DESIGN DECISION



Learning how to allocate cognition intelligently.



DARREL should eventually learn patterns such as:



\- this task needs analysis but not creativity

\- this task benefits from two independent perspectives

\- this task needs memory

\- this task requires fresh research

\- this task needs stronger verification

\- this task is cheap enough for local inference

\- this task justifies a stronger cloud model



\---



\# 23. What is the Cognitive Intake Layer?



Status: FUTURE DIRECTION



A future authoritative front-end reasoning layer that estimates what cognitive resources a request requires before expensive processing begins.



Neural Routing V0.1 currently provides a limited shadow signal prototype, not a production Cognitive Intake authority.



\---



\# 24. What is the Cognitive Budget Manager?



Status: V0.3 SHADOW / EXPERIMENTAL; PRODUCTION AUTHORITY FUTURE



Cognitive Budget Manager V0.1 is implemented in shadow mode. It proposes diagnostic budget tiers and compares them with observed usage.



It has authority=false and enforced=false, so production budget control remains future work.



Potential budgets include:



\- latency

\- tokens

\- provider calls

\- cost

\- local compute

\- module count

\- memory depth

\- verifier depth

\- research depth

\- reasoning passes



\---



\# 25. What is the Cognitive Compiler?



Status: FUTURE DIRECTION



A major future V0.4/V1 concept.



It is not implemented and V0.4 has not started.



Instead of always using one fixed pipeline, DARREL should compile a temporary task-specific cognitive execution graph.



Example:



simple calculation

→ calculator

→ lightweight verification



complex planning

→ planner

→ independent reasoning

→ challenge

→ synthesis

→ verification



\---



\# 26. Why is the Cognitive Compiler important?



Status: DESIGN DECISION



It turns selective cognition from simple module switching into dynamic task-specific cognitive programming.



This may become one of DARREL's signature architectural ideas.



\---



\# 27. What is the Shared Cognitive Workspace?



Status: FUTURE DIRECTION



A structured space where active cognitive modules exchange compact typed state.



Potential contents include:



\- claims

\- confidence

\- uncertainty

\- evidence

\- risks

\- objections

\- memory references

\- verifier feedback

\- budget

\- execution state



The aim is to avoid repeatedly sending full reports between agents.



\---



\# 28. Why was the Neural-Linked Dual Brain direction proposed?



Status: FUTURE DIRECTION



Benchmarking showed that sequential LLM inference is a major latency source.



A future architecture can reduce this by:



\- running independent Left/Right cognition in parallel

\- sharing compact state

\- skipping synthesis when agreement is high

\- using cheap verification signals before invoking a full verifier

\- adapting cognitive effort to provider capability



\---



\# 29. Should Left Brain and Right Brain be treated as literal brain hemispheres?



Status: DESIGN DECISION



No.



They are metaphors for different cognitive perspectives.



If a different structure performs better, use it.



Possible future perspectives include:



\- analyst

\- creator

\- skeptic

\- planner

\- evidence specialist

\- safety specialist



\---



\# 30. Can independent cognition run in parallel?



Status: APPROVED DIRECTION



Yes, when dependencies allow.



This should be benchmarked carefully because parallelism can reduce wall-clock time without necessarily reducing total compute.



\---



\# 31. What is the future agreement/conflict gate?



Status: FUTURE DIRECTION



A lightweight mechanism that evaluates whether independent cognitive outputs:



\- agree strongly

\- disagree materially

\- remain uncertain



High agreement may allow deterministic merging.



Significant disagreement may justify synthesis.



\---



\# 32. Should synthesis always run?



Status: DESIGN DECISION



No.



Synthesis must earn its cost.



If two outputs already agree strongly, a separate synthesis model call may be unnecessary.



\---



\# 33. Should the full verifier always run?



Status: DESIGN DECISION



No.



Future architecture may use lightweight checks first.



Full verification should be reserved for cases where risk, uncertainty, disagreement, or evidence needs justify it.



\---



\# 34. Must the verifier be able to disagree?



Status: LOCKED DESIGN DECISION



Yes.



If it always approves the reasoning path, it is not a verifier.



\---



\# 35. What is the current correction policy?



Status: VERIFIED CURRENT V0.2



Current pattern:



initial response

→ verifier

→ if REVIEW, one corrective revision

→ reverify

→ stop



Unlimited recursive correction is intentionally avoided.



\---



\# 36. What is provider-aware cognition?



Status: FUTURE DIRECTION / PARTIAL CURRENT FOUNDATION



Provider selection should eventually depend on cognitive needs and provider capabilities.



Potential considerations:



\- task difficulty

\- quality

\- latency

\- cost

\- privacy

\- offline operation

\- reliability

\- historical success



Current provider abstraction lays the foundation.



\---



\# 37. Which providers are currently supported?



Status: VERIFIED



Current known providers:



\- Ollama / qwen3:1.7b

\- Anthropic / Claude



Current Anthropic default:



claude-sonnet-4-6



Exact current provider behavior should still be checked through controlled tests.



\---



\# 38. What happens if Anthropic fails?



Status: VERIFIED CURRENT DESIGN



DARREL can fall back to Ollama.



Telemetry must make clear:



\- requested provider

\- actual provider

\- fallback state

\- failure reason where relevant



Fallbacks must never be hidden.



\---



\# 39. Are secrets allowed in Git?



Status: LOCKED SECURITY RULE



No.



Never commit:



\- API keys

\- passwords

\- access tokens

\- recovery codes

\- credentials



If one is committed accidentally, treat it as compromised and rotate/revoke it.



\---



\# 40. What is the memory rule?



Status: LOCKED DESIGN DECISION



Memory must be relevant, not merely available.



High-strength unrelated memory must not hijack new tasks.



\---



\# 41. Has memory contamination happened before?



Status: VERIFIED



Yes.



Benchmarking exposed learned-memory contamination where strong historical SCS concepts appeared in unrelated prompts.



A relevance gate was added.



Regression tests now protect relevant versus irrelevant learned-memory injection.



\---



\# 42. Should persistent memory be used during safe regression tests?



Status: DESIGN DECISION



No, unless fully isolated.



Safe deterministic tests should use mocks or temporary state.



\---



\# 43. What future memory architecture is approved?



Status: FUTURE DIRECTION



Hierarchical memory.



Potential layers:



\- working

\- episodic

\- semantic

\- procedural

\- user

\- project

\- hypothesis



\---



\# 44. What is memory economics?



Status: FUTURE DIRECTION



Memories may eventually be evaluated using metadata such as:



\- relevance

\- confidence

\- source quality

\- age

\- usefulness

\- contradiction

\- reinforcement

\- decay

\- risk



This is intended to stop memory accumulation from becoming cognitive pollution.



\---



\# 45. What is stopping intelligence?



Status: FUTURE DIRECTION



DARREL should eventually decide whether another cognitive step is worth its cost.



Possible stop signals:



\- confidence high

\- agreement high

\- uncertainty low

\- evidence saturated

\- little expected improvement

\- budget exhausted



Possible continue signals:



\- contradiction

\- uncertainty

\- verifier REVIEW

\- missing evidence

\- safety risk

\- major disagreement



\---



\# 46. What is the Cognitive Performance Ledger?



Status: FUTURE DIRECTION



A structured record of how DARREL thought and whether that route helped.



Potential fields:



\- task type

\- signals

\- modules

\- provider

\- memory

\- tools

\- latency

\- tokens

\- cost

\- verifier result

\- revision

\- outcome

\- lessons



This becomes evidence for future routing learning.



\---



\# 47. What is cognitive economy?



Status: FUTURE DIRECTION



Each cognitive resource should eventually have estimated cost and historical benefit.



DARREL should optimize expected value rather than raw compute.



\---



\# 48. Can DARREL self-experiment?



Status: APPROVED WITH CONSTRAINTS



Eventually, yes.



Controlled experiments may compare:



\- route A vs route B

\- synthesis vs no synthesis

\- memory vs no memory

\- provider A vs provider B

\- shallow vs deep verifier

\- rule router vs neural router



But self-experimentation is not permission for unrestricted autonomous production self-modification.



\---



\# 49. Can DARREL autonomously rewrite its own architecture?



Status: FROZEN / NOT APPROVED



No.



Autonomous production code modification is intentionally frozen during current development.



\---



\# 50. What is the Shadow Brain?



Status: V0.3 SHADOW / EXPERIMENTAL; BROADER LEARNED AUTHORITY FUTURE



Neural Routing V0.1 in observation-only mode, with broader learned routing remaining future work.



It predicts:



\- route

\- cognitive complexity

\- provider

\- budget

\- verifier depth

\- memory depth



without controlling production.



\---



\# 51. What is the Executive Resolution layer?



Status: FUTURE DIRECTION



The final layer should resolve internal disagreement and compress rich internal cognition into useful user-facing output.



DARREL should be rich internally and simple externally.



\---



\# 52. Should internal chain-of-thought be exposed?



Status: DESIGN DECISION



No.



The architecture should expose useful conclusions, uncertainty, evidence, and diagnostics where appropriate, not raw private model reasoning.



\---



\# 53. What are learned cognitive programs?



Status: LONG-TERM DIRECTION



DARREL may eventually learn reusable strategies, not just routing weights.



Example:



high-risk comparison

→ research

→ opposing perspectives

→ synthesis

→ evidence verification



These may become procedural memory.



\---



\# 54. What is the current V0.2 priority?



Status: VERIFIED CURRENT PRIORITY



Finish and stabilize V0.2 before promoting major V0.3/V1 architecture.



Current near-term priority:



1\. synchronize docs/engineering with verified live code and Git history

2\. preserve the completed one-command test runner and memory isolation contract

3\. environment reproducibility

4\. provider validation

5\. benchmark repeatability

6\. telemetry

7\. documentation synchronization

8\. stable checkpoint



Neural Routing V0.1 and Cognitive Budget Manager V0.1 exist only as V0.3 shadow / experimental telemetry. Do not begin V0.4.



\---



\# 55. What features are frozen until V0.2 is stable?



Status: DESIGN DECISION



Do not promote:



\- production Neural Routing

\- adaptive synaptic learning

\- large new agent families

\- autonomous code modification

\- major memory rewrite

\- major dashboard redesign

\- uncontrolled external-tool expansion

\- premature deployment/scaling



\---



\# 56. What is the current test situation?



Status: VERIFIED



Codex successfully ran the approved deterministic isolated set:



30 passed

0 failed



Modules included:



tests.test\_anthropic\_provider

tests.test\_provider\_failures

tests.test\_provider\_telemetry

tests.test\_provider\_diagnostics

tests.test\_telemetry\_contract

tests.test\_memory\_contract

tests.test\_learned\_relevance

tests.test\_benchmark\_result\_contract



Persistent memory and Git state were unchanged.



Additional isolated shadow-layer verification:



\- Neural Routing V0.1: 7 / 7 passed

\- Cognitive Budget Manager V0.1: 8 / 8 passed



Combined safe and shadow verification: 45 / 45 passed. The safe runner supports safe, shadow, and all classifications.



The provider-failure module now has nine behavior-based tests covering explicit failure classification, missing fields/metrics, and primary-to-fallback identity preservation.



\---



\# 57. Why didn't Codex initially run Python?



Status: VERIFIED



The repository virtual environment was valid.



Codex's managed sandbox blocked process creation.



Narrowly scoped approved execution of:



C:\\Projects\\DARREL\\DARREL-SCS\\.venv\\Scripts\\python.exe



worked correctly.



Do not recreate the virtual environment because of this sandbox behavior.



\---



\# 58. What Python environment should be used?



Status: VERIFIED



Repository interpreter:



C:\\Projects\\DARREL\\DARREL-SCS\\.venv\\Scripts\\python.exe



Known version:



Python 3.14.7



\---



\# 59. What is the next automation target?



Status: CURRENT PRIORITY



Implemented and committed:



scripts/test-darrel-safe.ps1



Purpose:



The safe runner provides one-command deterministic regression testing with temporary protected memory and no unnecessary external calls.



The V0.2 to V0.3 boundary is committed at 177e500. The initial V0.3 stabilization milestones are protected by commits 601cd91, 611a773, 6dbcbd1, and c3974a6. Current work continues through small regression-led V0.3 objectives; V0.4 remains out of scope.



\---



\# 60. What should automation focus on first?



Status: DESIGN DECISION



Automate repetitive engineering work.



Good targets:



\- safe tests

\- startup

\- benchmarks

\- provider diagnostics

\- telemetry capture



The committed V0.3 support baseline includes a read-only preflight, configuration-only credential-redacted provider diagnostics, deterministic benchmark result/capture validation, and defensive telemetry snapshots. Live provider checks and integration of capture into benchmark execution remain separately controlled work.

\- release checks

\- GitHub Actions for mocked tests



Do not automate uncontrolled self-modification.



\---



\# 61. Why is DARREL currently slower than a direct model?



Status: VERIFIED ENGINEERING FINDING



Sequential LLM inference dominates latency.



A medium path may involve multiple independent and sequential model calls.



High-leverage future optimization comes from:



\- reducing unnecessary calls

\- shortening handoffs

\- parallelizing independent calls

\- skipping synthesis when unnecessary

\- using cheap verification gates

\- escalating only when extra cognition is useful



\---



\# 62. What controlled performance sequence should be used?



Status: APPROVED PLAN



Phase 0:

benchmark correctness



Phase 1:

parallel Left + Right where both are already selected



Phase 2:

Shared Cognitive Workspace



Phase 3:

agreement/conflict gate



Phase 4:

cheap verification gate



Phase 5:

provider capability-aware cognition



Phase 6:

Neural Routing shadow mode



Current state note:



Neural Routing V0.1 shadow telemetry and Cognitive Budget Manager V0.1 shadow telemetry were introduced before the broader performance sequence was completed. This does not grant either layer production authority or approve later phases.



Phase 7:

rebenchmark and ablation



Phase 8:

adaptive synapses only after a valid reward/credit model exists



\---



\# 63. Should multiple architectural changes be made at once?



Status: LOCKED ENGINEERING RULE



No.



Change one important variable at a time.



Then:



checkpoint

→ change

→ test

→ measure

→ compare

→ keep/revert



\---



\# 64. What should happen after each engineering session?



Status: DESIGN DECISION



Record:



\- date

\- objective

\- starting state

\- files changed

\- commands

\- tests

\- results

\- bugs

\- fixes

\- performance before/after

\- checkpoint

\- next objective

\- time spent where known



\---



\# 65. What should the operator be told after each session?



Status: DESIGN DECISION



Keep it simple:



\- what changed

\- what now works

\- what still does not

\- whether the build is safely saved

\- what happens next



The operator should not have to wonder whether closing the laptop loses the work.



\---



\# 66. What is the role of ChatGPT?



Status: WORKFLOW DECISION



ChatGPT acts as lead architect / engineering coordinator.



Responsibilities:



\- preserve architectural intent

\- decide engineering sequence

\- review evidence

\- prevent architecture drift

\- coordinate Codex/GitHub work

\- maintain engineering knowledge



\---



\# 67. What is the role of Codex?



Status: WORKFLOW DECISION



Codex is the local execution and repository engineering environment.



It can:



\- inspect files

\- trace architecture

\- edit local code

\- run tests

\- diagnose the environment

\- automate repetitive engineering tasks



It must follow AGENTS.md and repository safety rules.



\---



\# 68. What is GitHub's role?



Status: WORKFLOW DECISION



GitHub is the versioned shared engineering history.



Code, architecture docs, tests, decisions, and checkpoints should be recoverable there where appropriate.



Secrets must never be committed.



\---



\# 69. Where should engineering documentation live?



Status: CURRENT DECISION



Repository-native documentation:



docs/engineering/



Key files:



CURRENT\_BUILD\_STATUS.md

MASTER\_ENGINEERING\_HANDOVER.md

COMPLETE\_ENGINEER\_HANDBOOK.md

SENIOR\_ENGINEER\_FAQ.md

V1\_ARCHITECTURE\_ROADMAP.md

ENGINEERING\_DECISIONS.md



Root instructions:



AGENTS.md



\---



\# 70. What happens when documentation disagrees with code?



Status: LOCKED RULE



For current implementation:



live reproducible code wins.



For intended future direction:



engineering roadmap and decision docs guide work.



Document the discrepancy.



Do not silently rewrite history.



\---



\# 71. What is the core scientific question?



Status: DESIGN DECISION



Does DARREL's selective cognitive architecture produce enough measurable benefit to justify its extra computation and complexity?



Possible benefit dimensions:



\- correctness

\- reliability

\- reasoning

\- creativity

\- verification

\- memory

\- adaptability

\- cost

\- latency

\- resource selection



The answer may vary by task class.



That is acceptable.



\---



\# 72. What does success look like?



Status: DESIGN DECISION



Success is not:



"many agents ran."



Success is:



DARREL made a better decision about what cognition to use.



Eventually it should learn that decision from experience.



\---



\# 73. What is the V1 signature idea?



Status: LOCKED VISION



Estimate cognition

→ allocate resources

→ compile a temporary cognitive program

→ execute

→ measure whether it helped

→ learn how to allocate cognition better next time



DARREL should evolve toward a learned operating system for intelligence.



\---



\# 74. What should an incoming engineer challenge?



Status: DESIGN DECISION



Everything except the need for evidence.



Existing mechanisms are not sacred.



If a simpler architecture delivers:



\- fewer calls

\- lower latency

\- lower cost

\- equal or better quality



prefer it.



Preserve the hypothesis, not unnecessary complexity.



\---



\# 75. Golden Rule



Never add complexity because it sounds intelligent.



Add it only when DARREL becomes measurably better because of it.



\---



\# 76. What is the current implementation boundary?



Status: VERIFIED CURRENT BOUNDARY



IMPLEMENTED NOW:



\- V0.2 Selective Pulse baseline, provider behavior, verification, memory relevance, safe runner, and memory isolation



V0.3 SHADOW / EXPERIMENTAL:



\- Neural Routing V0.1 telemetry

\- Cognitive Budget Manager V0.1 telemetry



FUTURE:



\- V0.4 Cognitive Compiler and temporary execution graphs

\- production Neural Routing authority

\- production budget enforcement and the remaining V1 architecture



Current milestone commits:



\- 0521a8f â€” safe runner and memory isolation

\- bef072e â€” Neural Routing shadow telemetry

\- 10504e5 â€” Cognitive Budget shadow telemetry

\- d56a570 â€” engineering knowledge base



Protected milestone checkpoints:



\- checkpoints/neural\_routing\_v0\_1\_pre

\- checkpoints/cognitive\_budget\_v0\_1\_pre



The current Attention Router remains authoritative and the Selective Pulse Engine remains the final execution gatekeeper.

