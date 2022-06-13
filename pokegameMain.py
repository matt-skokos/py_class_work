from PokeGame import PokeGame


def main():
    pokegame1 = PokeGame()
    opponent_pokemon = pokegame1.draw_pokemon()
    while opponent_pokemon:
        user_pokemon = pokegame1.get_choice()
        user_pokemon.attack(opponent_pokemon)
        opponent_pokemon = pokegame1.draw_pokemon()


if __name__ == "__main__":
    main()

