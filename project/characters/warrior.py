# manages the warrior class
from .base import Character

class Warrior(Character):
    def __init__(self, name, stamina, strength):
        super().__init__(name)
        self._stamina = stamina
        self._str = strength
        self.health = stamina * 150
        self.armor = strength * 5