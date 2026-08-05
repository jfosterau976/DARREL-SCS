from core.communication_bus import communication_bus


class AgentMessageRouter:

    def __init__(self):
        self.name = "SCS Agent Message Router"


    def route(self, sender, receiver, message, priority="normal"):

        result = communication_bus.send(
            sender,
            receiver,
            message,
            priority
        )

        return {
            "router": self.name,
            "status": "routed",
            "delivery": result
        }


    def inbox(self, receiver):

        return {
            "router": self.name,
            "receiver": receiver,
            "messages": communication_bus.get_messages(receiver)
        }


agent_message_router = AgentMessageRouter()