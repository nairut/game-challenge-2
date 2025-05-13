from game_object import GameObject
import os
import json
class Item(GameObject):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description)
        self.pickable = pickable
        self.location = location
        self.used = False

    def examine(self):
        return self.description

    def pick_item(self):
        return "You can't use this item right now."

    def drop(self):
        return f"You dropped the {self.name}."

    def show(self):
        return f"You see a {self.name} here."
    
    def get_location(self):
        return self.location
    
    def display_location(self):
        print(self.location)


class Key(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description, location, pickable)
        self.used = False

    def examine(self):
        return self.description

    def pick_item(self):
        pass

    def drop(self):
        return f"You dropped the {self.name}."

    def show(self):
        return f"You see a {self.name} here."
    
    def get_location(self):
        return self.location
    
    def display_location(self):
        print(self.location)



class Sword(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description, location, pickable)
        self.used = False

    def examine(self):
        return self.description

    def pick_item(self):
        self.used = True

    def drop(self):
        return f"You dropped the {self.name}."

    def show(self):
        return f"You see a {self.name} here."
    
    def get_location(self):
        return self.location
    
    def display_location(self):
        print(self.location)


class Armer(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description, location, pickable)
        self.item_in_use = False


    def examine(self):
        return self.description

    def pick_item(self):
        if self.pickable:
            self.item_in_use = True
            return f"você pegou o item {self.name}"
        return 'Este item não pode ser usado.'


    def drop(self):
        return f"você pegou o item {self.name}"

    def show(self):
        self.pickable = True
        return f"You see a {self.name} here."
    
    def get_location(self):
        return self.location
    
    def display_location(self):
        print(self.location)