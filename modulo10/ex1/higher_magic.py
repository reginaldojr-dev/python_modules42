from collections.abc import Callable


Spell = Callable[[str, int], str]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Spell,
) -> Spell:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return 'Spell fizzled'
    return caster


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == '__main__':
    def fireball(target: str, power: int) -> str:
        return f'Fireball hits {target} for {power}'

    def heal(target: str, power: int) -> str:
        return f'Heals {target} for {power}'

    combined = spell_combiner(fireball, heal)
    amplified = power_amplifier(fireball, 3)
    print('Testing spell combiner...')
    print(f'Combined spell result: {", ".join(combined("Dragon", 10))}')
    print('Testing power amplifier...')
    print(f'Original: 10, Amplified: {amplified("Dragon", 10).split()[-1]}')
