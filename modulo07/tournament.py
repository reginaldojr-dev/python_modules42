from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print('*** Tournament ***')
    print(f'{len(opponents)} opponents involved')
    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]
    for index, (left, left_strategy) in enumerate(creatures):
        for right, right_strategy in creatures[index + 1:]:
            print('* Battle *')
            print(left.describe())
            print('vs.')
            print(right.describe())
            print('now fight!')
            try:
                for action in left_strategy.act(left):
                    print(action)
                for action in right_strategy.act(right):
                    print(action)
            except StrategyError as error:
                print(f'Battle error, aborting tournament: {error}')
                return


if __name__ == '__main__':
    print('Tournament 0 (basic)')
    print('[ (Flameling+Normal), (Healing+Defensive) ]')
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print('Tournament 1 (error)')
    print('[ (Flameling+Aggressive), (Healing+Defensive) ]')
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print('Tournament 2 (multiple)')
    print('[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]')
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
