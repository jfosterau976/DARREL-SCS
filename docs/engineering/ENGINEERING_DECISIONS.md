\# DARREL / SCS Engineering Decisions



\## Purpose



This file records engineering decisions that should guide implementation.



It is not a list of every idea discussed.



A decision here means:

\- the direction is intentionally chosen

\- future engineers should not casually reverse it

\- changes should require evidence, testing, or an explicit new decision



Live reproducible code remains authoritative for what currently exists.



\---



\# 1. Project Identity



Decision:



The public-facing assistant is DARREL.



Nickname:



Dazza.



The underlying system is the Synthetic Cognitive System (SCS).



DARREL is not a single LLM.



LLMs are interchangeable reasoning resources inside SCS.



Status:



LOCKED



\---



\# 2. Core SCS Principle



Decision:



DARREL should selectively allocate cognition rather than activate maximum reasoning for every task.



The system should eventually learn:



\- what cognition is required

\- how much cognition is worth spending

\- which resources should perform it

\- whether additional cognition is useful

\- when to stop



Status:



LOCKED



\---



\# 3. Selective Pulse Engine Authority



Decision:



The Selective Pulse Engine remains the final executive activation gatekeeper.



Routing systems may recommend activation.



They do not bypass the Pulse Engine.



This applies to:



\- current rule routing

\- future cognitive signal routing

\- neural routing

\- learned routing

\- provider selection

\- module activation



Status:



LOCKED



\---



\# 4. Provider Independence



Decision:



DARREL must not become permanently coupled to one LLM provider.



Providers are interchangeable cognitive resources.



Provider choice may depend on:



\- task type

\- cost

\- latency

\- quality

\- privacy

\- offline availability

\- historical performance

\- specialization



Status:



LOCKED



\---



\# 5. Memory Relevance



Decision:



Memory must be relevant, not merely available.



Strong historical memory must not be injected into unrelated tasks.



Memory retrieval and reinforcement should be relevance-driven.



Status:



LOCKED



Evidence:



Current learned relevance regression tests already protect this behavior.



\---



\# 6. Verifier Independence



Decision:



The verifier must be able to disagree with reasoning and synthesis outputs.



The verifier must not behave as a rubber stamp.



PASS and REVIEW must represent meaningful independent evaluation.



Status:



LOCKED



\---



\# 7. Corrective Revision Limit



Decision:



A verifier REVIEW may trigger corrective revision.



Current policy should avoid unlimited recursive correction.



Current expected structure:



initial answer

→ verify

→ if REVIEW, one corrective revision

→ reverify

→ stop



Status:



LOCKED FOR V0.2



Future versions may revise this only with measured evidence.



\---



\# 8. One Objective Per Engineering Change



Decision:



Engineering work should focus on one controlled objective at a time.



Before major architectural changes:



\- protect stable state

\- make the smallest useful change

\- test it

\- measure it

\- keep or revert based on evidence



Status:



LOCKED



\---



\# 9. Stable Build Protection



Decision:



Stable builds and checkpoints must be protected.



Do not casually:



\- reset Git

\- clean untracked files

\- delete backups

\- delete memory snapshots

\- move stable tags

\- overwrite known-good checkpoints



Status:



LOCKED



\---



\# 10. Persistent Memory Protection



Decision:



Persistent memory is system state.



It must not be treated as disposable test data.



Safe deterministic tests should avoid writing to real persistent memory.



Status:



LOCKED



\---



\# 11. Evidence-Driven Architecture



Decision:



New components must earn their complexity.



A component should be questioned if it does not improve measurable performance.



Examples include:



\- memory

\- synthesis

\- right-brain reasoning

\- verifier depth

\- provider switching

\- neural routing

\- additional reasoning passes



Status:



LOCKED



\---



\# 12. Direct LLM Baselines



Decision:



DARREL must be compared against direct model baselines.



Future evaluation should compare:



\- direct local model

\- DARREL with local model

\- direct cloud model

\- DARREL with cloud model

\- full DARREL

\- DARREL with selected components removed



Status:



LOCKED



\---



\# 13. Ablation Testing



Decision:



Major architecture claims require ablation testing.



Examples:



\- full DARREL versus no memory

\- full DARREL versus no synthesis

\- full DARREL versus no verifier

\- full DARREL versus no creative reasoning

\- rule router versus future neural router



Status:



LOCKED



\---



\# 14. Neural Routing Is Future Experimental Work



Decision:



Neural Routing is not current production authority.



Initial Neural Routing should use a small prototype of approximately 10–20 cognitive signal neurons.



Status:



LOCKED



\---



\# 15. Neural Routing Shadow Mode First



Decision:



The first neural router must operate in shadow mode.



Shadow mode means:



1\. current router makes the real production decision

2\. neural router receives the same task/signals

3\. neural router predicts a route

4\. prediction is logged

5\. actual outcome is compared

6\. production behavior is unchanged



Status:



LOCKED



\---



\# 16. Neural Router Cannot Bypass Pulse



Decision:



Even after learning, Neural Routing cannot directly activate arbitrary cognition outside executive control.



The Selective Pulse Engine remains final authority.



Status:



LOCKED



\---



\# 17. Neural Routing Weights Must Learn From Outcomes



Decision:



Adaptive routing weights should not be introduced merely because they appear biologically interesting.



Weight changes must eventually be driven by measured outcomes such as:



\- answer quality

\- verifier result

\- latency

\- token use

\- provider cost

\- memory usefulness

\- user outcome

\- benchmark performance



Status:



LOCKED PRINCIPLE



Implementation timing remains future work.



\---



\# 18. Brain Metaphor Is Not Literal Architecture



Decision:



Left Brain / Right Brain is a useful cognitive diversity metaphor.



DARREL should not be constrained by literal human neuroanatomy.



Future architecture may include:



\- analytical perspective

\- creative perspective

\- skeptic

\- planner

\- evidence specialist

\- safety specialist

\- other specialist cognition



Status:



LOCKED



\---



\# 19. Independent Cognition Can Run in Parallel



Decision:



Independent cognitive work should run in parallel when dependencies allow.



Example:



left reasoning ─┐

&#x20;              ├→ synthesis

right reasoning ┘



The purpose is reduced wall-clock latency without sacrificing cognitive diversity.



Status:



LOCKED DIRECTION



Implementation should be benchmarked before large refactors.



\---



\# 20. Shared Cognitive Workspace



Decision:



Future cognition should exchange compact structured state rather than repeatedly copying entire histories.



A Shared Cognitive Workspace is an approved architectural direction.



Potential state includes:



\- task

\- hypotheses

\- evidence

\- uncertainty

\- objections

\- memory references

\- verifier feedback

\- budget

\- execution graph

\- stopping state



Status:



APPROVED FUTURE DIRECTION



\---



\# 21. Cognitive Intake Layer



Decision:



DARREL should eventually estimate cognitive requirements before expensive activation.



Potential signals include:



\- analysis

\- creativity

\- research

\- planning

\- memory relevance

\- uncertainty

\- safety

\- risk

\- verification need

\- mathematical reasoning

\- tool need

\- complexity



Status:



APPROVED V0.3 DIRECTION



\---



\# 22. Cognitive Budget Manager



Decision:



DARREL should eventually allocate an explicit cognitive budget.



Budget dimensions may include:



\- latency

\- tokens

\- provider calls

\- API cost

\- local compute

\- memory depth

\- module count

\- verifier depth

\- reasoning passes

\- research depth



Core question:



"How much cognition is this task worth?"



Status:



APPROVED V0.3/V1 DIRECTION



\---



\# 23. Cognitive Compiler



Decision:



The Cognitive Compiler is a major approved V1 architecture concept.



DARREL should eventually build a temporary task-specific cognitive execution graph rather than using one fixed pipeline for every request.



Status:



APPROVED SIGNATURE V1 DIRECTION



\---



\# 24. Temporary Cognitive Programs



Decision:



Future DARREL should support task-specific execution programs.



Examples:



simple arithmetic

→ calculator

→ verifier



research task

→ research

→ analysis

→ evidence verification



high-risk planning

→ planning

→ multiple reasoning perspectives

→ adversarial challenge

→ synthesis

→ safety verification



Status:



APPROVED FUTURE DIRECTION



\---



\# 25. Hierarchical Memory



Decision:



Future memory should evolve toward separate functional layers.



Potential layers:



\- working

\- episodic

\- semantic

\- procedural

\- user

\- project

\- hypothesis



Status:



APPROVED FUTURE DIRECTION



\---



\# 26. Memory Economics



Decision:



Future memories should carry usefulness metadata.



Potential metadata:



\- confidence

\- source quality

\- age

\- relevance

\- usage

\- importance

\- contradiction state

\- usefulness

\- decay

\- reinforcement



Status:



APPROVED FUTURE DIRECTION



\---



\# 27. Adversarial Verification



Decision:



Verification should eventually become mode-aware.



Potential modes:



\- logic

\- factual accuracy

\- mathematics

\- hallucination

\- evidence

\- safety

\- contradiction

\- counterexample

\- bias

\- assumption challenge



Status:



APPROVED FUTURE DIRECTION



\---



\# 28. Cognitive Opposition



Decision:



Some tasks should selectively use deliberate disagreement.



Possible pattern:



advocate

→ skeptic

→ neutral analyst

→ synthesis



This should not activate on every task.



Status:



APPROVED FUTURE DIRECTION



\---



\# 29. Stopping Intelligence



Decision:



DARREL should eventually learn whether further cognition has positive expected value.



The system should not keep thinking simply because more reasoning is possible.



Status:



APPROVED SIGNATURE V1 DIRECTION



\---



\# 30. Cognitive Performance Ledger



Decision:



DARREL should eventually maintain structured outcome records for cognition.



Potential fields:



\- task type

\- cognitive signals

\- route

\- modules

\- providers

\- tools

\- memory

\- latency

\- tokens

\- cost

\- verifier outcome

\- revision

\- final outcome

\- lessons



Status:



APPROVED SIGNATURE V1 DIRECTION



\---



\# 31. Cognitive Economy



Decision:



Modules and providers should eventually have measured cost and historical value.



DARREL should optimize expected benefit rather than raw compute usage.



Status:



APPROVED V1 DIRECTION



\---



\# 32. Self-Experimentation



Decision:



DARREL may eventually run controlled internal A/B or shadow experiments.



Examples:



\- route A versus route B

\- synthesis versus no synthesis

\- memory versus no memory

\- provider A versus provider B

\- shallow verifier versus deep verifier



Self-experimentation means evidence collection.



It does not mean unrestricted autonomous production self-modification.



Status:



APPROVED WITH SAFETY CONSTRAINT



\---



\# 33. Shadow Brain



Decision:



Future Neural Routing should begin as a Shadow Brain.



It may predict:



\- complexity

\- module activation

\- provider

\- budget

\- memory depth

\- verifier depth



It does not control production initially.



Status:



LOCKED FUTURE IMPLEMENTATION RULE



\---



\# 34. Executive Resolution



Decision:



User-facing output should not expose all internal cognitive detail.



DARREL should be rich internally and concise externally.



The final executive layer should:



\- resolve conflicts

\- preserve useful uncertainty

\- remove redundant internals

\- communicate clearly

\- adapt output to the user



Status:



LOCKED DESIGN PRINCIPLE



\---



\# 35. Learned Cognitive Programs



Decision:



Long-term learning should not be limited to routing weights.



DARREL may eventually learn reusable cognitive strategies or programs.



These may become procedural memory.



Status:



APPROVED LONG-TERM DIRECTION



\---



\# 36. Safe Automation



Decision:



Automation should first target repetitive engineering work, not autonomous architectural self-modification.



Approved early automation:



\- deterministic regression runner

\- startup scripts

\- benchmark scripts

\- provider diagnostics

\- GitHub Actions for safe mocked tests

\- release/checkpoint preparation



Status:



LOCKED NEAR-TERM DIRECTION



\---



\# 37. Codex Role



Decision:



Codex is the local execution and repository engineering environment.



Codex should:



\- inspect live code

\- edit files

\- run tests

\- run diagnostics

\- help automate engineering workflow



Codex must follow repository engineering instructions and protected-state rules.



Status:



LOCKED WORKFLOW DECISION



\---



\# 38. ChatGPT Role



Decision:



ChatGPT acts as lead architect / engineering coordinator.



Responsibilities include:



\- preserving architectural intent

\- directing engineering sequence

\- reviewing evidence

\- preventing architecture drift

\- coordinating Codex and GitHub workflow

\- updating engineering knowledge



Status:



LOCKED WORKFLOW DECISION



\---



\# 39. GitHub Role



Decision:



GitHub is the versioned shared engineering history.



Engineering docs should live in the repository so future engineers and Codex can access them.



No secrets may be stored in Git.



Status:



LOCKED



\---



\# 40. Current Version Boundary



Decision:



V0.2 should be stabilized before major V0.3/V1 architecture is promoted into production.



Future concepts may be:



\- documented

\- tested in isolation

\- benchmarked

\- run in shadow mode



They should not destabilize the known baseline.



Status:



LOCKED



\---



\# 41. Current Immediate Engineering Priority



Decision:



The current near-term sequence is:



1\. safe reproducible tests

2\. one-command safe test runner

3\. environment/reproducibility improvement

4\. provider validation

5\. benchmark repeatability

6\. telemetry

7\. documentation synchronization

8\. stable checkpoint

9\. only then begin measured V0.3 experiments



Status:



CURRENT PRIORITY



\---



\# 42. Signature Architecture Statement



Decision:



The long-term DARREL architecture is summarized as:



Estimate cognition

→ allocate resources

→ compile a temporary cognitive program

→ execute

→ measure whether it helped

→ learn how to allocate cognition better next time



DARREL should evolve toward a learned operating system for intelligence.



Status:



LOCKED V1 VISION

