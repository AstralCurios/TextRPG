# manages the rogue class
from .base import Character

class Rogue(Character):
    def __init__(self, name, stamina, dexterity):
        super().__init__(name)
        self._stamina = stamina
        self._dex = dexterity
        self.health = stamina * 120
        self.armor = dexterity * 2
        self.dodge_chance = dexterity * 0.02
