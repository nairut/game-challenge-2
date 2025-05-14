from game_object import GameObject
from item import Item

class Character(GameObject):
    def __init__(self, name: str, description: str, location: str = None, character_type: str = "NPC"):
        if not name:
            raise ValueError("O nome do personagem não pode estar vazio.")
        if not description:
            raise ValueError("A descrição do personagem não pode estar vazia.")
        super().__init__(name, description)
        self.location = location
        self.character_type = character_type
        self.inventory = {}

    def speak(self):
        return "Olá!"

    def get_location(self):
        return self.location

    def set_location(self, new_location: str):
        self.location = new_location

class Player(Character):
    def __init__(self, name: str, description: str = "Um aventureiro corajoso", location: str = "Floresta"):
        super().__init__(name, description, location, "player")
        self.health = 100
        self.max_health = 100
        self.equipped_weapon = None
        self.equipped_armor = None

    def pick_up_item(self, item: Item) -> str:
        if not item.pickable:
            return f"Não é possível pegar {item.name}."
        
        if item.in_inventory:
            return f"Você já está carregando {item.name}."
        
        result = item.pick_item()
        if "pegou" in result:
            self.inventory[item.name] = item
        return result

    def drop_item(self, item_name: str) -> str:
        if item_name not in self.inventory:
            return f"Você não está carregando {item_name}."
        
        item = self.inventory[item_name]
        result = item.drop()
        if "largou" in result:
            del self.inventory[item_name]
            if self.equipped_weapon == item:
                self.equipped_weapon = None
            if self.equipped_armor == item:
                self.equipped_armor = None
        return result

    def show_inventory(self) -> str:
        if not self.inventory:
            return "Seu inventário está vazio."
        
        inventory_text = "Seu inventário:\n"
        for item_name, item in self.inventory.items():
            inventory_text += f"- {item_name}: {item.description}\n"
        return inventory_text

    def use_item(self, item_name: str) -> str:
        if item_name not in self.inventory:
            return f"Você não está carregando {item_name}."
        
        item = self.inventory[item_name]
        result = item.use()
        
        if item.item_type == "weapon":
            self.equipped_weapon = item
        elif item.item_type == "armor":
            self.equipped_armor = item
        elif item.item_type == "potion":
            self.health = min(self.max_health, self.health + item.heal_amount)
        
        return result

    def get_status(self) -> str:
        status = f"Status de {self.name}:\n"
        status += f"Vida: {self.health}/{self.max_health}\n"
        if self.equipped_weapon:
            status += f"Arma equipada: {self.equipped_weapon.name}\n"
        if self.equipped_armor:
            status += f"Armadura equipada: {self.equipped_armor.name}\n"
        return status

class NPC(Character):
    def __init__(self, name: str, description: str, location: str, dialog: list[str] = None):
        super().__init__(name, description, location, "NPC")
        self.dialog = dialog or ["Olá, aventureiro!"]
        self.current_dialog_index = 0

    def speak(self) -> str:
        if not self.dialog:
            return "Este personagem não tem nada a dizer."
        
        dialog = self.dialog[self.current_dialog_index]
        self.current_dialog_index = (self.current_dialog_index + 1) % len(self.dialog)
        return dialog