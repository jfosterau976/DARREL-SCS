class ContextManager:

    def __init__(self):

        self.system_name = "Synthetic Cognitive System"
        self.abbreviation = "SCS"
        self.version = "V0.1"

        self.purpose = (
            "A modular cognitive AI system using "
            "specialised agents for analysis, creativity, "
            "synthesis and verification."
        )

    def get_context(self):

        return {
            "system_name": self.system_name,
            "abbreviation": self.abbreviation,
            "version": self.version,
            "purpose": self.purpose
        }


context_manager = ContextManager()