class StrategyEvolutionEngine:

    def __init__(self):
        self.name = "SCS Strategy Evolution Engine"
        self.strategy_history = []


    def evaluate_strategy(self, strategy, performance_score):

        record = {
            "strategy": strategy,
            "performance_score": performance_score
        }

        self.strategy_history.append(record)

        return {
            "system": self.name,
            "strategy": strategy,
            "performance_score": performance_score,
            "status": "strategy_recorded",
            "total_strategies": len(self.strategy_history)
        }


    def choose_best_strategy(self):

        if not self.strategy_history:
            return {
                "strategy": "LEFT+RIGHT+SYNTHESIS+VERIFIER",
                "reason": "No strategy history available"
            }

        best = max(
            self.strategy_history,
            key=lambda x: x["performance_score"]
        )

        return {
            "strategy": best["strategy"],
            "reason": "Highest performance strategy selected",
            "score": best["performance_score"]
        }


strategy_evolution = StrategyEvolutionEngine()