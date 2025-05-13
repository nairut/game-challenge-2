from game_object import GameObject
from item import Item

class Place(GameObject):
    def __init__(self, name: str, description: str, takes_to: str = False):
        super().__init__(name, description)
        self.takes_to = takes_to
        self.items: dict[str, Item] = {}

    def get_description(self):
        return self.description
    
    def get_name(self):
        return self.name
    
    def get_takes_to(self):
        return self.takes_to
    
    def add_item(self, item: Item):
        self.items[item.name] = item
