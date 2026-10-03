import functools
import operator
from collections.abc import Callable
from typing import Any


Operation = Callable[[int, int], int]


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Operation] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda left, right: max(left, right),
        'min': lambda left, right: min(left, right),
    }
    if operation not in operations:
        raise ValueError('Unknown operation')
    return functools.reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        'fire': functools.partial(base_enchantment, 50, 'fire'),
        'ice': functools.partial(base_enchantment, 50, 'ice'),
        'lightning': functools.partial(base_enchantment, 50, 'lightning'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(value: Any) -> str:
        return 'Unknown spell type'

    @dispatch.register
    def _(value: int) -> str:
        return f'Damage spell: {value} damage'

    @dispatch.register
    def _(value: str) -> str:
        return f'Enchantment: {value}'

    @dispatch.register
    def _(value: list) -> str:
        return f'Multi-cast: {len(value)} spells'

    return dispatch


if __name__ == '__main__':
    print('Testing spell reducer...')
    print(f'Sum: {spell_reducer([10, 20, 30, 40], "add")}')
    print(f'Product: {spell_reducer([10, 20, 30, 40], "multiply")}')
    print(f'Max: {spell_reducer([10, 20, 30, 40], "max")}')
    print('Testing memoized fibonacci...')
    for number in [0, 1, 10, 15]:
        print(f'Fib({number}): {memoized_fibonacci(number)}')
    dispatcher = spell_dispatcher()
    print('Testing spell dispatcher...')
    print(dispatcher(42))
    print(dispatcher('fireball'))
    print(dispatcher(['a', 'b', 'c']))
    print(dispatcher({}))
