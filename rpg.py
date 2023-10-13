import random


class Warrior:
    def __init__(self, character_name, details, health, power):
        self.character_name = character_name
        self.details = details
        self.health = health
        self.power = power

    def greet(self):
        print(f"You selected {self.characterName}")

    def alive(self):
        if self.health > 0:
            print(
                f"\n{self.character_name} is alive and has {self.health} health points"
            )
            return self.health

    def attack(self, other_character):
        if self.power % 2 == 1:
            print("MISSED! Lucky for you!")
        else:
            random_power = random.randint(1, self.power)
            other_character.health -= random_power
            print(
                f"\n\n{self.character_name} attacks {other_character.character_name} for {random_power} damage"
            )

        if other_character.health <= 0:
            print(f"{other_character.character_name} is DEAD")
            print("/////////////////////////////////////////\n")


class Hero(Warrior):
    def announce(self, villain):
        print(
            f" {hero.character_name} says: You will be defeated, {villain.character_name}, by the mighty hand of {self.character_name}!"
        )
        print("/////////////////////////////////////////\n")


class Villain(Warrior):
    def taunt(self, hero):
        print(
            f"{villain.character_name} says: You are no match for me {hero.character_name}!"
        )
        print("/////////////////////////////////////////\n")


hero_input = input("Type your Hero name: ")
villain_input = input("Type your Villain name:  ")


##########INSTANTIATE VILLAIN AND HERO
villain = Villain(villain_input.upper(), "Needs 1 MILLLLLLION dollars", 25, 10)
hero = Hero(hero_input.upper(), "Shagadellic, BABY!", 25, 10)


while hero.alive() and villain.alive():
    print("\n\n\n/////////////////////////////////////////")
    print(f"{hero.character_name} HEALTH: {hero.health}")
    print(f"{villain.character_name} HEALTH: {villain.health} ")
    print("///////////CHOOSE THE NEXT STEP///////////////\n")
    print("f: attack villain with hero")
    print("a: attack hero with villain")
    print("s: you want to give up, so you run away")
    print("n: be a pacifist, but still stay")
    print("v: have villain taunt hero")
    print("h: have hero posture against villain\n")
    print("/////////////////////////////////////////\n")
    print("TYPE NEW INPUT BELOW")

    user_input = input()
    if user_input == "f":
        hero.attack(villain)
    elif user_input == "a":
        villain.attack(hero)
    elif user_input == "s":
        print("I thought you were better than that!")
        print("/////////////////////////////////////////\n")
        break
    elif user_input == "n":
        print(f"{hero.character_name} chooses not to fight.")
        villain.attack(hero)
        print(
            f"Can you believe {villain.character_name} still hits {hero.character_name}?  HOW RUDE?!?!"
        )
        print("/////////////////////////////////////////\n")
    elif user_input == "v":
        villain.taunt(hero)

    elif user_input == "h":
        hero.announce(villain)

    else:
        print("!!!!!!Please type a correct command!!!!!!")
        print("Options are:  'f', 'a', 's', 'n', 'v', 'h'")
        print("/////////////////////////////////////////\n")
