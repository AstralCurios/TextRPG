#Execute the actual game here
from characters import *
from combat import *


class Character:
    def __init__(self, name, health, armor, attack_power):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack_power = attack_power
    
    def take_damage(self, damage):
        actual_damage = max(0, damage - self.armor)
        self.health -= actual_damage
        return actual_damage
    
    def is_alive(self):
        return self.health > 0
