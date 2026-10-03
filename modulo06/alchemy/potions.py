from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    return f"Healing potion: {create_earth()} + {create_air()}"


def strength_potion() -> str:
    return f"Strength potion: {create_fire()} + {create_water()}"
