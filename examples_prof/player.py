class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.location = None
        self.inventory = []

class Player(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.location = "Floresta"
        self.inventory = ["Lanterna"]
