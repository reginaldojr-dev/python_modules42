from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creatures import HealCapability, TransformCapability


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
        if isinstance(creature, HealCapability):
            print(creature.heal())

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
        if isinstance(creature, TransformCapability):
            print(creature.transform())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.revert())
