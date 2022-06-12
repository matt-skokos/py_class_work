from random import random


class Pokemon:
    """Represents a Pokemon object"""
    damage = 40
    basic_attack = "tackle"

    def __init__(self, name, trainer):
        self.name, self.trainer = name, trainer
        self.level, self.hp = 1, 50
        self.paralyzed = False

    def speak(self):
        print(self.name + "!")

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(f"{self.name} used {self.basic_attack}!")
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(f"{self.name} fainted!")

    def __str__(self):
        return f"{self.name}'s trainer is {self.trainer} and their basic " \
               f"attack is '{self.basic_attack}'"


class PsychicType(Pokemon):
    basic_attack = "Psychic Shift"
    prob = 1

    def __init__(self, name, trainer):
        super().__init__(name, trainer)

    def attack(self, other):
        """Attacks a Pokemon with a chance of paralyzing it unless it is
        PsychicType
        """
        if isinstance(other, (FightingType, PoisonType)):
            self.damage = self.damage * 2
        elif isinstance(other, (BugType, GhostType, DarkType)):
            self.damage = self.damage / 2
        if not self.paralyzed:
            self.speak()
            print(f"{self.name} used {self.basic_attack}!")
            other.receive_damage(self.damage)
        if random() < self.prob and not isinstance(other, PsychicType):
            other.paralyzed = True
            print(f"{other.name} is paralyzed!")

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - self.damage)
        if self.hp == 0:
            print(f"{self.name} fainted!")

    def __str__(self):
        return f"{self.name}'s trainer is {self.trainer} and their basic " \
               f"attack is '{self.basic_attack}'"


# FairyType class by Allison Tsai

class FairyType(Pokemon):
    basic_attack = 'Sweet Kiss'
    prob = .1

    def __init__(self, name, trainer, hp: int):
        super().__init__(name, trainer)  # maybe shoot a message that the parenthesis are missing
        self.level = 1
        self.hp = hp
        self.paralyzed = False
        self.confused = False
        self.burned = False
        self.poisoned = False

    def __str__(self):
        return f"FairyPokemon:{self.name}:{self.trainer}:{self.level}:" \
               f"{self.hp}:{self.paralyzed}"

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            if isinstance(other, (FightingType, DragonType, DarkType)):
                double_damage = self.damage * 2
                other.receive_damage(double_damage)
            elif isinstance(other, (PoisonType, FireType)):
                half_damage = self.damage / 2
                other.receive_damage(half_damage)
            else:
                other.receive_damage(self.damage)
            if random.random() < self.prob:  # chance of inflicting Confusion
                other.confused = True
                print(f"{other.name} is confused!")
        else:
            print(f"{self.name} could not attack. {self.name} is paralyzed!")


class FightingType(Pokemon):
    """FightingType stub"""
    pass


class PoisonType(Pokemon):
    """PoisonType against"""
    pass


class BugType(Pokemon):
    """BugType stub"""
    pass


class GhostType(Pokemon):
    """GhostType stub"""
    pass


class DarkType(Pokemon):
    """DarkType stub"""
    pass


class FireType(Pokemon):
    """FireType stub"""
    pass


class DragonType(Pokemon):
    """DragonType stub"""
    pass


def main():
    necrozma = PsychicType("Necrozma", "Matt")
    darkpoke = DarkType("DarkPoke", "Dennis")  # weak against check
    ghostpoke = GhostType("GhostType", "Greg")  # damage received check
    fightpoke = FightingType("FighterType", "Frank")  # strong against check
    necrozma.attack(darkpoke)
    print("Darkpoke hp: ", darkpoke.hp)
    ghostpoke.attack(necrozma)
    print("Necrozma hp: ", necrozma.hp)
    fightpoke.attack(necrozma)
    darkpoke.attack(necrozma)
    print("Necrozma hp: ", necrozma.hp)


if __name__ == "__main__":
    main()
