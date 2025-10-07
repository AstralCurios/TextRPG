# initializes the character classes and makes them available for import.
from .base import Character
from .wizard import Wizard
from .warrior import Warrior
from .rogue import Rogue

__all__ = ["Character", "Wizard", "Warrior", "Rogue"]