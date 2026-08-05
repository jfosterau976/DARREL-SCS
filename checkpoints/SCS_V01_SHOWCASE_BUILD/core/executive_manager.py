class ExecutiveManager:

    def __init__(self):
        self.name = "SCS Executive Manager"
        self.role = "decision_control"


    def create_plan(self, skills, agents, priorities=None):

        plan = []
        step = 1


        # Safety gets highest priority
        if priorities:

            for item in priorities:

                if item["area"] == "safety":

                    if "verifier_agent" in agents:
                        plan.append({
                            "step": step,
                            "agent": "verifier_agent",
                            "priority": "high",
                            "purpose": "Check safety risks and possible harm"
                        })
                        step += 1


        # Research for accuracy
        if priorities:

            for item in priorities:

                if item["area"] == "accuracy":

                    if "research_agent" in agents:
                        plan.append({
                            "step": step,
                            "agent": "research_agent",
                            "priority": "high",
                            "purpose": "Gather evidence and supporting information"
                        })
                        step += 1


                    if "left_brain" in agents:
                        plan.append({
                            "step": step,
                            "agent": "left_brain",
                            "priority": "high",
                            "purpose": "Analyse logic and risks"
                        })
                        step += 1


        # Creativity
        if "right_brain" in agents:

            plan.append({
                "step": step,
                "agent": "right_brain",
                "priority": "medium",
                "purpose": "Generate ideas and possibilities"
            })
            step += 1


        # Prevent duplicates
        existing = set()
        clean_plan = []

        for item in plan:

            if item["agent"] not in existing:
                clean_plan.append(item)
                existing.add(item["agent"])


        return {
            "manager": self.name,
            "status": "plan_created",
            "skills": skills,
            "priorities_used": priorities,
            "execution_plan": clean_plan
        }


executive_manager = ExecutiveManager()