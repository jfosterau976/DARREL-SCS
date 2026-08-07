# Dependency Map

## core\__init__.py

- No imports

## core\adaptive_decision_test.py

- core.decision_feedback_bridge

## core\adaptive_effort_controller.py

- No imports

## core\adaptive_learning_loop.py

- core.cognitive_memory

## core\adaptive_learning_loop_checkpoint.py

- core.cognitive_memory

## core\adaptive_loop_test.py

- core.decision_feedback_bridge
- core.ooda_loop

## core\agent_context.py

- core.communication_bus

## core\agent_message_router.py

- core.communication_bus

## core\agent_organizer.py

- No imports

## core\agent_registry.py

- No imports

## core\attention_manager.py

- No imports

## core\attention_manager_FOUNDATION_V1.py

- No imports

## core\attention_router.py

- core.attention_manager
- core.cognitive_memory
- core.selective_activation_engine

## core\attention_router_V01_WORKING_BACKUP.py

- core.attention_manager
- core.selective_activation_engine

## core\attention_router_V1_WORKING.py

- core.attention_manager
- core.selective_activation_engine

## core\branch_manager.py

- No imports

## core\branch_manager_v01_backup.py

- No imports

## core\branch_manager_v02_working.py

- No imports

## core\cognitive_controller.py

- core.coordinator
- core.executive_manager
- core.improvement_memory

## core\cognitive_controller_v01_backup.py

- core.coordinator
- core.executive_manager
- core.improvement_memory

## core\cognitive_effort_controller.py

- No imports

## core\cognitive_memory.py

- json
- os

## core\cognitive_memory_backup_v01.py

- json
- os

## core\cognitive_memory_backup_v02.py

- json
- os

## core\cognitive_memory_backup_v03.py

- json
- os

## core\cognitive_memory_checkpoint.py

- json
- os

## core\cognitive_memory_CLEAN_WITH_SEARCH_V1.py

- json
- os

## core\cognitive_memory_DEDUP_V1.py

- json
- os

## core\cognitive_memory_IMPORTANCE_V1.py

- json
- os

## core\cognitive_memory_MEMORY_SEARCH_V1.py

- json
- os

## core\cognitive_memory_STABLE_MEMORY_V1.py

- json
- os

## core\cognitive_memory_STRENGTHENING_V1.py

- json
- os

## core\cognitive_memory_V20_STABLE.py

- json
- os

## core\cognitive_memory_WORKING_BACKUP.py

- json
- os

## core\cognitive_message.py

- No imports

## core\cognitive_orchestrator.py

- No imports

## core\cognitive_orchestrator_checkpoint.py

- No imports

## core\cognitive_output_formatter.py

- No imports

## core\cognitive_performance_memory.py

- No imports

## core\cognitive_performance_memory_checkpoint.py

- No imports

## core\cognitive_performance_monitor.py

- No imports

## core\cognitive_performance_monitor_checkpoint.py

- No imports

## core\cognitive_pipeline.py

- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.research_agent
- core.tree_router
- core.verifier_engine

## core\cognitive_pipeline_backup_v01.py

- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.tree_router

## core\cognitive_pipeline_backup_v02.py

- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.synthesis_agent
- core.tree_router

## core\cognitive_pipeline_backup_v03.py

- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.synthesis_agent
- core.tree_router

## core\cognitive_pipeline_backup_v04.py

- core.attention_manager
- core.branch_manager
- core.cognitive_memory
- core.coordinator
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

## core\cognitive_pipeline_checkpoint_v01.py

- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

## core\cognitive_pipeline_checkpoint_v02.py

- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

## core\cognitive_pipeline_checkpoint_v03.py

- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.tree_router

## core\cognitive_pipeline_checkpoint_v04.py

- core.branch_manager
- core.learning_feedback
- core.neural_tree_executor
- core.planner_agent
- core.research_agent
- core.tree_router
- core.verifier_engine

## core\cognitive_pulse_controller.py

- core.attention_router
- core.pulse
- core.pulse_orchestrator

## core\cognitive_pulse_v1.py

- core.left_cognitive_engine
- core.right_cognitive_engine
- core.synthesis_engine
- core.verifier_engine

## core\cognitive_pulse_v1_checkpoint.py

- core.left_cognitive_engine
- core.right_cognitive_engine
- core.synthesis_engine
- core.verifier_engine

## core\cognitive_regulation_engine.py

- No imports

## core\cognitive_state_manager.py

- No imports

## core\communication_bus.py

- No imports

## core\context_manager.py

- No imports

## core\coordinator.py

- core.learning_feedback
- core.memory_consolidator
- core.pulse
- core.reflection_agent
- core.scs_executive
- datetime
- time

## core\coordinator_BACKUP.py

- agents.synthesis_agent
- agents.verifier_agent
- core.left_brain
- core.persistent_memory
- core.right_brain

## core\coordinator_backup_v01.py

- core.left_brain
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_COGNITIVE_LOOP_V1.py

- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_DUAL_MEMORY_V1.py

- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_FULL_COGNITION_V1.py

- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_LEARNED_REASONING_CONNECTED_V1.py

- core.left_brain
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_LEARNING_LOOP_CONNECTED_BACKUP.py

- core.learning_feedback
- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_LEFT_MEMORY_V1.py

- core.left_brain
- core.memory_consolidator
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\coordinator_REFLECTION_LOOP_V1.py

- core.left_brain
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\decision_engine.py

- No imports

## core\decision_feedback_bridge.py

- core.feedback_controller

## core\decision_router.py

- No imports

## core\effort_activation_map.py

- No imports

## core\executive_manager.py

- No imports

## core\experience_loop_checkpoint.py

- core.cognitive_memory
- core.learning_coordinator

## core\experience_loop_test.py

- core.cognitive_memory
- core.learning_coordinator

## core\experience_replay_engine.py

- No imports

## core\experience_replay_engine_checkpoint.py

- No imports

## core\experience_strategy_selector.py

- No imports

## core\experience_strategy_selector_checkpoint.py

- No imports

## core\feedback_connection_test.py

- core.feedback_interpreter

## core\feedback_controller.py

- core.feedback_interpreter

## core\feedback_interpreter.py

- No imports

## core\full_cognitive_pulse_checkpoint.py

- core.pulse_orchestrator
- core.scs_executive

## core\full_cognitive_pulse_test.py

- core.pulse_orchestrator
- core.scs_executive

## core\goal_feedback_engine.py

- No imports

## core\goal_planning_engine.py

- No imports

## core\goal_planning_engine_checkpoint.py

- No imports

## core\improvement_memory.py

- datetime
- json
- os

## core\learning_coordinator.py

- core.cognitive_memory

## core\learning_coordinator_checkpoint.py

- core.memory_gate

## core\learning_extractor.py

- datetime

## core\learning_feedback.py

- core.cognitive_memory

## core\learning_feedback_BACKUP_BEFORE_V2.py

- core.cognitive_memory

## core\learning_feedback_backup_v01.py

- No imports

## core\learning_feedback_backup_v02.py

- No imports

## core\left_brain.py

- core.llm_interface
- core.memory_consolidator

## core\left_brain_ADAPTIVE_REASONING_CONNECTED_V1.py

- core.memory_consolidator

## core\left_brain_BEFORE_ADAPTIVE_REASONING_V1.py

- core.memory_consolidator

## core\left_brain_checkpoint_v01.py

- No imports

## core\left_brain_LEARNED_CONTEXT_V1.py

- core.memory_consolidator

## core\left_brain_REASONING_CONTEXT_V1.py

- core.memory_consolidator

## core\left_brain_V20_STABLE.py

- No imports

## core\left_brain_V21_backup.py

- No imports

## core\left_cognitive_engine.py

- No imports

## core\left_cognitive_engine_checkpoint.py

- No imports

## core\llm_interface.py

- json
- os
- urllib.error
- urllib.request

## core\llm_interface_backup.py

Error: invalid syntax (<unknown>, line 90)

## core\memory.py

- No imports

## core\memory_advisor.py

- core.memory_retriever

## core\memory_advisor_checkpoint.py

- core.memory_retriever

## core\memory_agent.py

- No imports

## core\memory_consolidator.py

- core.cognitive_memory

## core\memory_consolidator_BEFORE_REASONING_V1.py

- core.cognitive_memory

## core\memory_consolidator_PRIORITY_V1.py

- core.cognitive_memory

## core\memory_consolidator_PRIORITY_V2.py

- core.cognitive_memory

## core\memory_consolidator_REASONING_CONNECTED_V1.py

- core.cognitive_memory

## core\memory_consolidator_V2_BACKUP.py

- core.cognitive_memory

## core\memory_consolidator_V2_STABLE.py

- core.cognitive_memory

## core\memory_gate.py

- core.memory_advisor

## core\memory_gate_checkpoint.py

- core.memory_advisor

## core\memory_optimizer.py

- json
- os

## core\memory_retriever.py

- core.cognitive_memory

## core\memory_retriever_checkpoint.py

- core.cognitive_memory

## core\message_bus.py

- json
- os

## core\message_bus_backup_v01.py

- No imports

## core\message_bus_checkpoint_v02.py

- No imports

## core\message_bus_checkpoint_v03.py

- No imports

## core\module_registry.py

- No imports

## core\module_registry_setup.py

- core.goal_planning_engine
- core.learning_extractor
- core.left_brain
- core.module_registry
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\neural_tree_executor.py

- core.message_bus

## core\neural_tree_executor_backup.py

- No imports

## core\neural_tree_executor_backup_v01.py

- core.message_bus

## core\neural_tree_executor_backup_v02.py

- No imports

## core\neural_tree_executor_checkpoint_v01.py

- core.message_bus

## core\neural_tree_executor_v02_backup.py

- No imports

## core\neural_tree_executor_v02_working.py

- No imports

## core\neural_tree_executor_v03_backup.py

- core.agent_message_router

## core\neural_tree_manager.py

- No imports

## core\ooda_loop.py

- No imports

## core\ooda_loop_before_adaptive_decide.py

- No imports

## core\ooda_loop_before_self_adaptive.py

- No imports

## core\ooda_loop_before_smart_decide.py

- No imports

## core\ooda_loop_V02_adaptive_checkpoint.py

- No imports

## core\orchestrated_scs.py

- core.cognitive_orchestrator
- core.self_managing_scs

## core\orchestrated_scs_checkpoint.py

- core.cognitive_orchestrator
- core.self_managing_scs

## core\orchestrated_scs_v2.py

- core.self_managing_scs

## core\orchestrated_scs_v2_BACKUP.py

Error: '(' was never closed (<unknown>, line 24)

## core\orchestrated_scs_v2_broken_backup.py

- core.cognitive_orchestrator
- core.left_brain
- core.right_brain
- core.selective_activation_engine
- core.self_managing_scs
- core.synthesis_engine
- core.verifier_engine

## core\orchestrated_scs_v2_checkpoint.py

- core.cognitive_orchestrator
- core.selective_activation_engine
- core.self_managing_scs

## core\orchestrated_scs_v2_V20_STABLE.py

- core.cognitive_orchestrator
- core.left_brain
- core.right_brain
- core.selective_activation_engine
- core.self_managing_scs
- core.synthesis_engine
- core.verifier_engine

## core\persistent_memory.py

- json
- pathlib

## core\planner_agent.py

- core.cognitive_memory

## core\planner_agent_backup_v01.py

- No imports

## core\planner_agent_backup_v02.py

- No imports

## core\planner_agent_backup_v03.py

- core.cognitive_memory

## core\planner_agent_backup_v04.py

- core.cognitive_memory

## core\plugin_organizer.py

- No imports

## core\pulse.py

- core.attention_router
- core.pulse_orchestrator_V3

## core\pulse_CONTROLLER_V05_BACKUP.py

- agents.synthesis_agent
- agents.verifier_agent
- core.left_brain
- core.pulse_router
- core.right_brain

## core\pulse_cycle.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

## core\pulse_cycle_before_feedback_connection.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

## core\pulse_cycle_before_feedback_interpreter.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

## core\pulse_cycle_before_ooda.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.pulse_router

## core\pulse_cycle_before_ooda_router.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

## core\pulse_cycle_ooda_act_working.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

## core\pulse_cycle_ooda_working.py

- agents.analysis_agent
- agents.right_brain
- agents.synthesis_agent
- agents.verifier_agent
- core.ooda_loop
- core.pulse_router

## core\pulse_engine.py

- No imports

## core\pulse_intelligence_router.py

- No imports

## core\pulse_intelligence_router_before_v2_fix.py

- No imports

## core\pulse_intelligence_router_checkpoint.py

- No imports

## core\pulse_intelligence_router_WORKING_FULL_PULSE.py

- No imports

## core\pulse_orchestrator.py

- core.pulse_orchestrator_V3

## core\pulse_orchestrator_FOUNDATION_V1.py

- No imports

## core\pulse_orchestrator_V2_WORKING.py

- No imports

## core\pulse_orchestrator_V3.py

- core.module_registry_setup

## core\pulse_orchestrator_V3_BACKUP.py

- No imports

## core\pulse_orchestrator_V4_REGISTRY_BACKUP.py

- core.module_registry_setup

## core\pulse_router.py

- No imports

## core\pulse_router_before_ooda.py

- No imports

## core\pulse_router_before_v2_fix.py

- No imports

## core\pulse_SELECTIVE_ACTIVATION_CONNECTED_V1.py

- core.attention_router
- core.left_brain
- core.pulse_router
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\pulse_V05_WORKING_AFTER_FIX.py

- core.left_brain
- core.pulse_router
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\pulse_V05_WORKING_BACKUP.py

- core.attention_router
- core.cognitive_memory
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\pulse_V06_MEMORY_CONNECTED_BACKUP.py

- core.attention_router
- core.cognitive_memory
- core.learning_extractor
- core.left_brain
- core.pulse_router
- core.reflection_agent
- core.right_brain
- core.synthesis_agent
- core.verifier_engine

## core\pulse_V07_COGNITIVE_EFFORT_BACKUP.py

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

## core\pulse_V08_ADAPTIVE_EFFORT_BACKUP.py

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

## core\pulse_V09_EFFORT_ACTIVATION_BACKUP.py

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

## core\pulse_V10_ORCHESTRATOR_CONNECTED_BACKUP.py

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

## core\pulse_V12_DYNAMIC_EXECUTION_BACKUP.py

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

## core\pulse_V13_ORCHESTRATOR_CONNECTED.py

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

## core\pulse_V13_ORCHESTRATOR_CONNECTED_BACKUP.py

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

## core\pulse_V13_ORCHESTRATOR_TEST.py

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

## core\pulse_V13_SUMMARY_BACKUP.py

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

## core\reflection_agent.py

- core.cognitive_memory

## core\reflection_agent_BEFORE_MEMORY_LINK.py

- No imports

## core\reflection_agent_DUPLICATE_FILTER_V1.py

- core.cognitive_memory

## core\reflection_agent_IMPORTANCE_READY_V1.py

- core.cognitive_memory

## core\reflection_agent_LEARNING_LOOP_V1.py

- core.cognitive_memory

## core\reflection_agent_MEMORY_LOOP_V1.py

- core.cognitive_memory

## core\reflection_agent_REINFORCEMENT_CONFIRMED_V1.py

- core.cognitive_memory

## core\reflection_agent_V1_STABLE.py

- No imports

## core\reflection_loop.py

- agents.learning_agent
- agents.memory_agent
- agents.optimizer_agent
- core.improvement_memory

## core\research_agent.py

- core.message_bus

## core\research_agent_checkpoint_v01.py

- core.message_bus

## core\right_brain.py

- core.llm_interface
- core.memory_consolidator

## core\right_brain_backup_v01.py

- core.cognitive_message
- core.llm_interface

## core\right_brain_checkpoint_v01.py

- No imports

## core\right_brain_MEMORY_V1.py

- core.memory_consolidator

## core\right_brain_V20_STABLE.py

- No imports

## core\right_cognitive_engine.py

- No imports

## core\right_cognitive_engine_checkpoint.py

- No imports

## core\router.py

- No imports

## core\scs.py

- agents.synthesis_agent
- agents.verifier_agent
- core.left_brain
- core.right_brain

## core\scs_adaptive_controller.py

- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.pulse_intelligence_router
- core.strategy_evolution_engine

## core\scs_adaptive_controller_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.pulse_intelligence_router
- core.strategy_evolution_engine

## core\scs_executive.py

- core.decision_engine
- core.learning_coordinator
- core.ooda_loop

## core\scs_executive_checkpoint.py

- core.learning_coordinator
- core.ooda_loop

## core\scs_master_controller.py

- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.strategy_evolution_engine

## core\scs_master_controller_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_pulse_v1
- core.strategy_evolution_engine

## core\selective_activation_engine.py

- No imports

## core\selective_activation_engine_checkpoint.py

- No imports

## core\selective_activation_engine_FOUNDATION_V1.py

- No imports

## core\selective_pulse_engine.py

- core.cognitive_memory
- core.decision_engine
- core.learning_feedback
- core.left_brain
- core.right_brain
- core.synthesis_engine
- core.verifier_engine
- datetime
- uuid

## core\selective_pulse_engine_checkpoint.py

- core.left_cognitive_engine
- core.right_cognitive_engine
- core.synthesis_engine
- core.verifier_engine

## core\selective_pulse_engine_FOUNDATION_V1.py

- core.cognitive_memory
- core.decision_engine
- core.learning_feedback
- core.left_brain
- core.right_brain
- core.synthesis_engine
- core.verifier_engine
- datetime
- uuid

## core\self_managing_scs.py

- core.selective_pulse_engine

## core\self_managing_scs_before_orchestrator_fix.py

Error: unexpected indent (<unknown>, line 42)

## core\self_managing_scs_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_experience_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_feedback_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_feedback_complete_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_feedback_engine
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_goal_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_performance_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.goal_feedback_engine
- core.goal_planning_engine
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_strategy_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.experience_replay_engine
- core.experience_strategy_selector
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\self_managing_scs_strategy_evolution_checkpoint.py

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

## core\self_managing_scs_v1_checkpoint.py

- core.adaptive_learning_loop
- core.cognitive_regulation_engine
- core.cognitive_state_manager
- core.pulse_intelligence_router
- core.selective_pulse_engine

## core\skill_manager.py

- No imports

## core\skill_organizer.py

- No imports

## core\strategy_evolution_engine.py

- No imports

## core\strategy_evolution_engine_checkpoint.py

- No imports

## core\strategy_optimizer.py

- No imports

## core\strategy_optimizer_checkpoint.py

- No imports

## core\synthesis_agent.py

- core.llm_interface
- core.memory_consolidator

## core\synthesis_agent_LEARNED_REASONING_CONNECTED_V1.py

- No imports

## core\synthesis_agent_PRIORITY_MEMORY_V1.py

- core.memory_consolidator

## core\synthesis_agent_V20_STABLE.py

- No imports

## core\synthesis_engine.py

- core.synthesis_agent

## core\synthesis_engine_before_llm_upgrade.py

- No imports

## core\thinking_loop.py

- agents.memory_agent
- core.attention_manager
- core.branch_manager
- core.cognitive_controller
- core.coordinator
- core.executive_manager
- core.neural_tree_executor
- core.tree_router

## core\tree_router.py

- No imports

## core\tree_router_backup_v01.py

- No imports

## core\tree_router_backup_v02.py

- No imports

## core\tree_router_v01_backup.py

- No imports

## core\tree_router_v02_working_backup.py

- No imports

## core\unified_scs_pulse.py

- core.adaptive_learning_loop
- core.pulse_intelligence_router
- core.selective_pulse_engine
- core.strategy_evolution_engine

## core\unified_scs_pulse_checkpoint.py

- core.adaptive_learning_loop
- core.pulse_intelligence_router
- core.selective_pulse_engine
- core.strategy_evolution_engine

## core\verifier_engine.py

- No imports

## core\verifier_engine_BACKUP_BEFORE_V2.py

- core.message_bus

## core\verifier_engine_checkpoint.py

- No imports

## core\verifier_engine_checkpoint_v01.py

- No imports

## core\verifier_engine_FULL_LOOP_V1.py

- No imports

## core\verifier_engine_PRE_REFLECTION_BACKUP.py

- No imports

## agents\analysis_agent.py

- No imports

## agents\evaluation_agent.py

- No imports

## agents\learning_agent.py

- No imports

## agents\memory_agent.py

- json
- os

## agents\optimizer_agent.py

- No imports

## agents\organizer.py

- No imports

## agents\planning_agent.py

- No imports

## agents\research_agent.py

- core.left_brain
- plugins.search
- plugins.web_browser

## agents\right_brain.py

- No imports

## agents\synthesis_agent.py

- No imports

## agents\verifier_agent.py

- core.llm_interface

## agents\verifier_agent_BACKUP.py

- core.cognitive_message
- core.llm_interface

## plugins\organizer.py

- No imports

## plugins\search.py

- bs4
- requests
- urllib.parse

## plugins\web_browser.py

- requests

## dashboard\app.py

- core.coordinator
- flask
- os
- sys

## dashboard\app_backup.py

- core.orchestrated_scs_v2
- flask
- os
- sys

## dashboard\app_backup_before_fix.py

- core.orchestrated_scs_v2
- flask
- os
- sys

## dashboard\app_backup_working.py

- core.orchestrated_scs_v2
- flask
- os
- sys

## dashboard\app_darrel_backup.py

- core.orchestrated_scs_v2
- flask
- os
- sys

## dashboard\app_v02_checkpoint.py

- core.orchestrated_scs_v2
- flask
- os
- sys

## dashboard\app_v04_checkpoint.py

- core.orchestrated_scs_v2
- flask
- os
- sys

