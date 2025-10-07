# manages the wizard class
from .base import Character

class Wizard(Character):
    def __init__(self, name, stamina, intelligence):
        super().__init__(name)
        self._stamina = stamina
        self._int = intelligence
        self.health = stamina * 100
        self.mana = intelligence * 10
        self.armor = intelligence * 1