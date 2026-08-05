class SkillManager:
    def __init__(self):
        self.name = "Skill Manager"
        self.skills = {
            "creativity": ["right_brain"],
            "verification": ["verifier_agent"],
            "analysis": ["left_brain"],
            "research": ["research_agent"]
        }

    def add_skill(self, skill_name, agents):
        self.skills[skill_name] = agents

    def find_agents(self, skill_name):
        return self.skills.get(skill_name, [])

    def list_skills(self):
        return self.skills


skill_manager = SkillManager()