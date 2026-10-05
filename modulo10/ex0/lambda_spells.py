from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int,
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f'* {spell} *', spells))


def mage_stats(mages: list[dict[str, int]]) -> dict[str, int | float]:
    return {
        'max_power': max(mages, key=lambda mage: mage['power'])['power'],
        'min_power': min(mages, key=lambda mage: mage['power'])['power'],
        'avg_power': round(
            sum(mage['power'] for mage in mages) / len(mages),
            2,
        ),
    }


if __name__ == '__main__':
    artifacts: list[dict[str, Any]] = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
    ]
    spells = ['fireball', 'heal', 'shield']
    print('Testing artifact sorter...')
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )
    print('Testing spell transformer...')
    print(' '.join(spell_transformer(spells)))
