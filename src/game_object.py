class GameObject:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


    def describe(self):
        return self.description