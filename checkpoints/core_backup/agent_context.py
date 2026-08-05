from core.communication_bus import communication_bus


class AgentContext:

    def __init__(self):
        self.name = "SCS Agent Context Manager"


    def get_context(self, agent):

        messages = communication_bus.get_messages(agent)

        return {
            "agent": agent,
            "context_messages": messages,
            "message_count": len(messages)
        }


agent_context = AgentContext()