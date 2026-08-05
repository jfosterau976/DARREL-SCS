class MessageBus:

    def __init__(self):

        self.name = "SCS Agent Message Bus"
        self.messages = []


    def send(self, sender, receiver, message, priority="medium"):

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

        if receiver:

            return [
                m for m in self.messages
                if m["receiver"] == receiver
            ]

        return self.messages


message_bus = MessageBus()