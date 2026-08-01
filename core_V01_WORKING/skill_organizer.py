class SkillOrganizer:
    def __init__(self):
        self.skills = {}

    def register(self, name, description):
        self.skills[name] = {
            "description": description,
            "status": "available"
        }

    def get(self, name):
        return self.skills.get(name)

    def list_skills(self):
        return {
            name: details["description"]
            for name, details in self.skills.items()
        }


skill_organizer = SkillOrganizer()