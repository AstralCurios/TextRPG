from characters import Wizard, Rogue, Warrior
from combat import *

def main():
    name = input("Name: ")
    klass = input("Class (wizard/warrior/rogue): ").lower()

    if klass == "wizard":
        player = Wizard(name, stamina=5, intelligence=10)
    elif klass == "warrior":
        player = Warrior(name, stamina=10, strength=5)
    elif klass == "rogue":
        player = Rogue(name, stamina=7, dexterity=7)
    else:
        raise Exception("Invalid class")

    print(f"Welcome, {player.name}!")

if __name__ == "__main__":
    main()