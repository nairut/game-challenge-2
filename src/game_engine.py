from place import Place
from character import Character, Player, NPC
from item import Item, Weapon, Armor, Key, Potion, QuestItem
import os
import json
from colorama import init, Fore, Style
from typing import Dict, List, Tuple, Optional

# Inicializa o colorama
init()

class TextFormatter:
    """Gerencia toda a formatação e estilo de texto da interface do jogo."""
    
    def __init__(self) -> None:
        self.separator = "=" * 60
        self.section_separator = "-" * 60

    def format_separator(self) -> str:
        """Retorna uma linha separadora formatada."""
        return f"\n{Fore.CYAN}{self.separator}{Style.RESET_ALL}\n"

    def format_section(self, title: str) -> str:
        """Retorna um cabeçalho de seção formatado com título e sublinhado."""
        return f"\n{Fore.YELLOW}{title}\n{'-' * len(title)}{Style.RESET_ALL}"

    def format_game_output(self, text: str) -> str:
        """Retorna uma mensagem geral do jogo formatada."""
        return f"{Fore.GREEN}>>> {text}{Style.RESET_ALL}"

    def format_error(self, text: str) -> str:
        """Retorna uma mensagem de erro formatada."""
        return f"{Fore.RED}>>> {text}{Style.RESET_ALL}"

    def format_success(self, text: str) -> str:
        """Retorna uma mensagem de sucesso formatada."""
        return f"{Fore.GREEN}>>> {text}{Style.RESET_ALL}"

    def format_npc_dialog(self, npc_name: str, dialog: str) -> str:
        """Retorna um diálogo de NPC formatado."""
        return f"{Fore.MAGENTA}>>> {npc_name}: {dialog}{Style.RESET_ALL}"

    def format_input_prompt(self) -> str:
        """Retorna um prompt de entrada formatado."""
        return f"{Fore.CYAN}>>> O que você quer fazer? {Style.RESET_ALL}"

    def format_game_title(self) -> str:
        """Retorna o título do jogo formatado."""
        return f"\n{Fore.CYAN}=== AVENTURA TEXTUAL ==={Style.RESET_ALL}\n"

    def format_farewell(self) -> str:
        """Retorna uma mensagem de despedida formatada."""
        return f"\n{Fore.GREEN}Obrigado por jogar! Até a próxima aventura!{Style.RESET_ALL}"


class GameEngine:
    """Classe principal do motor do jogo que gerencia o estado e a lógica do jogo."""

    def __init__(self) -> None:
        self.place_object_dict: Dict[str, Place] = {}
        self.item_object_dict: Dict[str, Item] = {}
        self.npc_object_dict: Dict[str, Character] = {}
        self.world: Dict = {}
        self.player: Optional[Player] = None
        self.current_place: Optional[Place] = None
        self.game_running: bool = False
        self.formatter = TextFormatter()

    def print_separator(self) -> None:
        """Imprime uma linha separadora."""
        print(self.formatter.format_separator())

    def print_section(self, title: str) -> None:
        """Imprime um cabeçalho de seção."""
        print(self.formatter.format_section(title))

    def _create_case_insensitive_dict(self, items: Dict[str, any]) -> Dict[str, str]:
        """Cria um mapeamento case-insensitive de nomes de itens para suas versões originais."""
        return {name.lower(): name for name in items.keys()}

    def _get_original_case_name(self, name: str, case_dict: Dict[str, str]) -> Optional[str]:
        """Obtém a versão original de um nome a partir de um dicionário case-insensitive."""
        return case_dict.get(name.lower())

    def get_available_actions(self) -> List[Tuple[str, List[str]]]:
        """Retorna uma lista de ações disponíveis agrupadas por categoria."""
        actions = []
        
        # Ações sempre disponíveis
        actions.append(("AÇÕES DISPONÍVEIS", [
            "olhar: Ver descrição do local",
            "inventario (ou i): Ver seus itens",
            "status: Ver seu status",
            "ajuda: Ver todos os comandos",
            "sair: Encerrar o jogo"
        ]))
        
        # Ações relacionadas a itens
        if self.current_place.items:
            actions.append(("ITENS QUE VOCÊ PODE PEGAR", [
                f"pegar {item_name}" for item_name in self.current_place.items
            ]))
        
        # Ações relacionadas ao inventário
        if self.player.inventory:
            actions.append(("ITENS NO SEU INVENTÁRIO", [
                f"usar {item_name}" for item_name in self.player.inventory
            ] + [
                f"largar {item_name}" for item_name in self.player.inventory
            ]))
        
        # Ações relacionadas a NPCs
        if self.current_place.characters:
            actions.append(("PERSONAGENS COM QUEM VOCÊ PODE FALAR", [
                f"falar com {char_name}" for char_name in self.current_place.characters
            ]))
        
        # Ações de movimento
        if self.current_place.takes_to:
            actions.append(("LUGARES PARA ONDE VOCÊ PODE IR", [
                f"ir para {place_name}" for place_name in self.current_place.takes_to
            ]))
        
        return actions

    def display_available_actions(self) -> None:
        """Exibe todas as ações disponíveis agrupadas por categoria."""
        actions = self.get_available_actions()
        for section_title, section_actions in actions:
            self.print_section(section_title)
            for action in section_actions:
                print(f"- {action}")

    def show_help(self) -> None:
        """Exibe o menu de ajuda com todos os comandos disponíveis."""
        self.print_separator()
        self.print_section("AJUDA - COMANDOS DISPONÍVEIS")
        help_text = """
- olhar: Mostra a descrição detalhada do local atual
- inventario (ou i): Mostra seus itens
- pegar <item>: Pega um item do local
- largar <item>: Larga um item do seu inventário
- usar <item>: Usa um item do seu inventário
- falar com <personagem>: Fala com um personagem
- ir para <lugar>: Move para outro lugar
- status: Mostra seu status atual
- ajuda: Mostra esta mensagem
- sair: Encerra o jogo
"""
        print(help_text)
        self.print_separator()

    def _handle_pick_item(self, item_name: str) -> bool:
        """Processa o comando 'pegar'."""
        item_name_lower = item_name.lower()
        items_lower = self._create_case_insensitive_dict(self.current_place.items)
        
        original_item_name = self._get_original_case_name(item_name, items_lower)
        if original_item_name:
            item = self.current_place.items[original_item_name]
            result = self.player.pick_up_item(item)
            print(self.formatter.format_success(result))
            if "pegou" in result:
                self.current_place.remove_item(original_item_name)
        else:
            print(self.formatter.format_error(f"Não há {item_name} aqui."))
        return True

    def _handle_drop_item(self, item_name: str) -> bool:
        """Processa o comando 'largar'."""
        item_name_lower = item_name.lower()
        inventory_lower = self._create_case_insensitive_dict(self.player.inventory)
        
        original_item_name = self._get_original_case_name(item_name, inventory_lower)
        if original_item_name:
            result = self.player.drop_item(original_item_name)
            print(self.formatter.format_success(result))
            if "largou" in result:
                self.current_place.add_item(self.item_object_dict[original_item_name])
        else:
            print(self.formatter.format_error(f"Você não está carregando {item_name}."))
        return True

    def _handle_use_item(self, item_name: str) -> bool:
        """Processa o comando 'usar'."""
        item_name_lower = item_name.lower()
        inventory_lower = self._create_case_insensitive_dict(self.player.inventory)
        
        original_item_name = self._get_original_case_name(item_name, inventory_lower)
        if original_item_name:
            print(self.formatter.format_success(self.player.use_item(original_item_name)))
        else:
            print(self.formatter.format_error(f"Você não está carregando {item_name}."))
        return True

    def _handle_talk_to_npc(self, npc_name: str) -> bool:
        """Processa o comando 'falar com'."""
        npc_name_lower = npc_name.lower()
        characters_lower = self._create_case_insensitive_dict(self.current_place.characters)
        
        original_npc_name = self._get_original_case_name(npc_name, characters_lower)
        if original_npc_name:
            npc = self.current_place.characters[original_npc_name]
            print(self.formatter.format_npc_dialog(npc.name, npc.speak()))
        else:
            print(self.formatter.format_error(f"Não há {npc_name} aqui."))
        return True

    def _handle_move_to(self, place_name: str) -> bool:
        """Processa o comando 'ir para'."""
        place_name_lower = place_name.lower()
        takes_to_lower = [place.lower() for place in self.current_place.takes_to]
        
        if place_name_lower in takes_to_lower:
            original_place_name = next(place for place in self.current_place.takes_to if place.lower() == place_name_lower)
            if original_place_name in self.place_object_dict:
                self.current_place = self.place_object_dict[original_place_name]
                self.print_separator()
                print(self.formatter.format_success(f"Você foi para {original_place_name}."))
                print(self.current_place.get_full_description())
                self.print_separator()
            else:
                print(self.formatter.format_error(f"Erro: Local {place_name} não encontrado."))
        else:
            print(self.formatter.format_error(f"Você não pode ir para {place_name} a partir daqui."))
        return True

    def process_command(self, command: str) -> bool:
        """Processa um comando do jogador e retorna se o jogo deve continuar."""
        command = command.lower().strip()
        
        if command == "sair":
            return False
        
        if command == "ajuda":
            self.show_help()
            return True
        
        if command == "olhar":
            self.print_separator()
            print(self.current_place.get_full_description())
            self.print_separator()
            return True
        
        if command in ["inventario", "i"]:
            self.print_separator()
            print(self.player.show_inventory())
            self.print_separator()
            return True
        
        if command == "status":
            self.print_separator()
            print(self.player.get_status())
            self.print_separator()
            return True
        
        if command.startswith("pegar "):
            return self._handle_pick_item(command[6:].strip())
        
        if command.startswith("largar "):
            return self._handle_drop_item(command[7:].strip())
        
        if command.startswith("usar "):
            return self._handle_use_item(command[5:].strip())
        
        if command.startswith("falar com "):
            return self._handle_talk_to_npc(command[10:].strip())
        
        if command.startswith("ir para "):
            return self._handle_move_to(command[8:].strip())
        
        print(self.formatter.format_error("Comando não reconhecido. Digite 'ajuda' para ver os comandos disponíveis."))
        return True

    def run(self) -> None:
        """Loop principal do jogo."""
        self.print_separator()
        print(self.formatter.format_game_title())
        self.print_separator()
        
        # Carrega o mundo do jogo
        if not self.load_world():
            return
        
        self.load_places()
        self.load_items()
        self.load_npcs()
        
        # Cria o jogador
        if not self.create_player():
            return
        
        # Define a localização inicial
        self.current_place = self.place_object_dict["Floresta"]
        self.print_separator()
        print(self.current_place.get_full_description())
        self.print_separator()
        
        # Loop principal do jogo
        self.game_running = True
        while self.game_running:
            self.display_available_actions()
            self.print_separator()
            command = input(self.formatter.format_input_prompt()).strip()
            self.game_running = self.process_command(command)
        
        self.print_separator()
        print(self.formatter.format_farewell())
        self.print_separator()

    def find_world_path(self) -> str:
        """Retorna o caminho para o arquivo world.json."""
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'world.json')
    
    def load_world(self) -> Dict:
        """Carrega o mundo do jogo a partir do arquivo world.json."""
        try:
            with open(self.find_world_path(), 'r', encoding='utf8') as f:
                self.world = json.load(f)
                return self.world
        except FileNotFoundError:
            print(self.formatter.format_error("Erro: O arquivo 'world.json' não foi encontrado. Encerrando o jogo..."))
        except PermissionError:
            print(self.formatter.format_error("Erro: Você não tem permissão para acessar 'world.json'. Encerrando o jogo..."))
        except json.JSONDecodeError:
            print(self.formatter.format_error("Erro: Falha ao decodificar JSON — verifique a sintaxe em 'world.json'. Encerrando o jogo..."))
        except Exception as e:
            print(self.formatter.format_error(f"Ocorreu um erro inesperado: {e}. Encerrando o jogo."))
        self.world = None
        return None
    
    def load_places(self) -> None:
        """Carrega os lugares do mundo do jogo."""
        if not self.world:
            raise ValueError('Mundo não foi carregado corretamente.')
        
        locations = self.world.get("locations", [])
        if not locations:
            raise KeyError("Chave 'locations' não encontrada nos dados do mundo.")
        
        for data in locations:
            name = data.get("name", "")
            description = data.get("description", "")
            takes_to = data.get("takes_to", [])
            self.place_object_dict[name] = Place(name, description, takes_to)

    def load_items(self) -> None:
        """Carrega os itens do mundo do jogo."""
        if not self.world:
            raise ValueError('Mundo não foi carregado corretamente.')
        
        items_data = self.world.get("items", [])
        if not items_data:
            raise KeyError("Chave 'items' não encontrada nos dados do mundo.")
        
        for data in items_data:
            name = data.get("name")
            description = data.get("description", "")
            location = data.get("location")
            pickable = data.get("pickable", False)
            item_type = data.get("type", "generic")

            # Cria o tipo apropriado de item
            if item_type == "weapon":
                offense_bonus = data.get("offense_bonus", 0)
                item = Weapon(name, description, location, pickable, offense_bonus)
            elif item_type == "armor":
                defense_bonus = data.get("defense_bonus", 0)
                item = Armor(name, description, location, pickable, defense_bonus)
            elif item_type == "key":
                item = Key(name, description, location, pickable)
            elif item_type == "potion":
                heal_amount = data.get("heal_amount", 0)
                item = Potion(name, description, location, pickable, heal_amount)
            elif item_type == "quest_item":
                item = QuestItem(name, description, location, pickable)
            else:
                item = Item(name, description, location, pickable, item_type)

            self.item_object_dict[name] = item
            
            # Adiciona o item ao seu local
            if location in self.place_object_dict:
                self.place_object_dict[location].add_item(item)
            else:
                print(self.formatter.format_error(f"⚠️ Local '{location}' não encontrado para o item '{name}'"))
            
    def load_npcs(self) -> None:
        """Carrega os NPCs do mundo do jogo."""
        if not self.world:
            print(self.formatter.format_error('Mundo não foi carregado corretamente.'))
            return
        
        characters_data = self.world.get("characters", [])
        for data in characters_data:
            name = data.get("name")
            description = data.get("description")
            location = data.get("location")
            dialog = data.get("dialog", ["Olá, aventureiro!"])
            
            npc = NPC(name, description, location, dialog)
            self.npc_object_dict[name] = npc
            
            # Adiciona o NPC ao seu local
            if location in self.place_object_dict:
                self.place_object_dict[location].add_character(npc)
            else:
                print(self.formatter.format_error(f"⚠️ Local '{location}' não encontrado para o NPC '{name}'"))

    def create_player(self) -> bool:
        """Cria o jogador e retorna se a criação foi bem-sucedida."""
        print(self.formatter.format_game_output("\nBem-vindo à Aventura!"))
        while True:
            name = input("Digite seu nome (ou 'sair' para encerrar): ").strip()
            if name.lower() == 'sair':
                return False
            if name:
                self.player = Player(name)
                print(self.formatter.format_success(f"\nBem-vindo, {name}! Sua aventura está prestes a começar..."))
                return True
            print(self.formatter.format_error("Por favor, digite um nome válido."))


if __name__ == "__main__":
    game = GameEngine()
    game.run()