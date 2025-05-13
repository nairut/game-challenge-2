import json
from player import Player

class Game:
    def __init__(self):
        self.locations = None
        self.characters = None
        self.items = None
        self.player = None

    def load_world(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            self.locations = data['locations']
            self.characters = data['characters']
            self.items = data['items']

    def start(self):
        print("Iniciando o jogo...\n")
        player = Player("Player", "Você é um aventureiro que acordou na floresta.")
        self.characters.append(player)
        self.player = player
        print("Você está na floresta.")
        print("Você pode ir para:")
        for location in self.locations:
            print(f"- {location['name']}")
    
