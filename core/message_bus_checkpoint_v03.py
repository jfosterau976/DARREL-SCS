class MessageBus:

    def __init__(self):

        self.name = "SCS Agent Message Router"

        self.messages = []


    def send(self, sender, receiver, message, priority="medium", confidence=1.0):

        packet = {

            "sender": sender,

            "receiver": receiver,

            "message": message,

            "priority": priority,

            "confidence": confidence

        }


        self.messages.append(packet)


        return {

            "status": "message_sent",

            "packet": packet,

            "total_messages": len(self.messages)

        }


    def broadcast(self, sender, receivers, message, confidence=1.0):

        results = []


        for receiver in receivers:

            results.append(

                self.send(

                    sender,

                    receiver,

                    message,

                    confidence=confidence

                )

            )


        return {

            "status": "broadcast_complete",

            "messages": results

        }


    def read_for_agent(self, receiver):

        return [

            message

            for message in self.messages

            if message["receiver"] == receiver

        ]


    def get_messages(self):

        return self.messages



message_bus = MessageBus()