from game_object import GameObject
from place import Place
from character import Character, Player, NPC
from item import Item, Key, Sword, Armer
import os
import json


class GameEngine:
    def __init__(self):
        self.place_object_dict: dict[str, Place] = {}
        self.item_object_dict: dict[str, Item] = {}
        self.npc_object_dict: dict[str, Character] = {}
        self.world: dict[str] = {}
        self.player: Player = None
        self.current_place: Place = None


    def find_world_path(self) -> str:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'world.json')
    
    def load_world(self) -> dict:
        try:
            with open(self.find_world_path(), 'r', encoding='utf8') as f:
                self.world = json.load(f)
                return self.world
        except FileNotFoundError:
            print("Error: The file 'worlds.json' was not found. Exiting the game...")
        except PermissionError:
            print("Error: You do not have permission to access 'worlds.json'. Exiting the game...")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON — check the syntax in 'worlds.json'. Exiting the game...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Exiting the game.")
        self.world = None
        return None
    
    def load_places(self):
        if not self.world:
            raise ValueError('Mundo não foi carregado corretamente, por isso, os locais não foram carregados.')
        locations = self.world.get("locations", [])
        if not locations:
            raise KeyError("Missing 'locations' key in world data.")
        for data in locations:
            name = data.get("name", "")
            description = data.get("description", "")
            takes_to = data.get("takes_to", [])
            self.place_object_dict[name] = Place(name, description, takes_to)


    def load_items(self) -> dict:
        if not self.world:
            raise ValueError('Mundo não foi carregado corretamente, por isso, os itens não foram carregados.')
        all_items_from_world = self.world.get("items", [])
        if not all_items_from_world:
            raise KeyError("Missing 'items' key in world data.")
        for data in all_items_from_world:
            name = data.get("name")
            description = data.get("description", "")
            location = data.get("location")
            pickable = data.get("pickable", False)

            price = data.get("price")
            offense_bonus = data.get("offense_bonus")
            defense_bonus = data.get("defense_bonus")
            usable = data.get("usable")

            if name == "Chave":
                self.item_object_dict[name]  = Key(name, description, location, pickable)
            if name == "Espada":
                self.item_object_dict[name]  = Sword(name, description, location, pickable)
            if name == "Armadura":
                self.item_object_dict[name]  = Armer(name, description, location, pickable)

            if location in self.place_object_dict:
                self.place_object_dict[location].add_item(self.item_object_dict[name])
            else:
                print(f"⚠️ Local '{location}' não encontrado para o item '{name}'")


            
    def load_npcs(self):
        if not self.world:
            print('Mundo não foi carregado corretamente, por isso, os Personagens não foram carregados')
            return
        characters = self.world['characters']
        for character in characters:
            name = character.get('name')
            description = character.get('description')
            location = character.get('location')
            character_type = character.get('type')
            self.npc_object_dict[name] = NPC(name, description, location, character_type)


    def define_first_place(self):
        self.current_place = self.place_object_dict['Floresta']
         
    def create_player(self):
        # player_input = input('insira seu nome: ')
        player_input = "Turian"
        if player_input.lower() == 'sair':
            return 'sair'
        self.player = Player(player_input)
        print(f"Bem-vindo ao Jogo {self.player.name}")
    

    def show_inventory(self):
        self.player.show_inventory(self.item_object_dict)

    def get_places_user_can_go_from_current_place(self) -> list:
        places_user_can_go = self.current_place.get_takes_to()
        places_lower = []
        for place in places_user_can_go:
            places_lower.append(place.lower())
        return places_lower

    def using_sword_in_place(self):
        item = self.instanciate_item_in_current_place()
        if not item or item.name.lower() != "espada":
            return False  
        if item.used:
            return True 
        while True:
            print('Há uma árvore na frente da sua carruagem. Use a espada para abrir caminho.')
            user_input = input('Pressione 1 para usar a espada \nou 2 para voltar: ')
            if user_input == '1':
                item.pick_item()
                print(f'{self.player.name}, parabéns, você usou o item: {item.name}.')
                return True
            elif user_input == '2' or user_input.lower() == "sair":
                print("Você voltou para o menu inicial.")
                return False
            else:
                print("Escolha inválida.")

    def change_places(self):
        user_input = input(f"{self.player.name}, para onde você quer ir? - {self.current_place.get_takes_to()}: ")

        if user_input.lower() == 'sair':
            return 'sair'
        
        # Para sair da Floresta, tem que usar a Espada ao menos uma vez
        if self.current_place.name.lower() == 'floresta':
            espada_item = self.instanciate_item_in_current_place()
            if espada_item and espada_item.name.lower() == 'espada' and not espada_item.used:
                success = self.using_sword_in_place()
                if not success:
                    return


        stopwords = {"a", "o", "os", "as", "para", "da", "de", "do", "das", "dos", "pra", 'não'}
        user_words = [word for word in user_input.lower().split() if word not in stopwords]
        for place_name, value in self.place_object_dict.items():
            if any(word in place_name.lower() for word in user_words):
                for places_to_to in self.get_places_user_can_go_from_current_place():
                    if place_name.lower() in places_to_to.lower():
                        self.current_place = self.place_object_dict[place_name]
                        return
  


        print('***********************')
        print(f"A partir de {self.current_place.name} você não pode ir para {user_input}")
        print('***********************')
        return


    def show_action_menu(self):
        print('O que você deseja fazer agora?')
        print("1 - Entender melhor o ambiente")
        print("2 - Ver o inventário de itens")
        print("3 - Descobrir para onde pode ir")
        print("4 - Mover")


    def instanciate_item_in_current_place(self):
        for item, instance in self.item_object_dict.items():
            if instance.location == self.current_place.name:
                return instance



    def run(self):

        self.load_world()
        self.load_places()
        self.load_items()
        self.load_npcs()
        self.define_first_place()

        # self.change_places()
   
        print('Olá, vamos começar o jogo?')
        print('Antes de começar, por favor:')
        create_player = self.create_player()
        if create_player == 'sair':
            return



        get_out = ""
        while get_out == "":
            print('--------------------')
            print(f'Seu local atual:')
            print(self.current_place.name)
            self.show_action_menu()

            user_input = input('Insira sua Escolha ')
            if user_input.lower() == 'sair':
                return
            if user_input == '1':
                print('--------------------')
                print(self.current_place.description)
                print('--------------------')

            if user_input == '2':
                print('--------------------')
                for item in self.current_place.items.values():
                    print(f"- {item.name}: {item.examine()}")
        
            if user_input == '3':
                print('Você pode ir para: ')
                for place in self.current_place.takes_to:
                    print(f'- {place}')
            if user_input == '4':
                result = self.change_places()
                if result == 'sair':
                    return  # this will exit the game



if __name__ == "__main__":
    game = GameEngine()
    game.run()



