class SkillOrganizer:
    def __init__(self):
        self.name = "Skill Organizer"
        self.skills = {}

    def register(self, name, description):
        self.skills[name] = {
            "description": description,
            "status": "available"
        }

    def list_skills(self):
        return self.skills


skill_organizer = SkillOrganizer()