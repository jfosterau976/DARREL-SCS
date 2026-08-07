from datetime import datetime


class LearningExtractor:

    def __init__(self):
        self.name = "SCS Learning Extractor"
        self.role = "reflection_to_learning"

    def extract(self, reflection):

        if not reflection:

            return {
                "status": "no_learning",
                "lessons": [],
                "lesson_count": 0
            }

        lesson = reflection.get(
            "lesson",
            {}
        )

        learning = []

        for improvement in lesson.get(
            "improvements",
            []
        ):

            learning.append({

                "type": "learning",

                "source": "reflection",

                "lesson": improvement,

                "confidence": lesson.get(
                    "confidence",
                    0.5
                ),

                "strength": 1,

                "importance": (
                    "HIGH"
                    if lesson.get("confidence", 0) >= 0.90
                    else "MEDIUM"
                    if lesson.get("confidence", 0) >= 0.75
                    else "LOW"
                ),

                "timestamp": datetime.now().isoformat()

            })

        return {

            "agent": self.name,

            "role": self.role,

            "status": "learning_extracted",

            "lessons": learning,

            "lesson_count": len(learning)

        }


learning_extractor = LearningExtractor()