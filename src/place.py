from game_object import GameObject
from item import Item
from character import Character

class Place(GameObject):
    def __init__(self, name: str, description: str, takes_to: list[str] = None):
        super().__init__(name, description)
        self.takes_to = takes_to or []
        self.items: dict[str, Item] = {}
        self.characters: dict[str, Character] = {}

    def get_description(self) -> str:
        return self.description
    
    def get_name(self) -> str:
        return self.name
    
    def get_takes_to(self) -> list[str]:
        return self.takes_to
    
    def add_item(self, item: Item) -> None:
        self.items[item.name] = item
    
    def remove_item(self, item_name: str) -> Item:
        return self.items.pop(item_name, None)
    
    def add_character(self, character: Character) -> None:
        self.characters[character.name] = character
    
    def remove_character(self, character_name: str) -> Character:
        return self.characters.pop(character_name, None)
    
    def get_items_description(self) -> str:
        if not self.items:
            return "Não há itens aqui."
        
        items_text = "Itens neste local:\n"
        for item_name, item in self.items.items():
            items_text += f"- {item_name}: {item.description}\n"
        return items_text
    
    def get_characters_description(self) -> str:
        if not self.characters:
            return "Não há personagens aqui."
        
        characters_text = "Personagens neste local:\n"
        for char_name, character in self.characters.items():
            characters_text += f"- {char_name}: {character.description}\n"
        return characters_text
    
    def get_full_description(self) -> str:
        description = f"\n{self.name}\n"
        description += f"{self.description}\n\n"
        description += self.get_items_description() + "\n"
        description += self.get_characters_description() + "\n"
        description += "Lugares acessíveis:\n"
        for place in self.takes_to:
            description += f"- {place}\n"
        return description
