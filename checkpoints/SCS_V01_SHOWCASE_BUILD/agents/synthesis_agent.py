class SynthesisAgent:

    def __init__(self):
        self.name = "SCS Synthesis Agent"
        self.role = "integration"


    def synthesize(self, message, agent_results):

        combined = []

        for agent_name, result in agent_results.items():

            combined.append(
                f"{agent_name.upper()}:\n{result}"
            )


        response = "\n\n".join(combined)


        return {
            "agent": self.name,
            "role": self.role,
            "status": "complete",
            "input": message,
            "response": (
                "Integrated cognitive output:\n\n"
                + response
            ),
            "confidence": 0.8,
            "agents_used": list(agent_results.keys())
        }


synthesis_agent = SynthesisAgent()