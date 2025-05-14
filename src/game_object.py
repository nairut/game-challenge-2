class GameObject:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name
    
    def describe(self):
        return self.description