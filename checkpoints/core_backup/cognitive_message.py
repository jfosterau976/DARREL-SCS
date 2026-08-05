class CognitiveMessage:

    def __init__(
        self,
        sender,
        role,
        content,
        status="complete",
        confidence=0.5,
        claims=None,
        concerns=None,
        metadata=None
    ):

        self.sender = sender
        self.role = role
        self.content = content
        self.status = status
        self.confidence = confidence
        self.claims = claims or []
        self.concerns = concerns or []
        self.metadata = metadata or {}

    def to_dict(self):

        return {
            "sender": self.sender,
            "role": self.role,
            "content": self.content,
            "status": self.status,
            "confidence": self.confidence,
            "claims": self.claims,
            "concerns": self.concerns,
            "metadata": self.metadata
        }


def create_message(
    sender,
    role,
    content,
    status="complete",
    confidence=0.5,
    claims=None,
    concerns=None,
    metadata=None
):

    return CognitiveMessage(
        sender=sender,
        role=role,
        content=content,
        status=status,
        confidence=confidence,
        claims=claims,
        concerns=concerns,
        metadata=metadata
    )