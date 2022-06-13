from pokemon import *


class PokeGame:
    def __init__(self):
        self.game_master = []
        self.setup()

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
        if len(self.game_master) > 0:
            drawn_pokemon = self.game_master.pop(0)
            print(f"Your opponent has selected: {drawn_pokemon.name} \n"
                  f"{drawn_pokemon}")
            return drawn_pokemon
        else:
            print("Game Over")
            return None

    def get_choice(self):
        """ Recieves Pokemon choice and info from user."""
        global user_pokemon, pokemon_hp
        print("Select a Pokemon to play with "
              "(or 9 to end)".center(55))
        print("1: Psychic Type")
        print("2: Fairy Type")
        while True:
            try:
                user_choice = int(input("Enter your choice: "))
                if user_choice == 9:
                    return None
                elif user_choice == 1:
                    pokemon_name = input("Enter a name for your "
                                         "Pokemon: ")
                    pokemon_trainer = input("Enter a trainer for your "
                                            "Pokemon: ")
                    user_pokemon = PsychicType(pokemon_name,
                                               pokemon_trainer)
                elif user_choice == 2:
                    pokemon_name = input("Enter a name for your "
                                         "Pokemon: ")
                    pokemon_trainer = input("Enter a trainer for your "
                                            "Pokemon: ")
                    while True:
                        try:
                            pokemon_hp = int(input("Enter hp for your "
                                                   "Pokemon: "))
                            break
                        except (TypeError, IndexError,
                                UnboundLocalError):
                            print("Please enter an integer.")
                            continue
                    user_pokemon = FairyType(pokemon_name,
                                             pokemon_trainer,
                                             pokemon_hp)
                else:
                    print("Please enter a valid choice.")
            except ValueError:
                print("Please enter an integer")
                continue
            return user_pokemon
        return user_pokemon


def main():
    pokegame1 = PokeGame()
    opponent_pokemon = pokegame1.draw_pokemon()
    while opponent_pokemon:
        user_pokemon = pokegame1.get_choice()
        user_pokemon.attack(opponent_pokemon)
        opponent_pokemon = pokegame1.draw_pokemon()


if __name__ == "__main__":
    main()

