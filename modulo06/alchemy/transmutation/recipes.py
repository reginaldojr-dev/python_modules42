from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Lead to gold: {create_air()} + {create_fire()} + "
        f"{strength_potion()}"
    )
