from pokemon import *
from PokeGame import PokeGame


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
