from datetime import datetime


class LearningExtractor:

    def __init__(self):
        self.name = "SCS Learning Extractor"
        self.role = "reflection_to_learning"


    def extract(self, reflection):

        if not reflection:
            return {
                "status": "no_learning",
                "lesson": None
            }


        lesson_data = reflection.get(
            "lesson",
            {}
        )

        improvements = lesson_data.get(
            "improvements",
            []
        )


        lessons = []

        for improvement in improvements:

            lessons.append({
                "type": "learning",
                "source": "reflection_agent",
                "lesson": improvement,
                "confidence": lesson_data.get(
                    "confidence",
                    0.5
                ),
                "timestamp": datetime.now().isoformat()
            })


        return {
            "agent": self.name,
            "role": self.role,
            "status": "learning_extracted",
            "lessons": lessons,
            "lesson_count": len(lessons)
        }


learning_extractor = LearningExtractor()