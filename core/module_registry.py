class ModuleRegistry:

    def __init__(self):
        self.name = "SCS Module Registry"
        self.modules = {}

    def register(self, name, module):
        self.modules[name] = module

    def get(self, name):
        return self.modules.get(name)

    def exists(self, name):
        return name in self.modules

    def remove(self, name):
        if name in self.modules:
            del self.modules[name]

    def available_modules(self):
        return sorted(self.modules.keys())

    def count(self):
        return len(self.modules)


module_registry = ModuleRegistry()