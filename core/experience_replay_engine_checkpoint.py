class ExperienceReplayEngine:

    def __init__(self):
        self.name = "SCS Experience Replay Engine"
        self.experiences = []


    def store(self, experience):

        self.experiences.append(experience)

        return {
            "system": self.name,
            "status": "experience_stored",
            "total_experiences": len(self.experiences)
        }


    def recall(self, question):

        matches = []

        keywords = question.lower().split()

        for experience in self.experiences:

            text = str(experience).lower()

            score = sum(
                1 for word in keywords
                if word in text
            )

            if score > 0:
                matches.append({
                    "experience": experience,
                    "similarity_score": score
                })


        return {
            "system": self.name,
            "question": question,
            "matches": matches,
            "total_matches": len(matches)
        }


experience_replay = ExperienceReplayEngine()