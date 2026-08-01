class StrategyOptimizer:

    def __init__(self):
        self.name = "SCS Strategy Optimizer"
        self.strategy_scores = {}


    def optimize(self, strategy, performance):

        score = self.strategy_scores.get(
            strategy,
            0
        )

        state = performance.get(
            "performance_state",
            "stable"
        )


        if state == "stable":
            score += 1

        elif state == "needs_more_reasoning":
            score -= 1


        self.strategy_scores[strategy] = score


        return {
            "system": self.name,
            "strategy": strategy,
            "performance_state": state,
            "new_score": score,
            "status": "strategy_optimized"
        }


strategy_optimizer = StrategyOptimizer()