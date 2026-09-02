import random


ACHIEVEMENTS = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Treasure Hunter",
    "Speed Runner",
    "Survivor",
    "Strategist",
    "Crafting Genius",
    "World Savior",
    "Unstoppable",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, amount))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_distinct: set[str] = set()
    for achievements in players.values():
        all_distinct = all_distinct.union(achievements)

    common = set(ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}")

    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others = others.union(other_achievements)
        unique = achievements.difference(others)
        print(f"Only {name} has: {unique}")

    all_achievements = set(ACHIEVEMENTS)
    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
