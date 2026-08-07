# Module Reference

## core\__init__.py

### Classes
- None

### Functions
- None

### Imports
- None

---

## core\adaptive_decision_test.py

### Classes
- None

### Functions
- adaptive_decide

### Imports
- core.decision_feedback_bridge

---

## core\adaptive_effort_controller.py

### Classes
- AdaptiveEffortController

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\adaptive_learning_loop.py

### Classes
- AdaptiveLearningLoop

### Functions
- __init__
- learn

### Imports
- core.cognitive_memory

---

## core\adaptive_learning_loop_checkpoint.py

### Classes
- AdaptiveLearningLoop

### Functions
- __init__
- learn

### Imports
- core.cognitive_memory

---

## core\adaptive_loop_test.py

### Classes
- None

### Functions
- run_adaptive_test

### Imports
- core.decision_feedback_bridge
- core.ooda_loop

---

## core\agent_context.py

### Classes
- AgentContext

### Functions
- __init__
- get_context

### Imports
- core.communication_bus

---

## core\agent_message_router.py

### Classes
- AgentMessageRouter

### Functions
- __init__
- route
- inbox

### Imports
- core.communication_bus

---

## core\agent_organizer.py

### Classes
- AgentOrganizer

### Functions
- __init__
- register
- get
- list_agents
- health_check

### Imports
- None

---

## core\agent_registry.py

### Classes
- AgentRegistry

### Functions
- __init__
- add_agent
- get_agent
- find_by_skill
- list_all

### Imports
- None

---

## core\attention_manager.py

### Classes
- AttentionManager

### Functions
- __init__
- analyse_priority

### Imports
- None

---

## core\attention_manager_FOUNDATION_V1.py

### Classes
- AttentionManager

### Functions
- __init__
- analyse_priority

### Imports
- None

---

## core\attention_router.py

### Classes
- AttentionRouter

### Functions
- __init__
- calculate_state
- route

### Imports
- core.attention_manager
- core.cognitive_memory
- core.selective_activation_engine

---

## core\attention_router_V01_WORKING_BACKUP.py

### Classes
- AttentionRouter

### Functions
- __init__
- calculate_state
- route

### Imports
- core.attention_manager
- core.selective_activation_engine

---

## core\attention_router_V1_WORKING.py

### Classes
- AttentionRouter

### Functions
- __init__
- calculate_state
- route

### Imports
- core.attention_manager
- core.selective_activation_engine

---

## core\branch_manager.py

### Classes
- BranchManager

### Functions
- __init__
- activate

### Imports
- None

---

## core\branch_manager_v01_backup.py

### Classes
- BranchManager

### Functions
- __init__
- activate

### Imports
- None

---

## core\branch_manager_v02_working.py

### Classes
- BranchManager

### Functions
- __init__
- activate

### Imports
- None

---

## core\cognitive_controller.py

### Classes
- CognitiveController

### Functions
- __init__
- identify_skills
- select_agents
- think

### Imports
- core.coordinator
- core.executive_manager
- core.improvement_memory

---

## core\cognitive_controller_v01_backup.py

### Classes
- CognitiveController

### Functions
- __init__
- identify_skills
- select_agents
- think

### Imports
- core.coordinator
- core.executive_manager
- core.improvement_memory

---

## core\cognitive_effort_controller.py

### Classes
- CognitiveEffortController

### Functions
- __init__
- calculate

### Imports
- None

---

## core\cognitive_memory.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- memory_identity
- update_importance
- remember
- store
- recall
- find_memory_type
- strengthen_memory
- score_relevance
- recall_relevant

### Imports
- json
- os

---

## core\cognitive_memory_backup_v01.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- store
- recall

### Imports
- json
- os

---

## core\cognitive_memory_backup_v02.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- store
- recall

### Imports
- json
- os

---

## core\cognitive_memory_backup_v03.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- recall

### Imports
- json
- os

---

## core\cognitive_memory_checkpoint.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- store
- recall

### Imports
- json
- os

---

## core\cognitive_memory_CLEAN_WITH_SEARCH_V1.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- find_memory_type
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_memory_DEDUP_V1.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_memory_IMPORTANCE_V1.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- find_memory_type
- strengthen_memory
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_memory_MEMORY_SEARCH_V1.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- score_relevance
- recall_relevant
- recall
- find_memory_type

### Imports
- json
- os

---

## core\cognitive_memory_STABLE_MEMORY_V1.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- find_memory_type
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_memory_STRENGTHENING_V1.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- find_memory_type
- strengthen_memory
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_memory_V20_STABLE.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_memory_WORKING_BACKUP.py

### Classes
- CognitiveMemory

### Functions
- __init__
- load
- save
- remember
- store
- score_relevance
- recall_relevant
- recall

### Imports
- json
- os

---

## core\cognitive_message.py

### Classes
- CognitiveMessage

### Functions
- create_message
- __init__
- to_dict

### Imports
- None

---

## core\cognitive_orchestrator.py

### Classes
- CognitiveOrchestrator

### Functions
- __init__
- decide

### Imports
- None

---

## core\cognitive_orchestrator_checkpoint.py

### Classes
- CognitiveOrchestrator

### Functions
- __init__
- decide

### Imports
- None

---

## core\cognitive_output_formatter.py

### Classes
- CognitiveOutputFormatter

### Functions
- __init__
- format_left
- format_right
- format

### Imports
- None

---

## core\cognitive_performance_memory.py

### Classes
- CognitivePerformanceMemory

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\cognitive_performance_memory_checkpoint.py

### Classes
- CognitivePerformanceMemory

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\cognitive_performance_monitor.py

### Classes
- CognitivePerformanceMonitor

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\cognitive_performance_monitor_checkpoint.py

### Classes
- CognitivePerformanceMonitor

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\cognitive_pipeline.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.research_agent
- core.tree_router
- core.verifier_engine

---

## core\cognitive_pipeline_backup_v01.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.tree_router

---

## core\cognitive_pipeline_backup_v02.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.synthesis_agent
- core.tree_router

---

## core\cognitive_pipeline_backup_v03.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.synthesis_agent
- core.tree_router

---

## core\cognitive_pipeline_backup_v04.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

---

## core\cognitive_pipeline_checkpoint_v01.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

---

## core\cognitive_pipeline_checkpoint_v02.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

---

## core\cognitive_pipeline_checkpoint_v03.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

---

## core\cognitive_pipeline_checkpoint_v04.py

### Classes
- CognitivePipeline

### Functions
- __init__
- run

### Imports
- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.research_agent
- core.tree_router
- core.verifier_engine

---

## core\cognitive_pulse_controller.py

### Classes
- CognitivePulseController

### Functions
- __init__
- run

### Imports
- core.attention_router
- core.pulse
- core.pulse_orchestrator

---

## core\cognitive_pulse_v1.py

### Classes
- CognitivePulseV1

### Functions
- __init__
- run

### Imports
- core.left_cognitive_engine
- core.right_cognitive_engine
- core.synthesis_engine
- core.verifier_engine

---

## core\cognitive_pulse_v1_checkpoint.py

### Classes
- CognitivePulseV1

### Functions
- __init__
- run

### Imports
- core.left_cognitive_engine
- core.right_cognitive_engine
- core.synthesis_engine
- core.verifier_engine

---

## core\cognitive_regulation_engine.py

### Classes
- CognitiveRegulationEngine

### Functions
- __init__
- regulate

### Imports
- None

---

## core\cognitive_state_manager.py

### Classes
- CognitiveStateManager

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\communication_bus.py

### Classes
- CommunicationBus

### Functions
- __init__
- send
- get_messages
- clear

### Imports
- None

---

## core\context_manager.py

### Classes
- ContextManager

### Functions
- __init__
- get_context

### Imports
- None

---

## core\coordinator.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.learning_feedback
- core.memory_consolidator
- core.pulse
- core.reflection_agent
- core.scs_executive
- datetime
- time

---

## core\coordinator_BACKUP.py

### Classes
- Coordinator

### Functions
- __init__
- run_cycle
- process

### Imports
- agents.synthesis_agent
- agents.verifier_agent
- core.left_brain
- core.persistent_memory
- core.right_brain

---

## core\coordinator_backup_v01.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_COGNITIVE_LOOP_V1.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_DUAL_MEMORY_V1.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_FULL_COGNITION_V1.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_LEARNED_REASONING_CONNECTED_V1.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_LEARNING_LOOP_CONNECTED_BACKUP.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.learning_feedback
- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_LEFT_MEMORY_V1.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\coordinator_REFLECTION_LOOP_V1.py

### Classes
- Coordinator

### Functions
- __init__
- process

### Imports
- core.left_brain
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\decision_engine.py

### Classes
- DecisionEngine

### Functions
- __init__
- decide

### Imports
- None

---

## core\decision_feedback_bridge.py

### Classes
- DecisionFeedbackBridge

### Functions
- __init__
- update_strategy

### Imports
- core.feedback_controller

---

## core\decision_router.py

### Classes
- DecisionRouter

### Functions
- __init__
- decide

### Imports
- None

---

## core\effort_activation_map.py

### Classes
- EffortActivationMap

### Functions
- __init__
- activate

### Imports
- None

---

## core\executive_manager.py

### Classes
- ExecutiveManager

### Functions
- __init__
- create_plan

### Imports
- None

---

## core\experience_loop_checkpoint.py

### Classes
- None

### Functions
- run_experience

### Imports
- core.cognitive_memory
- core.learning_coordinator

---

## core\experience_loop_test.py

### Classes
- None

### Functions
- run_experience

### Imports
- core.cognitive_memory
- core.learning_coordinator

---

## core\experience_replay_engine.py

### Classes
- ExperienceReplayEngine

### Functions
- __init__
- store
- recall

### Imports
- None

---

## core\experience_replay_engine_checkpoint.py

### Classes
- ExperienceReplayEngine

### Functions
- __init__
- store
- recall

### Imports
- None

---

## core\experience_strategy_selector.py

### Classes
- ExperienceStrategySelector

### Functions
- __init__
- select

### Imports
- None

---

## core\experience_strategy_selector_checkpoint.py

### Classes
- ExperienceStrategySelector

### Functions
- __init__
- select

### Imports
- None

---

## core\feedback_connection_test.py

### Classes
- None

### Functions
- test_feedback

### Imports
- core.feedback_interpreter

---

## core\feedback_controller.py

### Classes
- FeedbackController

### Functions
- __init__
- process

### Imports
- core.feedback_interpreter

---

## core\feedback_interpreter.py

### Classes
- FeedbackInterpreter

### Functions
- __init__
- interpret

### Imports
- None

---

## core\full_cognitive_pulse_checkpoint.py

### Classes
- None

### Functions
- run_full_pulse

### Imports
- core.pulse_orchestrator
- core.scs_executive

---

## core\full_cognitive_pulse_test.py

### Classes
- None

### Functions
- run_full_pulse

### Imports
- core.pulse_orchestrator
- core.scs_executive

---

## core\goal_feedback_engine.py

### Classes
- GoalFeedbackEngine

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\goal_planning_engine.py

### Classes
- GoalPlanningEngine

### Functions
- __init__
- create_goal
- create_plan
- think

### Imports
- None

---

## core\goal_planning_engine_checkpoint.py

### Classes
- GoalPlanningEngine

### Functions
- __init__
- create_goal
- create_plan

### Imports
- None

---

## core\improvement_memory.py

### Classes
- ImprovementMemory

### Functions
- __init__
- save_improvement
- load_memory

### Imports
- datetime
- json
- os

---

## core\learning_coordinator.py

### Classes
- LearningCoordinator

### Functions
- __init__
- decide_learning_path

### Imports
- core.cognitive_memory

---

## core\learning_coordinator_checkpoint.py

### Classes
- LearningCoordinator

### Functions
- __init__
- decide_learning_path

### Imports
- core.memory_gate

---

## core\learning_extractor.py

### Classes
- LearningExtractor

### Functions
- __init__
- extract

### Imports
- datetime

---

## core\learning_feedback.py

### Classes
- LearningFeedback

### Functions
- __init__
- evaluate
- recall_lessons

### Imports
- core.cognitive_memory

---

## core\learning_feedback_BACKUP_BEFORE_V2.py

### Classes
- LearningFeedback

### Functions
- __init__
- evaluate
- recall_lessons

### Imports
- core.cognitive_memory

---

## core\learning_feedback_backup_v01.py

### Classes
- LearningFeedback

### Functions
- __init__
- evaluate

### Imports
- None

---

## core\learning_feedback_backup_v02.py

### Classes
- LearningFeedback

### Functions
- __init__
- evaluate
- recall_lessons

### Imports
- None

---

## core\left_brain.py

### Classes
- LeftBrain

### Functions
- __init__
- apply_learned_reasoning
- build_memory_context
- build_prompt
- think
- analyse
- analyze

### Imports
- core.llm_interface
- core.memory_consolidator

---

## core\left_brain_ADAPTIVE_REASONING_CONNECTED_V1.py

### Classes
- LeftBrain

### Functions
- __init__
- apply_learned_reasoning
- think
- analyse
- analyze

### Imports
- core.memory_consolidator

---

## core\left_brain_BEFORE_ADAPTIVE_REASONING_V1.py

### Classes
- LeftBrain

### Functions
- __init__
- apply_learned_reasoning
- think
- analyse
- analyze

### Imports
- core.memory_consolidator

---

## core\left_brain_checkpoint_v01.py

### Classes
- LeftBrain

### Functions
- __init__
- process
- analyse
- analyze

### Imports
- None

---

## core\left_brain_LEARNED_CONTEXT_V1.py

### Classes
- LeftBrain

### Functions
- __init__
- think
- analyse
- analyze

### Imports
- core.memory_consolidator

---

## core\left_brain_REASONING_CONTEXT_V1.py

### Classes
- LeftBrain

### Functions
- __init__
- apply_learned_reasoning
- think
- analyse
- analyze

### Imports
- core.memory_consolidator

---

## core\left_brain_V20_STABLE.py

### Classes
- LeftBrain

### Functions
- __init__
- process
- analyse
- analyze
- think

### Imports
- None

---

## core\left_brain_V21_backup.py

### Classes
- LeftBrain

### Functions
- __init__
- process
- analyse
- analyze
- think

### Imports
- None

---

## core\left_cognitive_engine.py

### Classes
- LeftCognitiveEngine

### Functions
- __init__
- analyze

### Imports
- None

---

## core\left_cognitive_engine_checkpoint.py

### Classes
- LeftCognitiveEngine

### Functions
- __init__
- analyze

### Imports
- None

---

## core\llm_interface.py

### Classes
- LLMInterface

### Functions
- __init__
- connect
- generate

### Imports
- json
- os
- urllib.error
- urllib.request

---

## core\llm_interface_backup.py

Error reading file: invalid syntax (<unknown>, line 90)

## core\memory.py

### Classes
- Memory

### Functions
- __init__
- remember
- recall

### Imports
- None

---

## core\memory_advisor.py

### Classes
- MemoryAdvisor

### Functions
- __init__
- advise

### Imports
- core.memory_retriever

---

## core\memory_advisor_checkpoint.py

### Classes
- MemoryAdvisor

### Functions
- __init__
- advise

### Imports
- core.memory_retriever

---

## core\memory_agent.py

### Classes
- None

### Functions
- None

### Imports
- None

---

## core\memory_consolidator.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_consolidator_BEFORE_REASONING_V1.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- find_related
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_consolidator_PRIORITY_V1.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- find_related
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_consolidator_PRIORITY_V2.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- find_related
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_consolidator_REASONING_CONNECTED_V1.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- find_related
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_consolidator_V2_BACKUP.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- find_related
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_consolidator_V2_STABLE.py

### Classes
- MemoryConsolidator

### Functions
- __init__
- is_noise
- find_related
- consolidate

### Imports
- core.cognitive_memory

---

## core\memory_gate.py

### Classes
- MemoryGate

### Functions
- __init__
- evaluate

### Imports
- core.memory_advisor

---

## core\memory_gate_checkpoint.py

### Classes
- MemoryGate

### Functions
- __init__
- evaluate

### Imports
- core.memory_advisor

---

## core\memory_optimizer.py

### Classes
- MemoryOptimizer

### Functions
- __init__
- optimize

### Imports
- json
- os

---

## core\memory_retriever.py

### Classes
- MemoryRetriever

### Functions
- __init__
- search

### Imports
- core.cognitive_memory

---

## core\memory_retriever_checkpoint.py

### Classes
- MemoryRetriever

### Functions
- __init__
- search

### Imports
- core.cognitive_memory

---

## core\message_bus.py

### Classes
- MessageBus

### Functions
- __init__
- load_messages
- save_messages
- send
- broadcast
- read_for_agent
- get_messages

### Imports
- json
- os

---

## core\message_bus_backup_v01.py

### Classes
- MessageBus

### Functions
- __init__
- send
- get_messages

### Imports
- None

---

## core\message_bus_checkpoint_v02.py

### Classes
- MessageBus

### Functions
- __init__
- send
- broadcast
- get_messages

### Imports
- None

---

## core\message_bus_checkpoint_v03.py

### Classes
- MessageBus

### Functions
- __init__
- send
- broadcast
- read_for_agent
- get_messages

### Imports
- None

---

## core\module_registry.py

### Classes
- ModuleRegistry

### Functions
- __init__
- register
- get
- exists
- remove
- available_modules
- count

### Imports
- None

---

## core\module_registry_setup.py

### Classes
- None

### Functions
- register_modules
- get_registry

### Imports
- core.goal_planning_engine
- core.learning_extractor
- core.left_brain
- core.module_registry
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\neural_tree_executor.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- core.message_bus

---

## core\neural_tree_executor_backup.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- None

---

## core\neural_tree_executor_backup_v01.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- core.message_bus

---

## core\neural_tree_executor_backup_v02.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- None

---

## core\neural_tree_executor_checkpoint_v01.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- core.message_bus

---

## core\neural_tree_executor_v02_backup.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- None

---

## core\neural_tree_executor_v02_working.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- None

---

## core\neural_tree_executor_v03_backup.py

### Classes
- NeuralTreeExecutor

### Functions
- __init__
- execute

### Imports
- core.agent_message_router

---

## core\neural_tree_manager.py

### Classes
- NeuralTreeManager

### Functions
- __init__
- view_tree
- activate_branch

### Imports
- None

---

## core\ooda_loop.py

### Classes
- OODA_Loop

### Functions
- __init__
- observe
- orient
- decide
- act

### Imports
- None

---

## core\ooda_loop_before_adaptive_decide.py

### Classes
- OODA_Loop

### Functions
- __init__
- observe
- orient
- decide
- act

### Imports
- None

---

## core\ooda_loop_before_self_adaptive.py

### Classes
- OODA_Loop

### Functions
- __init__
- observe
- orient
- decide
- act

### Imports
- None

---

## core\ooda_loop_before_smart_decide.py

### Classes
- OODA_Loop

### Functions
- __init__
- observe
- orient
- decide
- act

### Imports
- None

---

## core\ooda_loop_V02_adaptive_checkpoint.py

### Classes
- OODA_Loop

### Functions
- __init__
- observe
- orient
- decide
- act

### Imports
- None

---

## core\orchestrated_scs.py

### Classes
- OrchestratedSCS

### Functions
- __init__
- think

### Imports
- core.cognitive_orchestrator
- core.self_managing_scs

---

## core\orchestrated_scs_checkpoint.py

### Classes
- OrchestratedSCS

### Functions
- __init__
- think

### Imports
- core.cognitive_orchestrator
- core.self_managing_scs

---

## core\orchestrated_scs_v2.py

### Classes
- OrchestratedSCSV2

### Functions
- __init__
- think

### Imports
- core.self_managing_scs

---

## core\orchestrated_scs_v2_BACKUP.py

Error reading file: '(' was never closed (<unknown>, line 24)

## core\orchestrated_scs_v2_broken_backup.py

### Classes
- OrchestratedSCSV2

### Functions
- __init__
- think

### Imports
- core.cognitive_orchestrator
- core.left_brain
- core.right_brain
- core.selective_activation_engine
- core.self_managing_scs
- core.synthesis_engine
- core.verifier_engine

---

## core\orchestrated_scs_v2_checkpoint.py

### Classes
- OrchestratedSCSV2

### Functions
- __init__
- think

### Imports
- core.cognitive_orchestrator
- core.selective_activation_engine
- core.self_managing_scs

---

## core\orchestrated_scs_v2_V20_STABLE.py

### Classes
- OrchestratedSCSV2

### Functions
- __init__
- safe_output
- think

### Imports
- core.cognitive_orchestrator
- core.left_brain
- core.right_brain
- core.selective_activation_engine
- core.self_managing_scs
- core.synthesis_engine
- core.verifier_engine

---

## core\persistent_memory.py

### Classes
- PersistentMemory

### Functions
- __init__
- _load
- remember
- _save
- recall

### Imports
- json
- pathlib

---

## core\planner_agent.py

### Classes
- PlannerAgent

### Functions
- __init__
- select_strategy
- create_plan

### Imports
- core.cognitive_memory

---

## core\planner_agent_backup_v01.py

### Classes
- PlannerAgent

### Functions
- __init__
- create_plan

### Imports
- None

---

## core\planner_agent_backup_v02.py

### Classes
- PlannerAgent

### Functions
- __init__
- create_plan

### Imports
- None

---

## core\planner_agent_backup_v03.py

### Classes
- PlannerAgent

### Functions
- __init__
- create_plan

### Imports
- core.cognitive_memory

---

## core\planner_agent_backup_v04.py

### Classes
- PlannerAgent

### Functions
- __init__
- create_plan

### Imports
- core.cognitive_memory

---

## core\plugin_organizer.py

### Classes
- PluginOrganizer

### Functions
- __init__
- register
- get
- list_plugins

### Imports
- None

---

## core\pulse.py

### Classes
- Pulse

### Functions
- __init__
- run

### Imports
- core.attention_router
- core.pulse_orchestrator_V3

---

## core\pulse_CONTROLLER_V05_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- agents.synthesis_agent
- agents.verifier_agent
- core.left_brain
- core.pulse_router
- core.right_brain

---

## core\pulse_cycle.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

---

## core\pulse_cycle_before_feedback_connection.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

---

## core\pulse_cycle_before_feedback_interpreter.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

---

## core\pulse_cycle_before_ooda.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.pulse_router

---

## core\pulse_cycle_before_ooda_router.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

---

## core\pulse_cycle_ooda_act_working.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

---

## core\pulse_cycle_ooda_working.py

### Classes
- None

### Functions
- clean_agent_result
- run_pulse
- run_targeted_cycle

### Imports
- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

---

## core\pulse_engine.py

### Classes
- None

### Functions
- None

### Imports
- None

---

## core\pulse_intelligence_router.py

### Classes
- PulseIntelligenceRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\pulse_intelligence_router_before_v2_fix.py

### Classes
- PulseIntelligenceRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\pulse_intelligence_router_checkpoint.py

### Classes
- PulseIntelligenceRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\pulse_intelligence_router_WORKING_FULL_PULSE.py

### Classes
- PulseIntelligenceRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\pulse_orchestrator.py

### Classes
- PulseOrchestrator

### Functions
- __init__
- run_pulse

### Imports
- core.pulse_orchestrator_V3

---

## core\pulse_orchestrator_FOUNDATION_V1.py

### Classes
- PulseOrchestrator

### Functions
- __init__
- run_pulse

### Imports
- None

---

## core\pulse_orchestrator_V2_WORKING.py

### Classes
- PulseOrchestrator

### Functions
- __init__
- run_pulse

### Imports
- None

---

## core\pulse_orchestrator_V3.py

### Classes
- PulseOrchestrator

### Functions
- __init__
- decide_execution
- execute

### Imports
- core.module_registry_setup

---

## core\pulse_orchestrator_V3_BACKUP.py

### Classes
- PulseOrchestrator

### Functions
- __init__
- decide_execution

### Imports
- None

---

## core\pulse_orchestrator_V4_REGISTRY_BACKUP.py

### Classes
- PulseOrchestrator

### Functions
- __init__
- decide_execution
- execute

### Imports
- core.module_registry_setup

---

## core\pulse_router.py

### Classes
- PulseRouter

### Functions
- __init__
- decide
- route

### Imports
- None

---

## core\pulse_router_before_ooda.py

### Classes
- PulseRouter

### Functions
- __init__
- decide

### Imports
- None

---

## core\pulse_router_before_v2_fix.py

### Classes
- PulseRouter

### Functions
- __init__
- decide

### Imports
- None

---

## core\pulse_SELECTIVE_ACTIVATION_CONNECTED_V1.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.attention_router
- core.left_brain
- core.pulse_router
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V05_WORKING_AFTER_FIX.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.left_brain
- core.pulse_router
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V05_WORKING_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.attention_router
- core.cognitive_memory
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V06_MEMORY_CONNECTED_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.attention_router
- core.cognitive_memory
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V07_COGNITIVE_EFFORT_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V08_ADAPTIVE_EFFORT_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V09_EFFORT_ACTIVATION_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V10_ORCHESTRATOR_CONNECTED_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_orchestrator_V3
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V12_DYNAMIC_EXECUTION_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_orchestrator_V3
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V13_ORCHESTRATOR_CONNECTED.py

### Classes
- PulseController

### Functions
- __init__
- run
- summarize_execution

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_orchestrator
- core.pulse_orchestrator_V3
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V13_ORCHESTRATOR_CONNECTED_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_orchestrator
- core.pulse_orchestrator_V3
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V13_ORCHESTRATOR_TEST.py

### Classes
- PulseController

### Functions
- __init__
- run

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_orchestrator
- core.pulse_orchestrator_V3
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\pulse_V13_SUMMARY_BACKUP.py

### Classes
- PulseController

### Functions
- __init__
- run
- summarize_execution

### Imports
- core.adaptive_effort_controller
- core.attention_router
- core.cognitive_effort_controller
- core.cognitive_memory
- core.effort_activation_map
- core.learning_extractor
- core.left_brain
- core.pulse_orchestrator
- core.pulse_orchestrator_V3
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

---

## core\reflection_agent.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- core.cognitive_memory

---

## core\reflection_agent_BEFORE_MEMORY_LINK.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- None

---

## core\reflection_agent_DUPLICATE_FILTER_V1.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- core.cognitive_memory

---

## core\reflection_agent_IMPORTANCE_READY_V1.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- core.cognitive_memory

---

## core\reflection_agent_LEARNING_LOOP_V1.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- core.cognitive_memory

---

## core\reflection_agent_MEMORY_LOOP_V1.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- core.cognitive_memory

---

## core\reflection_agent_REINFORCEMENT_CONFIRMED_V1.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- core.cognitive_memory

---

## core\reflection_agent_V1_STABLE.py

### Classes
- ReflectionAgent

### Functions
- __init__
- reflect

### Imports
- None

---

## core\reflection_loop.py

### Classes
- ReflectionLoop

### Functions
- __init__
- reflect

### Imports
- agents.learning_agent
- agents.memory_agent
- agents.optimizer_agent
- core.improvement_memory

---

## core\research_agent.py

### Classes
- ResearchAgent

### Functions
- __init__
- research

### Imports
- core.message_bus

---

## core\research_agent_checkpoint_v01.py

### Classes
- ResearchAgent

### Functions
- __init__
- research

### Imports
- core.message_bus

---

## core\right_brain.py

### Classes
- RightBrain

### Functions
- __init__
- apply_learned_reasoning
- build_memory_context
- build_prompt
- think
- create
- analyse
- analyze

### Imports
- core.llm_interface
- core.memory_consolidator

---

## core\right_brain_backup_v01.py

### Classes
- RightBrain

### Functions
- __init__
- think

### Imports
- core.cognitive_message
- core.llm_interface

---

## core\right_brain_checkpoint_v01.py

### Classes
- RightBrain

### Functions
- __init__
- process
- create
- analyse
- analyze

### Imports
- None

---

## core\right_brain_MEMORY_V1.py

### Classes
- RightBrain

### Functions
- __init__
- apply_learned_reasoning
- think
- create
- analyse
- analyze

### Imports
- core.memory_consolidator

---

## core\right_brain_V20_STABLE.py

### Classes
- RightBrain

### Functions
- __init__
- process
- create
- analyse
- analyze
- think

### Imports
- None

---

## core\right_cognitive_engine.py

### Classes
- RightCognitiveEngine

### Functions
- __init__
- imagine

### Imports
- None

---

## core\right_cognitive_engine_checkpoint.py

### Classes
- RightCognitiveEngine

### Functions
- __init__
- imagine

### Imports
- None

---

## core\router.py

### Classes
- Router

### Functions
- __init__
- route

### Imports
- None

---

## core\scs.py

### Classes
- SCS

### Functions
- __init__
- think

### Imports
- agents.synthesis_agent
- agents.verifier_agent
- core.left_brain
- core.right_brain

---

## core\scs_adaptive_controller.py

### Classes
- SCSAdaptiveController

### Functions
- __init__
- process

### Imports
- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.pulse_intelligence_router
- core.strategy_evolution_engine

---

## core\scs_adaptive_controller_checkpoint.py

### Classes
- SCSAdaptiveController

### Functions
- __init__
- process

### Imports
- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.pulse_intelligence_router
- core.strategy_evolution_engine

---

## core\scs_executive.py

### Classes
- SCSExecutive

### Functions
- __init__
- process

### Imports
- core.decision_engine
- core.learning_coordinator
- core.ooda_loop

---

## core\scs_executive_checkpoint.py

### Classes
- SCSExecutive

### Functions
- __init__
- process

### Imports
- core.learning_coordinator
- core.ooda_loop

---

## core\scs_master_controller.py

### Classes
- SCSMasterController

### Functions
- __init__
- process

### Imports
- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.strategy_evolution_engine

---

## core\scs_master_controller_checkpoint.py

### Classes
- SCSMasterController

### Functions
- __init__
- process

### Imports
- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.strategy_evolution_engine

---

## core\selective_activation_engine.py

### Classes
- SelectiveActivationEngine

### Functions
- __init__
- activate

### Imports
- None

---

## core\selective_activation_engine_checkpoint.py

### Classes
- SelectiveActivationEngine

### Functions
- __init__
- activate

### Imports
- None

---

## core\selective_activation_engine_FOUNDATION_V1.py

### Classes
- SelectiveActivationEngine

### Functions
- __init__
- activate

### Imports
- None

---

## core\selective_pulse_engine.py

### Classes
- SelectivePulseEngine

### Functions
- __init__
- select_modules
- run

### Imports
- core.cognitive_memory
- core.decision_engine
- core.learning_feedback
- core.left_brain
- core.right_brain
- core.synthesis_engine
- core.verifier_engine
- datetime
- uuid

---

## core\selective_pulse_engine_checkpoint.py

### Classes
- SelectivePulseEngine

### Functions
- __init__
- run

### Imports
- core.left_cognitive_engine
- core.right_cognitive_engine
- core.synthesis_engine
- core.verifier_engine

---

## core\selective_pulse_engine_FOUNDATION_V1.py

### Classes
- SelectivePulseEngine

### Functions
- __init__
- run

### Imports
- core.cognitive_memory
- core.decision_engine
- core.learning_feedback
- core.left_brain
- core.right_brain
- core.synthesis_engine
- core.verifier_engine
- datetime
- uuid

---

## core\self_managing_scs.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.selective_pulse_engine

---

## core\self_managing_scs_before_orchestrator_fix.py

Error reading file: unexpected indent (<unknown>, line 42)

## core\self_managing_scs_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_experience_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_feedback_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_feedback_complete_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_feedback_engine
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_goal_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_performance_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_feedback_engine
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_strategy_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\self_managing_scs_strategy_evolution_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_performance_memory
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_feedback_engine
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine
- core.strategy_evolution_engine

---

## core\self_managing_scs_v1_checkpoint.py

### Classes
- SelfManagingSCS

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.pulse_intelligence_router
- core.selective_pulse_engine

---

## core\skill_manager.py

### Classes
- SkillManager

### Functions
- __init__
- add_skill
- find_agents
- list_skills

### Imports
- None

---

## core\skill_organizer.py

### Classes
- SkillOrganizer

### Functions
- __init__
- register
- get
- list_skills

### Imports
- None

---

## core\strategy_evolution_engine.py

### Classes
- StrategyEvolutionEngine

### Functions
- __init__
- evaluate_strategy
- choose_best_strategy

### Imports
- None

---

## core\strategy_evolution_engine_checkpoint.py

### Classes
- StrategyEvolutionEngine

### Functions
- __init__
- evaluate_strategy
- choose_best_strategy

### Imports
- None

---

## core\strategy_optimizer.py

### Classes
- StrategyOptimizer

### Functions
- __init__
- optimize

### Imports
- None

---

## core\strategy_optimizer_checkpoint.py

### Classes
- StrategyOptimizer

### Functions
- __init__
- optimize

### Imports
- None

---

## core\synthesis_agent.py

### Classes
- SynthesisAgent

### Functions
- __init__
- build_prompt
- synthesize

### Imports
- core.llm_interface
- core.memory_consolidator

---

## core\synthesis_agent_LEARNED_REASONING_CONNECTED_V1.py

### Classes
- SynthesisAgent

### Functions
- __init__
- synthesize

### Imports
- None

---

## core\synthesis_agent_PRIORITY_MEMORY_V1.py

### Classes
- SynthesisAgent

### Functions
- __init__
- synthesize

### Imports
- core.memory_consolidator

---

## core\synthesis_agent_V20_STABLE.py

### Classes
- SynthesisAgent

### Functions
- __init__
- synthesize

### Imports
- None

---

## core\synthesis_engine.py

### Classes
- SynthesisEngine

### Functions
- __init__
- combine

### Imports
- core.synthesis_agent

---

## core\synthesis_engine_before_llm_upgrade.py

### Classes
- SynthesisEngine

### Functions
- __init__
- combine

### Imports
- None

---

## core\thinking_loop.py

### Classes
- ThinkingLoop

### Functions
- __init__
- think

### Imports
- agents.memory_agent
- core.attention_manager
- core.branch_manager
- core.cognitive_controller
- core.coordinator
- core.executive_manager
- core.neural_tree_executor
- core.tree_router

---

## core\tree_router.py

### Classes
- TreeRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\tree_router_backup_v01.py

### Classes
- TreeRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\tree_router_backup_v02.py

### Classes
- TreeRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\tree_router_v01_backup.py

### Classes
- TreeRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\tree_router_v02_working_backup.py

### Classes
- TreeRouter

### Functions
- __init__
- route

### Imports
- None

---

## core\unified_scs_pulse.py

### Classes
- UnifiedSCSPulse

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.pulse_intelligence_router
- core.selective_pulse_engine
- core.strategy_evolution_engine

---

## core\unified_scs_pulse_checkpoint.py

### Classes
- UnifiedSCSPulse

### Functions
- __init__
- think

### Imports
- core.adaptive_learning_loop
- core.pulse_intelligence_router
- core.selective_pulse_engine
- core.strategy_evolution_engine

---

## core\verifier_engine.py

### Classes
- VerifierEngine

### Functions
- __init__
- verify

### Imports
- None

---

## core\verifier_engine_BACKUP_BEFORE_V2.py

### Classes
- VerifierEngine

### Functions
- __init__
- verify

### Imports
- core.message_bus

---

## core\verifier_engine_checkpoint.py

### Classes
- VerifierEngine

### Functions
- __init__
- verify

### Imports
- None

---

## core\verifier_engine_checkpoint_v01.py

### Classes
- VerifierEngine

### Functions
- __init__
- verify

### Imports
- None

---

## core\verifier_engine_FULL_LOOP_V1.py

### Classes
- VerifierEngine

### Functions
- __init__
- verify

### Imports
- None

---

## core\verifier_engine_PRE_REFLECTION_BACKUP.py

### Classes
- VerifierEngine

### Functions
- __init__
- verify

### Imports
- None

---

## agents\analysis_agent.py

### Classes
- AnalysisAgent

### Functions
- __init__
- run

### Imports
- None

---

## agents\evaluation_agent.py

### Classes
- EvaluationAgent

### Functions
- __init__
- evaluate

### Imports
- None

---

## agents\learning_agent.py

### Classes
- LearningAgent

### Functions
- __init__
- learn

### Imports
- None

---

## agents\memory_agent.py

### Classes
- MemoryAgent

### Functions
- __init__
- load_memory
- save_memory
- recall_memories

### Imports
- json
- os

---

## agents\optimizer_agent.py

### Classes
- OptimizerAgent

### Functions
- __init__
- optimize

### Imports
- None

---

## agents\organizer.py

### Classes
- AgentOrganizer

### Functions
- __init__
- register
- list_agents

### Imports
- None

---

## agents\planning_agent.py

### Classes
- PlanningAgent

### Functions
- __init__
- run

### Imports
- None

---

## agents\research_agent.py

### Classes
- ResearchAgent

### Functions
- __init__
- run

### Imports
- core.left_brain
- plugins.search
- plugins.web_browser

---

## agents\right_brain.py

### Classes
- RightBrainAgent

### Functions
- __init__
- run

### Imports
- None

---

## agents\synthesis_agent.py

### Classes
- SynthesisAgent

### Functions
- __init__
- synthesize

### Imports
- None

---

## agents\verifier_agent.py

### Classes
- VerifierAgent

### Functions
- __init__
- check

### Imports
- core.llm_interface

---

## agents\verifier_agent_BACKUP.py

### Classes
- VerifierAgent

### Functions
- __init__
- check

### Imports
- core.cognitive_message
- core.llm_interface

---

## plugins\organizer.py

### Classes
- PluginOrganizer

### Functions
- __init__
- register
- list_plugins

### Imports
- None

---

## plugins\search.py

### Classes
- Search

### Functions
- __init__
- _clean_url
- search

### Imports
- bs4
- requests
- urllib.parse

---

## plugins\web_browser.py

### Classes
- WebBrowser

### Functions
- __init__
- fetch

### Imports
- requests

---

## dashboard\app.py

### Classes
- None

### Functions
- home
- process

### Imports
- core.coordinator
- flask
- os
- sys

---

## dashboard\app_backup.py

### Classes
- Wrapper

### Functions
- home
- __init__

### Imports
- core.orchestrated_scs_v2
- flask
- os
- sys

---

## dashboard\app_backup_before_fix.py

### Classes
- Wrapper

### Functions
- home
- __init__

### Imports
- core.orchestrated_scs_v2
- flask
- os
- sys

---

## dashboard\app_backup_working.py

### Classes
- Wrapper

### Functions
- home
- __init__

### Imports
- core.orchestrated_scs_v2
- flask
- os
- sys

---

## dashboard\app_darrel_backup.py

### Classes
- Wrapper

### Functions
- home
- __init__

### Imports
- core.orchestrated_scs_v2
- flask
- os
- sys

---

## dashboard\app_v02_checkpoint.py

### Classes
- None

### Functions
- home
- think
- status

### Imports
- core.orchestrated_scs_v2
- flask
- os
- sys

---

## dashboard\app_v04_checkpoint.py

### Classes
- None

### Functions
- home
- think
- status

### Imports
- core.orchestrated_scs_v2
- flask
- os
- sys

---

