from core.cognitive_memory import cognitive_memory
class ReflectionAgent:

    def __init__(self):

        self.name = "SCS Reflection Agent"


    def reflect(self, verification):

        improvements = verification.get(
            "improvements",
            []
        )

        confidence = verification.get(
            "confidence",
            0
        )

        verdict = verification.get(
            "verdict",
            "UNKNOWN"
        )


        lesson = {

            "verdict": verdict,

            "confidence": confidence,

            "improvements": improvements

        }


        existing_memories = cognitive_memory.recall()


        duplicate = False


        for memory in existing_memories:

            if memory.get("type") == "reflection_lesson":

               if memory.get("lesson") == lesson:

                   duplicate = True

                   break


        if not duplicate:

            cognitive_memory.store(
                {
                    "type": "reflection_lesson",
                    "lesson": lesson,
                    "importance": "MEDIUM",
                    "status": "learned"
                }
            )


        return {

            "module": self.name,

            "status": "reflection_complete",

            "lesson": lesson,

            "memory_saved": True,

            "next_goal":

                "Improve future reasoning using lessons learned."

         }


reflection_agent = ReflectionAgent()