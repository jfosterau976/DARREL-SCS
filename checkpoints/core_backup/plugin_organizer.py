class PluginOrganizer:
    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin, description):
        self.plugins[name] = {
            "plugin": plugin,
            "description": description,
            "status": "available"
        }

    def get(self, name):
        return self.plugins.get(name)

    def list_plugins(self):
        return {
            name: {
                "description": details["description"],
                "status": details["status"]
            }
            for name, details in self.plugins.items()
        }


plugin_organizer = PluginOrganizer()