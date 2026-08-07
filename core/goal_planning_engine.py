class GoalPlanningEngine:

    def __init__(self):
        self.name = "SCS Goal Planning Engine"

    def create_goal(self, question):

        return {
            "system": self.name,
            "goal": question,
            "objective": "Find the best solution",
            "status": "goal_created"
        }

    def create_plan(self, goal):

        return {
            "system": self.name,
            "goal": goal["goal"],
            "plan": [
                "Analyse problem",
                "Generate possible approaches",
                "Evaluate risks",
                "Select best strategy",
                "Verify outcome"
            ],
            "status": "plan_created"
        }

    def think(self, question):

        goal = self.create_goal(question)
        plan = self.create_plan(goal)

        return {
            "system": self.name,
            "goal": goal,
            "plan": plan,
            "status": "planning_complete"
        }


goal_planner = GoalPlanningEngine()