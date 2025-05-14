from game_object import GameObject

class Item(GameObject):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False, item_type: str = "generic"):
        super().__init__(name, description)
        self.pickable = pickable
        self.location = location
        self.used = False
        self.item_type = item_type
        self.in_inventory = False

    def examine(self):
        return self.description

    def pick_item(self):
        if self.pickable and not self.in_inventory:
            self.in_inventory = True
            return f"Você pegou {self.name}."
        return "Você não pode pegar este item."

    def drop(self):
        if self.in_inventory:
            self.in_inventory = False
            return f"Você largou {self.name}."
        return "Você não está carregando este item."

    def show(self):
        return f"Você vê {self.name} aqui."

    def get_location(self):
        return self.location

    def use(self):
        return "Este item não pode ser usado."

    def display_location(self):
        print(self.location)


class Weapon(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False, offense_bonus: int = 0):
        super().__init__(name, description, location, pickable, "weapon")
        self.offense_bonus = offense_bonus

    def use(self):
        return f"Você brande {self.name}. Bônus de ataque: +{self.offense_bonus}"


class Armor(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False, defense_bonus: int = 0):
        super().__init__(name, description, location, pickable, "armor")
        self.defense_bonus = defense_bonus

    def use(self):
        return f"Você equipa {self.name}. Bônus de defesa: +{self.defense_bonus}"


class Key(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description, location, pickable, "key")
        self.used = False

    def use(self):
        if not self.used:
            self.used = True
            return f"Você usa {self.name} para abrir algo."
        return f"{self.name} já foi usada."


class Potion(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False, heal_amount: int = 0):
        super().__init__(name, description, location, pickable, "potion")
        self.heal_amount = heal_amount

    def use(self):
        if not self.used:
            self.used = True
            return f"Você bebe {self.name} e recupera {self.heal_amount} pontos de vida."
        return f"{self.name} já foi usada."


class QuestItem(Item):
    def __init__(self, name: str, description: str, location: str, pickable: bool = False):
        super().__init__(name, description, location, pickable, "quest_item")

    def use(self):
        return f"Este item parece importante para sua missão."


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