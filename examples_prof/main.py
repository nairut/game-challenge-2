from game import Game

def main():
    """Main function to start the game."""
    print("Bem-vindo à Aventura!")
    game_object = Game()
    game_object.carregar_mundo("world.json")
    game_object.iniciar()

if __name__ == "__main__":
    main()
