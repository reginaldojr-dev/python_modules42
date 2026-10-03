from modulo07.ex0.ex0 import AquaFactory, CreatureFactory, FlameFactory
from modulo07.ex1.ex1 import HealingCreatureFactory, TransformCreatureFactory
from modulo07.ex2.ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]
    for left, left_strategy in creatures:
        for right, right_strategy in creatures:
            if left is right:
                continue
            print(f'{left.name} vs {right.name}')
            try:
                for action in left_strategy.act(left):
                    print(action)
                for action in right_strategy.act(right):
                    print(action)
            except StrategyError as error:
                print(f'Invalid battle: {error}')


if __name__ == '__main__':
    battle([
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
