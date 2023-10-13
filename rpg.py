class Warrior:
    def __init__(self, character_name, details, health, power):
        self.character_name = character_name
        self.details = details
        self.health = health
        self.power = power

    def greet(self):
        print(f"You selected {Warrior.characterName}")

    def alive(self):
        if self.health > 0:
            print(f"{Warrior.character_name} is alive and has {Warrior.health} health points")

    def attack(self, other_character):
        other_character.health -= self.power
        print(
            f"{self.character_name} attacks {other_character.character_name} for {self.power} damage"
        )


class Hero(Warrior):
    def announce(self):
        print(
            f"Prepare to be defeated, {Villain.character_name} by the mighty hand of {Hero.character_name}!"
        )


class Villain(Warrior):
    def taunt(self):
        print(f"You are no match for me {Hero.character_name}!")




villain = Villain("Dr. Evil", "Needs 1 MILLLLLLION dollars", 25, 5)
hero = Hero("Austin Powers", "Shagadellic, BABY!", 25, 10)