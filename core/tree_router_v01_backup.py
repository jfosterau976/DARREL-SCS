class TreeRouter:

    def __init__(self):
        self.name = "SCS Tree Router"


    def route(self, message):

        text = message.lower()

        branches = []

        # Safety / high impact
        if any(word in text for word in [
            "health",
            "medical",
            "elderly",
            "safety",
            "risk",
            "danger"
        ]):
            branches.append("safety")


        # Knowledge / research
        if any(word in text for word in [
            "research",
            "analyse",
            "study",
            "information",
            "data"
        ]):
            branches.append("knowledge")


        # Creative thinking
        if any(word in text for word in [
            "create",
            "design",
            "invent",
            "idea",
            "new"
        ]):
            branches.append("creativity")


        # Logic / reasoning always available
        branches.append("reasoning")


        # Memory always checks previous experience
        branches.append("memory")


        return {
            "router": self.name,
            "status": "branches_selected",
            "input": message,
            "active_branches": list(dict.fromkeys(branches))
        }


tree_router = TreeRouter()