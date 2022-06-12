from collections import *
from pokemon import *


class PokeGame:
    def __init__(self, game_master):
        self.game_master = game_master
        self.setup()
        # self.draw_pokemon()

    def setup(self):
        psychic_type = PsychicType("Necrozma", "Nina")
        ghost_type = GhostType("Gastly", "Gage")
        # FairyType class by Allison Tsai
        fairy_type = FairyType("Clefairy", "Cleo", 70)
        pokemon1 = Pokemon("Tauros", "Tina")
        fighting_type = FightingType("Poliwrath", "Paul")
        fire_type = FireType("Charizard", "Charlie")
        dragon_type = DragonType("Exeggutor", "Ellen")
        bug_type = BugType("Metapod", "Marnie")
        self.game_master = [psychic_type, ghost_type, pokemon1,
                            fighting_type, fire_type, dragon_type,
                            bug_type, fairy_type]
        print(f"Your deck this game has {len(self.game_master)} cards!")

    def draw_pokemon(self):
        if self.game_master:
            return self.game_master.pop(1)
        else:
            print("Game Over")

    def print_menu(self):
        """ Prints the available Pokemon as a string."""
        print("Select a Pokemon to play against "
              "(or 9 to end)".center(55))
        poke_dict = OrderedDict()  # OrderedDict to maintain list order
        counter = 1
        for item in self.game_master:
            poke_dict[item.name] = counter
            counter += 1
        print("These are the Pokemon you can choose from: ".center(55))
        for k, v in poke_dict.items():
            print(v, k)
        while True:
            user_choice = int(input("Enter your choice: "))
            if user_choice != 9:
                user_choice = user_choice - 1
                print(f"Your pokemon: {self.game_master[user_choice]}")
                return self.game_master[user_choice]
            else:
                break


def main():
    deck1 = []
    pokegame1 = PokeGame(deck1)
    opponent_pokemon = pokegame1.draw_pokemon()
    try:
        print(f"Your opponent has selected: {opponent_pokemon.name} \n"
              f"{opponent_pokemon}")
        user_pokemon = pokegame1.print_menu()
        user_pokemon.attack(opponent_pokemon)
    except AttributeError:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

# menu_options = {
#     1: "",
#     2: "",
#     3: "",
#     4: "",
#     5: "",
#     6: "",
#     7: "",
#     8: "",
#     9: "End",
# }

# def main():
#     deck1 = []
#     game1 = PokeGame(deck1)
#     # for item in game1.game_master:
#     #     print(item.name)
#     game1.menu_options = {range(len(game1.game_master)): item.name
#     for item in game1.game_master}
#     print(game1.menu_options)
#     while True:
#         print()
#         game1.print_menu()
#         try:
#             option_choice = int(input("Enter your choice: "))
#         except ValueError:
#             print("Enter an integer please.")
#             continue
#        if option_choice in menu_options:
#             print(f"You chose {menu_options[option_choice]}\n")
#             if option_choice == 1:
#                 print(game1.game_master[0])
#             if option_choice == 2:
#                 print(game1.game_master[1])
#             if option_choice == 3:
#                 print(game1.game_master[2])
#             if option_choice == 4:
#                 print(game1.game_master[3])
#             if option_choice == 5:
#                 print(game1.game_master[4])
#             if option_choice == 6:
#                 print(game1.game_master[5])
#             if option_choice == 7:
#                 print(game1.game_master[6])
#             if option_choice == 8:
#                 pass
#             if option_choice == 9:
#                 print(f"Thanks for playing PokeGame! "
#                       f"We hope you had fun!")
#         else:
#             print("Enter an integer from the menu please.")
#
#     # game1.setup()
#     # drawnPokemon = game1.draw_pokemon()
