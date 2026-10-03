from .ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == '__main__':
    print('Testing Creature with healing capability')
    healing = HealingCreatureFactory()
    healing_creatures = [
        ('base:', healing.create_base()),
        ('evolved:', healing.create_evolved()),
    ]
    for label, creature in healing_creatures:
        print(label)
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())  # type: ignore[attr-defined]
    print('Testing Creature with transform capability')
    transforming = TransformCreatureFactory()
    transforming_creatures = [
        ('base:', transforming.create_base()),
        ('evolved:', transforming.create_evolved()),
    ]
    for label, creature in transforming_creatures:
        print(label)
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())  # type: ignore[attr-defined]
        print(creature.attack())
        print(creature.revert())  # type: ignore[attr-defined]
