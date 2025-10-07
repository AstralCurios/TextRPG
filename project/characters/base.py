# manages overhead for character actions

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.armor = 0

    def take_damage(self, dmg):
        actual = max(0, dmg - self.armor)
        self.health -= actual
        return actual

    def is_alive(self):
        return self.health > 0