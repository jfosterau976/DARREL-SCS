\# DARREL / SCS Current Build Status



\## Date



10 August 2026



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



Implementation checkpoint reviewed for V0.3 closure:



d205dc8



Commit message:



DARREL lock cognitive budget proposal output



Remote synchronization base: 177e500.



The 17 local V0.3 checkpoint commits from 601cd91 through d205dc8 were reviewed as one coherent stabilization sequence. They have not been pushed.



Recent implementation milestones immediately before that documentation commit:



0521a8f â€” DARREL V0.2 add memory-isolated safe test runner



bef072e â€” DARREL V0.2 add neural routing shadow telemetry



10504e5 â€” DARREL V0.3 add cognitive budget shadow telemetry



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

tests.test\_provider\_telemetry

tests.test\_provider\_diagnostics

tests.test\_telemetry\_contract

tests.test\_memory\_contract

tests.test\_learned\_relevance

tests.test\_benchmark\_result\_contract



Current controlled V0.3 closure verification:



\- Safe deterministic suite: 37 / 37 passed

\- Neural Routing shadow suite: 11 / 11 passed

\- Cognitive Budget shadow suite: 20 / 20 passed

\- Combined safe + shadow suite: 68 / 68 passed

\- Combined unittest time: 0.040 seconds

\- Combined runner elapsed: 0.303 seconds



The provider-failure matrix now verifies connection, HTTP, timeout, malformed-response, empty-response, missing-metrics, primary-to-fallback failure, provider identity, and unexpected-error behavior with mocked providers only.



Provider telemetry now defensively copies and normalizes malformed metric mappings, numeric counters, fallback flags, and provider identities after provider execution. Each call reports additive data-quality metadata identifying normalized fields. This is observational reliability only and does not change provider selection, requests, fallback policy, or responses.



Neural Routing comparison telemetry now normalizes malformed nested observation data, reports the affected fields through additive data-quality metadata, and is contract-locked by Pulse before publication. Even malformed comparison output is reasserted as mode=shadow and authority=false after authoritative execution.



Cognitive Budget proposal and comparison telemetry now normalize malformed top-level records, invalid state categories, and negative, boolean, non-finite, or out-of-range numeric signals. Additive data-quality metadata reports affected fields and proposal warnings survive comparison enrichment. Pulse reasserts mode=shadow, authority=false, and enforced=false on proposal output before execution planning while passing the authoritative Attention Router activation through unchanged. Malformed downstream Pulse/budget telemetry produces an observation error after authoritative execution instead of breaking coordinator completion. Every observed mapping reasserts the same locked contract before and after comparison.



Benchmark validation now supports deterministic file/directory discovery, optional filename patterns, human or JSON summaries, finite numeric checks, and explicit exit codes without mutating source artifacts. The 20 timestamped historical artifacts pass; the two legacy aggregate files remain intentionally reported as incompatible with the current record contract.



The safe runner now classifies safe, shadow, and combined suites while retaining temporary-memory isolation and bytecode suppression. It fingerprints protected memory by hash, length, and timestamp before and after each run, returns exit code 3 if the fingerprint changes or cannot be verified, and preserves the real unittest exit code when output is redirected.



Previous recorded safe Codex execution:



13 tests passed

0 failed



Approximate unittest duration:



0.032 seconds



Approximate safe-runner elapsed time:



0.448 seconds



The thirteenth test protects the SCS\_MEMORY\_FILE isolation contract.



Previous recorded isolated shadow-layer verification:



\- Neural Routing V0.1: 6 passed

\- Cognitive Budget Manager V0.1: 6 passed



The Cognitive Budget unittest suite itself ran in approximately 0.006 seconds within an approximately 0.408-second isolated command.



Previous documentation-audit verification:



\- Safe regressions: 13 / 13 passed

  \- unittest time: 0.057 seconds

  \- runner elapsed: 1.053 seconds

\- Neural Routing shadow tests: 6 / 6 passed

  \- time: 0.021 seconds

\- Cognitive Budget shadow tests: 6 / 6 passed

  \- time: 0.005 seconds



These are deterministic isolated results, not live-provider or full stateful-pipeline results.



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



A dedicated safe test runner is implemented and committed:



scripts/test-darrel-safe.ps1



The runner uses Python -B, sets PYTHONDONTWRITEBYTECODE=1, redirects SCS\_MEMORY\_FILE to temporary memory, restores the previous environment, verifies the protected-memory fingerprint, reports PASS / FAIL and elapsed time, and shows git status. It does not repair or rewrite persistent memory if verification fails.



The CognitiveMemory constructor supports an explicit memory file or SCS\_MEMORY\_FILE. When neither is supplied, its existing persistent-memory behavior remains unchanged.



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

\- memory-isolated safe regression runner

\- persistent-memory path override contract

\- Neural Routing V0.1 shadow telemetry

\- Cognitive Budget Manager V0.1 shadow telemetry



Current Git history should always be inspected before relying on this list.



\---



\# 14. Stable Checkpoints



Known stable tag:



v0.2-pre-claude



This tag represents an earlier stable checkpoint before Claude provider integration.



There is also an earlier tag:



v0.1-dell-stable



Do not move or delete stable tags casually.



Protected milestone checkpoints also include:



checkpoints/neural\_routing\_v0\_1\_pre



checkpoints/cognitive\_budget\_v0\_1\_pre



\---



\# 15. Historical Engineering Priority and Current Closure Status



Historical pre-closure objective:



Finish and stabilize the V0.2 baseline while formally maintaining the V0.2 â†’ V0.3 boundary.



Near-term work should prioritize:



1\. documentation synchronization with live code and Git history

2\. continued safe reproducible testing and local execution automation

3\. provider reliability

4\. persistent-memory protection

5\. benchmark repeatability

6\. telemetry

7\. clean separation between safe deterministic tests and stateful live tests

8\. documentation synchronization

9\. controlled Git checkpoints



The safe runner, persistent-memory isolation guard, Neural Routing shadow telemetry, and Cognitive Budget shadow telemetry are already implemented.



Neural Routing and Cognitive Budget are V0.3 shadow / experimental features. They do not control production routing, module activation, execution, stopping, or budget enforcement.



Do not promote Neural Routing or Cognitive Budget to production authority.



Do not destabilize the current Selective Pulse architecture while documenting V1.



Current closure status:



V0.3 stabilization is complete locally after controlled closure review. The next action is human review of the local checkpoint sequence and an explicit decision about the next engineering phase. Additional V0.3 work requires evidence of a genuine defect, and V0.4 requires separate explicit approval.



\---



\# 16. Stabilization Closure



Historical pre-closure engineering target:



Continue V0.3 stabilization one regression-led, deterministic objective at a time while keeping V0.4 and production authority changes out of scope.



The previously listed automation target is complete:



scripts/test-darrel-safe.ps1



The V0.2 to V0.3 boundary synchronization is committed at 177e500. Seventeen reviewed local V0.3 checkpoint commits run from 601cd91 through d205dc8. They are coherent, remain local, and have not been pushed.



Additional verified engineering support now present in the committed baseline:



\- scripts/preflight-darrel.ps1 for read-only reproducibility checks

\- scripts/provider\_diagnostics.py for configuration-only, credential-redacted provider diagnostics

\- benchmarks/result\_contract.py for deterministic benchmark validation and structured capture

\- defensive telemetry snapshots and explicit shadow-contract reassertion



V0.4 Cognitive Compiler implementation has not started.



Current engineering target:



Preserve the locally closed V0.3 state and stop at the V0.4 boundary. Do not resume speculative stabilization work.



Verified behavior:



\- use repository .venv

\- disable bytecode generation

\- run approved isolated test modules

\- print PASS / FAIL

\- print elapsed time

\- return non-zero exit code on failure

\- show git status after execution



Similar controlled scripts may be considered later for:



\- controlled live/stateful regression testing

\- integration of structured capture into a separately approved benchmark execution workflow

\- DARREL startup

\- live provider connectivity diagnostics when separately approved

\- release/checkpoint preparation



\---



\# 17. V0.2 / V1 Boundary



V0.2 is the stable engineering baseline.



IMPLEMENTED NOW:



\- Selective Pulse production execution path

\- provider abstraction and fallback telemetry

\- verifier PASS / REVIEW with one corrective revision

\- memory relevance protection

\- memory-isolated safe regression runner



V0.3 SHADOW / EXPERIMENTAL:



\- Neural Routing V0.1 predicts complexity, risk, and modules from 16 signals

\- Cognitive Budget Manager V0.1 proposes and compares diagnostic budgets



Both report authority=false. Cognitive Budget also reports enforced=false.



The Attention Router remains authoritative. The Selective Pulse Engine remains the final execution gatekeeper.



FUTURE V0.4+ / V1:



\- Cognitive Intake Layer

\- Cognitive Compiler

\- temporary cognitive graphs

\- hierarchical memory

\- Cognitive Performance Ledger

\- stopping intelligence

\- adversarial verification

\- production or learned Neural Routing authority

\- production Cognitive Budget enforcement

\- learned cognitive programs



These are future architecture unless live code proves otherwise.



They must not be described as completed V0.2 features.



The current shadow implementations must not be described as production V0.3 authority.



\---



\# 18. Engineering Source-of-Truth Rule



When documentation and implementation disagree:



For what currently exists:

live reproducible code wins.



For intended future direction:

docs/engineering roadmap and decision documents guide the work.



For safety:

protected memory, checkpoints, stable Git history, and explicit engineering constraints take priority over convenience.

