\# DARREL / SCS Current Build Status



\## Date



9 August 2026



\## Purpose



This file records the current known live implementation state of DARREL / Synthetic Cognitive System (SCS).



It is intentionally separate from the V1 architecture roadmap.



For implementation truth:

\- reproducible live code is authoritative

\- this file is a maintained engineering summary

\- future roadmap documents must not be treated as already implemented



\---



\# 1. Repository



Repository:



jfosterau976/DARREL-SCS



Primary branch:



main



Latest known commit:



8b44ff7dc8a3457f3e2af018d06378bff7298741



Commit message:



DARREL V0.2 add learned relevance regression tests



Local project path:



C:\\Projects\\DARREL\\DARREL-SCS



Current local worktree is not fully clean.



Known modified protected state:



scs\_memory.json



There are also numerous untracked:

\- benchmark files

\- provider experiments

\- checkpoint files

\- backup files

\- historical working copies



Do not clean, reset, delete, stage, or commit these casually.



\---



\# 2. Current Live Execution Path



The operational DARREL request path is:



dashboard/app.py

→ POST /process

→ coordinator.process()

→ pulse.run()

→ activation/routing

→ cognitive orchestration

→ reasoning

→ synthesis when activated

→ verification

→ reflection/learning where activated

→ final response



main.py is currently only a minimal FastAPI status endpoint.



SCS\_START.py reports loaded agents and skills but is not the primary cognitive request path.



The full live cognitive path can write learning to persistent memory.



Do not use the full live cycle for safe regression testing unless memory isolation is confirmed.



\---



\# 3. Selective Pulse Architecture



The current architecture uses the Selective Pulse Engine as the executive activation gate.



Known activation structure:



LOW cognition:

\- left reasoning

\- verifier



MEDIUM cognition:

\- left reasoning

\- right reasoning

\- synthesis

\- verifier



HIGH cognition:

\- goal planning

\- left reasoning

\- right reasoning

\- synthesis

\- verifier

\- reflection

\- learning



The exact live code remains authoritative if this summary becomes stale.



Memory and executive functionality are not yet fully integrated into all selective activation paths.



\---



\# 4. Thinking Policy



Current thinking policy is designed to reduce unnecessary latency and token usage.



LOW:

\- reasoning uses think=False

\- synthesis normally not activated



MEDIUM:

\- left reasoning uses think=False

\- right reasoning uses think=False

\- synthesis may use full/default thinking



HIGH:

\- left reasoning may use full/default thinking

\- right reasoning may use full/default thinking

\- synthesis may use full/default thinking



Corrective revision:

\- uses think=False



The purpose is selective computational depth rather than maximum reasoning on every request.



\---



\# 5. LLM Providers



\## Default Provider



Ollama



Default local model:



qwen3:1.7b



Local Ollama endpoint:



http://127.0.0.1:11434/api/generate



Known behavior:

\- stream disabled

\- temperature approximately 0.4

\- optional thinking mode

\- timing and token metrics

\- local fallback capability



\## Anthropic Provider



Anthropic support is implemented in the current LLM interface.



Provider selection:



SCS\_LLM\_PROVIDER=anthropic



Current default Anthropic model:



claude-sonnet-4-6



Anthropic API:



Messages API



Environment variable:



ANTHROPIC\_API\_KEY



Important:

\- secrets must never be stored in Git

\- secrets must never be printed in logs unnecessarily



Failed Anthropic requests can fall back to Ollama.



Telemetry tracks:

\- requested provider

\- actual provider

\- fallback status

\- timing/token metrics where available



Anthropic authentication has been verified directly against the Anthropic models API.



Live DARREL provider behavior must still be validated carefully through controlled tests.



\---



\# 6. Verification and Corrective Revision



The verifier produces real PASS / REVIEW signals.



Current corrective behavior:



PASS

→ return result



REVIEW

→ perform one corrective revision

→ verify again

→ stop



There is intentionally no unlimited correction loop.



Corrective revision timing is measured separately.



High-risk correction prompts are expected to preserve necessary safety information.



The verifier must remain capable of disagreeing with reasoning outputs.



\---



\# 7. Memory



Persistent memory is protected system state.



Known active/persistent memory files include:



\- scs\_memory.json

\- memory.json

\- message\_memory.json

\- memory/system\_memory.json

\- memory/improvement\_memory.json

\- dashboard memory data



There are also large memory snapshots/backups.



Known current scs\_memory.json is modified relative to HEAD.



Do not stage or overwrite it without explicit review.



Current learned-relevance logic includes regression tests proving:



\- strong but irrelevant learned concepts should not be injected

\- relevant learned concepts may be injected



This is important to the SCS principle that memory must be relevant, not merely available.



\---



\# 8. Automated Tests



The repository contains multiple structured unittest modules.



Current known deterministic isolated test set includes:



tests.test\_anthropic\_provider

tests.test\_provider\_failures

tests.test\_memory\_contract

tests.test\_learned\_relevance



Most recent safe Codex execution:



12 tests passed

0 failed



Approximate unittest duration:



0.121 seconds



Approximate total process time:



1.3 seconds



One non-failing ResourceWarning was observed during mocked HTTP error cleanup.



The run:

\- did not modify repository files

\- did not modify persistent-memory timestamps

\- used bytecode generation disabled

\- used the existing repository virtual environment



There are additional tests including smoke, contracts, telemetry, and integration-oriented tests.



Some of these may execute live cognitive paths and may touch persistent state.



Classify tests before automating them.



\---



\# 9. Python Environment



Repository virtual environment:



C:\\Projects\\DARREL\\DARREL-SCS\\.venv



Interpreter:



C:\\Projects\\DARREL\\DARREL-SCS\\.venv\\Scripts\\python.exe



Python version:



3.14.7



The virtual environment itself is valid.



Codex sandbox policy can block direct process creation with Access is denied.



Narrowly scoped approved execution of the repository virtual-environment interpreter works.



Do not recreate the virtual environment merely because sandbox execution is denied.



No standard python.exe, python3.exe, or py.exe is currently available through PATH inside the inspected Codex process.



This may be configured later as a separate environment task.



\---



\# 10. Current Safe Test Practice



For deterministic regression runs:



\- use the repository .venv interpreter

\- disable bytecode generation

\- use Python -B

\- mock external HTTP/provider calls

\- avoid full live cognitive cycles

\- avoid persistent memory writes

\- record test duration

\- inspect Git status after execution



A dedicated safe test runner is planned:



scripts/test-darrel-safe.ps1



This runner has not yet been confirmed as created at the time of this document.



\---



\# 11. Performance Baselines



Known approximate historical performance:



Simple LOW cognition:

under approximately 1 second in favorable local runs



Example simple math:

approximately 0.65 seconds in a prior smoke run



MEDIUM cognition:

approximately 15 seconds in a representative multi-agent design test after optimization



HIGH cognition:

approximately 35–36 seconds in representative deep/high-risk tests



Corrective revision:

approximately 4 seconds in a representative prior high-risk run



These values are historical engineering baselines, not guaranteed current performance.



Future benchmarking should generate fresh reproducible measurements.



\---



\# 12. Checkpoints and Backups



The repository contains extensive rollback coverage.



Known checkpoint areas include:



checkpoints/core\_backup

checkpoints/dashboard\_backup

checkpoints/SCS\_V01\_SHOWCASE\_BUILD



There are also numerous:



\- BEFORE\_\* files

\- \*\_checkpoint.py files

\- working checkpoint files

\- provider backups

\- memory snapshots



Do not delete these as part of routine cleanup.



Any cleanup must be explicitly reviewed.



\---



\# 13. Known Stable Git History



Important known V0.2 engineering work includes:



\- takeover checkpoint

\- latency instrumentation

\- low cognition optimization

\- selective thinking and LLM metrics

\- complexity-based thinking policy

\- real verifier PASS / REVIEW signals

\- corrective revision loop

\- stronger safety corrective policy

\- separate correction timing

\- smoke regression tests

\- corrective revision regression test

\- contract regression tests

\- provider failure regression tests

\- Anthropic provider support

\- provider telemetry

\- memory contract tests

\- learned relevance regression tests



Current Git history should always be inspected before relying on this list.



\---



\# 14. Stable Checkpoints



Known stable tag:



v0.2-pre-claude



This tag represents an earlier stable checkpoint before Claude provider integration.



There is also an earlier tag:



v0.1-dell-stable



Do not move or delete stable tags casually.



\---



\# 15. Current Engineering Priority



Primary objective:



Finish and stabilize V0.2.



Near-term work should prioritize:



1\. safe reproducible testing

2\. local execution automation

3\. provider reliability

4\. persistent-memory protection

5\. benchmark repeatability

6\. telemetry

7\. clean separation between safe deterministic tests and stateful live tests

8\. documentation synchronization

9\. controlled Git checkpoints



Do not begin production Neural Routing yet.



Do not destabilize the current Selective Pulse architecture while documenting V1.



\---



\# 16. Immediate Next Engineering Task



The immediate automation target is:



scripts/test-darrel-safe.ps1



Purpose:



Provide one safe command to run deterministic isolated regression tests without touching real persistent memory or live external providers.



Expected behavior:



\- use repository .venv

\- disable bytecode generation

\- run approved isolated test modules

\- print PASS / FAIL

\- print elapsed time

\- return non-zero exit code on failure

\- show git status after execution



After this is reliable, similar controlled scripts may be added for:



\- full regression testing

\- benchmarks

\- DARREL startup

\- provider diagnostics

\- release/checkpoint preparation



\---



\# 17. V0.2 / V1 Boundary



V0.2 is the stable engineering baseline.



V1 roadmap concepts include:



\- Cognitive Intake Layer

\- Cognitive Budget Manager

\- Cognitive Compiler

\- temporary cognitive graphs

\- hierarchical memory

\- Cognitive Performance Ledger

\- stopping intelligence

\- adversarial verification

\- Neural Routing / Shadow Brain

\- learned cognitive programs



These are future architecture unless live code proves otherwise.



They must not be described as completed V0.2 features.



\---



\# 18. Engineering Source-of-Truth Rule



When documentation and implementation disagree:



For what currently exists:

live reproducible code wins.



For intended future direction:

docs/engineering roadmap and decision documents guide the work.



For safety:

protected memory, checkpoints, stable Git history, and explicit engineering constraints take priority over convenience.

