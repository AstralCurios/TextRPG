#Execute the actual game here
from characters import *
from combat import *

#Create characters
player_name = input("Please enter the name of your character: ")
print(f"Welcome, {player_name}!")
player_class = input("Please choose your class (Wizard, Warrior, Rogue): ")
if player_class.lower() == "wizard":
    player = Wizard(player_name, stamina=5, intelligence=10)
elif player_class.lower() == "warrior":
    player = Warrior(player_name, stamina=10, strength=5)
elif player_class.lower() == "rogue":
    player = Rogue(player_name, stamina=7, dexterity=7)
else:
    raise Exception("Invalid class selected")

#Run combat
