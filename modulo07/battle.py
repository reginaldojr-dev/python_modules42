from ex0 import AquaFactory, FlameFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print('Testing factory')
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def battle(first: CreatureFactory, second: CreatureFactory) -> None:
    left = first.create_base()
    right = second.create_base()
    print('Testing battle')
    print(left.describe())
    print('vs.')
    print(right.describe())
    print('fight!')
    print(left.attack())
    print(right.attack())


if __name__ == '__main__':
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    test_factory(aqua)
    battle(flame, aqua)
