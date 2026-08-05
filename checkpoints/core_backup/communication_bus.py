class CommunicationBus:

    def __init__(self):
        self.name = "SCS Communication Bus"
        self.messages = []


    def send(self, sender, receiver, message, priority="normal"):

        packet = {
            "sender": sender,
            "receiver": receiver,
            "message": message,
            "priority": priority
        }

        self.messages.append(packet)

        return {
            "status": "message_sent",
            "packet": packet,
            "total_messages": len(self.messages)
        }


    def get_messages(self, receiver=None):

        if receiver is None:
            return self.messages

        return [
            msg for msg in self.messages
            if msg["receiver"] == receiver
        ]


    def clear(self):

        self.messages = []

        return {
            "status": "cleared"
        }


communication_bus = CommunicationBus()