class ExperienceStrategySelector:

    def __init__(self):
        self.name = "SCS Experience Strategy Selector"


    def select(self, recalled_experiences):

        if not recalled_experiences:
            return {
                "system": self.name,
                "strategy": "LEFT+RIGHT+SYNTHESIS+VERIFIER",
                "reason": "No previous experience found"
            }


        best = max(
            recalled_experiences,
            key=lambda x: x.get(
                "similarity_score",
                0
            )
        )

        return {
            "system": self.name,
            "strategy": best["experience"].get(
                "strategy",
                "LEFT+RIGHT+SYNTHESIS+VERIFIER"
            ),
            "reason": "Selected from previous experience",
            "similarity_score": best.get(
                "similarity_score",
                0
            )
        }


experience_strategy_selector = ExperienceStrategySelector()