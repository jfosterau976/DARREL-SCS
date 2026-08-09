\# DARREL / SCS V1 Architecture Roadmap



\## Purpose



This document defines the intended future architecture of DARREL / Synthetic Cognitive System (SCS).



It is a roadmap, not a statement that every feature described here is already implemented.



Current reproducible code remains authoritative for the live system.



The purpose of this roadmap is to preserve the long-term engineering direction so future work does not drift away from the core SCS hypothesis.



\---



\# 0. Current Implementation Boundary



IMPLEMENTED NOW:



\- V0.2 Selective Pulse production path

\- provider abstraction and fallback telemetry

\- verifier PASS / REVIEW with one corrective revision

\- memory relevance protection

\- memory-isolated safe regression runner

\- read-only development preflight and safe/shadow/all test classification

\- configuration-only credential-redacted provider diagnostics

\- deterministic benchmark result validation and structured capture contract

\- defensive telemetry snapshots



V0.3 SHADOW / EXPERIMENTAL:



\- Neural Routing V0.1 predicts complexity, risk, and module candidates from 16 signals

\- Cognitive Budget Manager V0.1 proposes diagnostic budgets and compares observed usage



Current isolated verification is 10 / 10 Neural Routing tests and 11 / 11 Cognitive Budget tests. Both layers reassert their no-authority contracts in comparison/error telemetry. Their comparison records expose additive data-quality metadata when malformed observation inputs are normalized; Cognitive Budget remains explicitly unenforced.



Neither shadow layer controls production. The current Attention Router remains authoritative and the Selective Pulse Engine remains the final executive activation gatekeeper.



The engineering-support additions above are protected by commits 601cd91, 611a773, 6dbcbd1, and c3974a6. They do not implement a Cognitive Compiler or dynamic execution graph.



FUTURE:



\- V0.4 Cognitive Compiler and temporary execution graphs

\- production or learned Neural Routing authority

\- production Cognitive Budget enforcement and stopping

\- remaining V1 architecture



\---



\# 1. Core SCS Hypothesis



DARREL should not behave like a single large model that performs the same amount of cognition for every task.



DARREL should instead estimate what cognition is required, activate only useful resources, measure the outcome, and learn how to make better activation decisions over time.



The central long-term loop is:



INPUT

→ estimate required cognition

→ allocate resources

→ compile a temporary cognitive program

→ execute selected cognition

→ synthesize if useful

→ verify if justified

→ decide whether more cognition is worthwhile

→ produce final output

→ record the outcome

→ learn how to allocate cognition better next time



The target is not simply more intelligence through more computation.



The target is better intelligence through better allocation of cognition.



\---



\# 2. DARREL Is Not the LLM



DARREL is the cognitive system.



LLMs are interchangeable reasoning resources inside DARREL.



DARREL should eventually be able to choose between:



\- local language models

\- cloud language models

\- specialist reasoning models

\- search

\- calculators

\- Python

\- structured tools

\- databases

\- memory systems

\- specialist agents

\- deterministic logic



No provider should become permanently coupled to the architecture.



Provider choice should eventually become part of cognitive routing.



\---



\# 3. Cognitive Intake Layer



Before activating expensive cognition, DARREL should estimate what kind of task it has received.



Neural Routing V0.1 currently provides a limited shadow signal prototype. There is no separate production Cognitive Intake authority yet.



The Cognitive Intake Layer should produce signals such as:



\- analysis requirement

\- creativity requirement

\- factual research requirement

\- memory relevance

\- planning requirement

\- uncertainty

\- safety risk

\- verification requirement

\- mathematical reasoning requirement

\- tool requirement

\- urgency

\- expected task complexity

\- expected value of additional cognition



These signals should inform routing but should not directly execute modules.



The Selective Pulse Engine remains the executive gatekeeper.



\---



\# 4. Cognitive Budget Manager



Cognitive Budget Manager V0.1 now proposes an explicit diagnostic cognitive budget in shadow mode.



It has authority=false and enforced=false. Production budget control remains future work.



The budget may include:



\- latency

\- model calls

\- token usage

\- API cost

\- local compute

\- memory retrieval depth

\- number of active modules

\- number of reasoning passes

\- verifier depth

\- research depth

\- corrective revision allowance



The Cognitive Budget Manager should answer:



"How much cognition is this task worth?"



Simple tasks should use very little cognition.



Complex or high-risk tasks may justify deeper cognition.



The budget should not be static.



It should eventually learn from historical outcomes.



\---



\# 5. Cognitive Compiler



The Cognitive Compiler is a key V1 architecture concept.



It is a future V0.4 prototype. It is not implemented, and V0.4 has not started.



Instead of using one fixed pipeline for every task, DARREL should dynamically compile a temporary cognitive execution graph for each request.



Example:



Simple arithmetic:



INPUT

→ calculator

→ verifier

→ OUTPUT



Creative design task:



INPUT

→ creative reasoning

→ analytical reasoning

→ synthesis

→ verifier

→ OUTPUT



Current-fact research task:



INPUT

→ research

→ evidence extraction

→ analytical reasoning

→ verifier

→ OUTPUT



High-risk planning task:



INPUT

→ planning

→ left reasoning

→ right reasoning

→ adversarial challenge

→ synthesis

→ safety verification

→ corrective revision if required

→ OUTPUT



The execution graph should be temporary and task-specific.



DARREL should eventually learn which cognitive programs work best for different task classes.



\---



\# 6. Selective Pulse Engine



The Selective Pulse Engine remains the final executive activation authority.



Other systems may recommend activation, including:



\- rule-based routing

\- cognitive signal neurons

\- neural routing

\- learned routing weights

\- provider selection logic

\- budget decisions



But they do not bypass the Pulse Engine.



The Pulse Engine determines what actually activates.



This protects the architecture from uncontrolled routing complexity.



\---



\# 7. Specialist Cognition



Most cognitive modules should normally remain inactive.



They should activate only when useful.



Potential specialists include:



\- analytical reasoning

\- creative reasoning

\- planning

\- research

\- synthesis

\- verification

\- safety

\- mathematics

\- code reasoning

\- evidence analysis

\- memory retrieval

\- reflection

\- learning

\- optimization

\- counterargument generation



The architectural goal is not maximum simultaneous activation.



The goal is minimum useful activation.



\---



\# 8. Parallel Cognition



Independent cognitive work should run in parallel when possible.



For example:



LEFT REASONING ─┐

&#x20;               ├→ synthesis

RIGHT REASONING ┘



There is little benefit in waiting for independent modules sequentially if they do not depend on one another.



Parallel execution should reduce wall-clock latency without reducing cognitive diversity.



\---



\# 9. Neural-Linked Dual Brain Direction



The existing Left Brain / Right Brain metaphor should remain flexible.



It should not become an artificial biological constraint.



The useful idea is independent cognitive perspectives.



Potential structure:



\- analytical perspective

\- creative perspective

\- skeptical perspective

\- planner

\- evidence specialist

\- safety specialist



Future designs may generalize beyond two brains.



The value comes from cognitive diversity and disagreement, not literal imitation of human brain anatomy.



\---



\# 10. Shared Cognitive Workspace



DARREL should eventually have a structured shared workspace where active cognitive modules can exchange compact state.



The workspace may contain:



\- task representation

\- active hypothesis

\- evidence

\- uncertainty

\- goals

\- objections

\- memory references

\- intermediate conclusions

\- verifier feedback

\- resource budget

\- current cognitive program

\- stopping state



Modules should exchange useful summaries rather than constantly copying entire reasoning histories.



The workspace should support coordination without creating massive context duplication.



\---



\# 11. Neural Routing Layer



Neural Routing V0.1 shadow telemetry is implemented, but Neural Routing is not current production authority.



Current V0.1 prototype:



16 deterministic normalized software signals with static versioned weights.



Exact implemented signals cover request length, multi-part density, constraints, question breadth, factual lookup, calculation, analysis, comparison, planning, creativity, decision support, risk, safety, uncertainty, verification, and memory relevance.



Future signals may include:



\- analysis

\- creativity

\- uncertainty

\- safety

\- risk

\- memory relevance

\- planning

\- research

\- verification

\- novelty

\- complexity

\- evidence need

\- mathematical need

\- tool need

\- expected benefit of deeper thought



Weighted synapses connect cognitive signals to:



\- modules

\- providers

\- tools

\- memory systems

\- routing policies



Weights may eventually adapt based on measured outcomes.



The current rollout uses SHADOW MODE.



In shadow mode:



1\. current router makes the real decision

2\. neural router predicts what it would activate

3\. prediction is recorded

4\. outcome is compared

5\. no production behavior changes



Only after benchmark evidence should neural routing gain authority.



The Selective Pulse Engine remains the final execution gate.



\---



\# 12. Provider-Aware Cognition



DARREL should eventually decide not only what cognition is required, but which provider is best suited to it.



Possible considerations:



\- provider quality

\- task specialization

\- token cost

\- latency

\- privacy

\- offline availability

\- context window

\- reasoning ability

\- reliability

\- historical success on similar tasks



Example:



simple task

→ local Qwen



high-value synthesis

→ Claude or another strong cloud model



calculation

→ calculator or Python



fresh factual query

→ search + reasoning



Provider choice should become part of cognitive economics.



\---



\# 13. Hierarchical Memory



Memory should evolve beyond one flat store.



Potential layers:



\## Working Memory



Temporary context for the current cognitive episode.



\## Episodic Memory



Past interactions and events.



\## Semantic Memory



Stable concepts and learned facts.



\## Procedural Memory



Reusable strategies and cognitive programs.



\## User Memory



Long-term user-specific preferences and context.



\## Project Memory



Persistent state for ongoing projects such as DARREL itself.



\## Hypothesis Memory



Tracked assumptions, experiments, and unresolved questions.



Memory retrieval should be relevance-driven.



Memory should never be injected merely because it exists.



\---



\# 14. Memory Economics



Memories should eventually carry metadata such as:



\- relevance

\- confidence

\- source quality

\- age

\- usage count

\- historical usefulness

\- contradiction state

\- risk of harm

\- importance

\- decay value

\- reinforcement value



Useful memories may strengthen.



Irrelevant or weak memories may decay.



Contradictory evidence should reduce confidence.



The objective is to prevent memory accumulation from degrading cognition.



\---



\# 15. Adversarial Verification



Verification should evolve beyond a generic PASS / REVIEW signal.



Possible verifier modes:



\- logical consistency

\- factual accuracy

\- mathematical correctness

\- hallucination detection

\- evidence adequacy

\- safety

\- policy compliance

\- counterexample search

\- internal contradiction

\- bias detection

\- assumption challenge



DARREL should choose the verifier depth based on task risk and uncertainty.



A low-risk task should not trigger an expensive adversarial process unnecessarily.



\---



\# 16. Cognitive Opposition



Some tasks benefit from deliberate disagreement.



Possible pattern:



ADVOCATE

→ strongest case for proposal



SKEPTIC

→ strongest case against proposal



NEUTRAL ANALYST

→ evaluates both



SYNTHESIS

→ reconciles evidence



This should activate selectively rather than on every request.



The verifier must be genuinely able to disagree with other reasoning modules.



\---



\# 17. Stopping Intelligence



One of the most important future capabilities is knowing when to stop thinking.



DARREL should estimate:



"Will another cognitive step improve the answer enough to justify its cost?"



Possible stop signals:



\- verifier confidence is high

\- independent modules agree

\- uncertainty is low

\- additional reasoning produces little change

\- budget exhausted

\- evidence saturated

\- task value does not justify more work



Possible continue signals:



\- unresolved contradiction

\- low confidence

\- high safety risk

\- missing evidence

\- major disagreement

\- verifier review

\- high expected value from one additional step



Stopping intelligence prevents recursive overthinking.



\---



\# 18. Cognitive Performance Ledger



DARREL should maintain a structured record of cognitive outcomes.



For each task, eventually record:



\- task class

\- complexity estimate

\- cognitive signals

\- routing decision

\- modules activated

\- providers used

\- tools used

\- memory retrieved

\- execution graph

\- latency

\- tokens

\- provider cost

\- verifier outcome

\- corrective revision

\- final confidence

\- user outcome if available

\- later success/failure signal

\- lessons



This becomes the evidence base for learning better routing behavior.



\---



\# 19. Cognitive Economy



Each module should eventually have an estimated cost and historical benefit.



DARREL should learn relationships such as:



\- synthesis usually helps for task class X

\- right-brain activation rarely improves task class Y

\- full verifier is valuable for high-risk task Z

\- local model is sufficient for simple task A

\- cloud provider gives meaningful improvement for task B

\- extra reasoning pass does not justify cost for task C



The system should optimize expected cognitive value rather than raw compute.



\---



\# 20. Self-Experimentation



DARREL should eventually be able to run controlled internal experiments.



Examples:



\- normal route versus alternative route

\- synthesis versus no synthesis

\- memory versus no memory

\- local model versus cloud model

\- rule router versus shadow neural router

\- single reasoning path versus opposition

\- shallow verifier versus deep verifier



Experiments must be controlled and measured.



DARREL should not autonomously rewrite its production architecture without engineering review.



Self-experimentation means evidence collection, not uncontrolled self-modification.



\---



\# 21. Shadow Brain



Neural Routing V0.1 currently operates as a limited Shadow Brain. Broader provider, budget, verifier-depth, memory-depth, and learned routing remain future work.



The Shadow Brain receives the same task and cognitive signals as the live router.



It predicts:



\- cognitive complexity

\- modules

\- provider

\- budget

\- verifier depth

\- memory depth



But it does not control execution.



Its predictions are compared against actual results.



This allows learning without destabilizing the stable system.



\---



\# 22. Executive Resolution Layer



The final user-facing answer should not expose every internal cognitive process.



The Executive Resolution Layer should:



\- select the useful conclusions

\- resolve conflicts

\- remove redundant internal detail

\- preserve uncertainty when appropriate

\- communicate clearly

\- adapt output length to the user



DARREL should be rich internally but simple externally.



\---



\# 23. Learned Cognitive Programs



A major long-term opportunity is learning reusable cognitive strategies.



Instead of only learning routing weights, DARREL may learn reusable programs such as:



"For high-risk comparison tasks:

research both options

→ skeptic each

→ synthesis

→ evidence verifier"



or:



"For simple factual recall:

memory check

→ one reasoning call

→ lightweight verifier"



These programs may become procedural memory.



This would allow DARREL to learn how to think, not just which module to activate.



\---



\# 24. Measurement and Ablation



Architecture decisions must be supported by measurement.



Required comparisons should eventually include:



\- direct LLM baseline

\- full DARREL

\- DARREL without memory

\- DARREL without creative reasoning

\- DARREL without synthesis

\- DARREL without verifier

\- local provider direct versus DARREL/local

\- cloud provider direct versus DARREL/cloud

\- rule router versus neural router

\- shallow cognition versus deep cognition



Track:



\- correctness

\- usefulness

\- hallucination rate

\- latency

\- tokens

\- provider cost

\- cognitive activation

\- verifier outcome

\- memory usefulness

\- user outcome where available



A component that does not improve measurable performance should be questioned.



\---



\# 25. Target Runtime Philosophy



Approximate long-term goals:



Simple deterministic/local tasks:

under approximately 1 second where possible.



Normal conversational reasoning:

approximately 1–5 seconds.



Selective multi-module cognition:

approximately 5–15 seconds.



High-risk or deep cognitive tasks:

15+ seconds only when measurable benefit justifies it.



These are design targets, not guaranteed limits.



Parallel execution should be used whenever dependencies allow.



\---



\# 26. Development Phases



\## V0.2



Goal:

stabilize current Selective Pulse architecture.



Current status:



IMPLEMENTED production baseline. Safe testing, memory isolation, provider reliability, verification, relevance protection, telemetry, and reproducibility remain stabilization concerns.



Focus:



\- provider reliability

\- regression testing

\- contract protection

\- learned memory relevance

\- corrective verification

\- telemetry

\- reproducibility

\- safe automation



Do not destabilize V0.2 by promoting Neural Routing beyond shadow telemetry without evidence and explicit approval.



\## V0.3



Goal:

introduce richer cognitive signals and explicit budgeting.



Current status:



V0.3 SHADOW / EXPERIMENTAL. Neural Routing V0.1 and Cognitive Budget Manager V0.1 are implemented only as telemetry. Neither has production authority.



Potential work:



\- Cognitive Intake

\- Cognitive Budget Manager

\- improved routing telemetry

\- task classification

\- stopping-signal prototypes



\## V0.4



Goal:

prototype Cognitive Compiler and temporary execution graphs.



Current status:



FUTURE. Not started and not approved for implementation by this documentation synchronization.



\## V0.5



Goal:

hierarchical memory and memory economics.



\## V0.6



Goal:

Cognitive Performance Ledger and outcome-driven routing learning.



\## V0.7



Goal:

Neural Router / Shadow Brain experiment.



\## V0.8



Goal:

advanced adversarial verification and specialist cognition.



\## V1



Goal:

experimental learned operating system for intelligence.



The V1 system should be capable of deciding:



\- what cognition is required

\- how much cognition is worth spending

\- which resources should perform it

\- when disagreement is useful

\- when verification is justified

\- when to stop

\- whether the chosen cognitive program actually helped

\- how to improve future cognitive allocation



\---



\# 27. Engineering Constraints



Do not:



\- replace stable architecture based only on intuition

\- integrate neural routing directly into production before shadow testing

\- allow learned routing to bypass the Pulse Engine

\- activate every module by default

\- inject all available memory

\- assume more model calls automatically means better cognition

\- couple DARREL permanently to one provider

\- optimize benchmarks at the expense of real system behavior

\- allow self-experimentation to become uncontrolled self-modification



\---



\# 28. Signature Design Principle



The strongest long-term architectural formulation is:



Estimate cognition

→ allocate resources

→ compile a temporary cognitive program

→ execute

→ measure whether it helped

→ learn how to allocate cognition better next time



DARREL should evolve into a learned operating system for intelligence.



The goal is not to imitate a biological brain literally.



The goal is to build a system that learns how to spend cognition intelligently.

