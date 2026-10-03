from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    status = 'VALID' if ingredients.lower() in allowed else 'INVALID'
    return f'{ingredients} - {status}'
