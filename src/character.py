from game_object import GameObject
from item import Item
from place import Place

class Character(GameObject):
    def __init__(self, name: str, description: str, location: str = False, type: str = False):
        if not name:
            raise ValueError("Character name cannot be empty.")
        if not description:
            raise ValueError("Character description cannot be empty.")
        super().__init__(name, description)
        self.location = location
        self.type = type



    def speak(self):
        print('Sou um jogador do Jogo')

        
    def add_item(self, item_object: Item):
        self.item_object_dic[item_object.name] = item_object


    def pick_up_item(self, item_object: Item):
        pass


    def drop_item(item):
        pass

    def show_inventory():
        pass

    def go_to(place_name):
        pass




class Player(Character):
    def __init__(self, name, description="Player", location="Start", type="player"):
        super().__init__(name, description, location, type)
        self.item_object_dict: dict[str, Item] = {}
        self.place_object_dict: dict[str, Place] = {}




    def pick_up_item(self, item_object: Item):
        if item_object.pickable:
            print(f"{self.name}, você pegou o item {item_object.name}.")
        else:
            print(f"Não é possível pegar este item: {item_object.name}")


    def drop_item(self, item_object: Item):
        if item_object.pickable:
            print(f'{self.name}, você soltou o item {item_object.name}')


    def show_inventory(self, item_object_dict: dict[str, Item]):
        for item in item_object_dict:
            print(item)

    def go_to(self, place_object: Place):
        print(f'{self.name}, escolha um local para onde quer ir:')
        new_places = place_object.takes_to
        print('--------------')
        index_list = []
        for index, place in enumerate(new_places, start=1):
            print(f'{index} - {place}')
            index_list.append(index)
        print('--------------')

        while True:
            user_input = input('Insira sua escolha: ')
            if user_input == '1':
                print(f'{self.name}, você está indo para: {new_places[0]}')
                return new_places[0]
            elif user_input == '2':
                print(f'{self.name}, você está indo para: {new_places[1]}')
                return new_places[1]
            elif user_input == '3':
                try:
                    print(f'{self.name}, você está indo para: {new_places[2]}')
                    return new_places[2]
                except IndexError:
                    print('Por favor, escolher uma opção válida')

            elif user_input == 'voltar':
                return
            else:
                print('Por favor, escolher uma opção ou digite "voltar" para retornar.')


class NPC(Character):
    def __init__(self, name: str, description: str, location: str, type: str):
        super().__init__(name, description, location, type)
        self.dialog: list[str] = []



    def speak(self):
        self.dialog = 'Sou um personagem do jogo (NPC)'
        print(self.dialog)