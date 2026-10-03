from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'
    return enchant


def memory_vault() -> dict[str, Callable[..., object]]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


if __name__ == '__main__':
    counter_a = mage_counter()
    counter_b = mage_counter()
    print('Testing mage counter...')
    print(f'counter_a call 1: {counter_a()}')
    print(f'counter_a call 2: {counter_a()}')
    print(f'counter_b call 1: {counter_b()}')
    accumulator = spell_accumulator(100)
    print('Testing spell accumulator...')
    print(f'Base 100, add 20: {accumulator(20)}')
    print(f'Base 100, add 30: {accumulator(30)}')
    print('Testing enchantment factory...')
    print(enchantment_factory('Flaming')('Sword'))
    print(enchantment_factory('Frozen')('Shield'))
    vault = memory_vault()
    print('Testing memory vault...')
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
