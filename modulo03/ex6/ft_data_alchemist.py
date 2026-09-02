import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    capitalized_players = [name.capitalize() for name in players]
    already_capitalized = [
        name for name in players if name == name.capitalize()
    ]

    scores = {
        name: random.randint(0, 1000)
        for name in capitalized_players
    }

    average = sum(scores.values()) / len(scores)
    high_scores = {
        name: score
        for name, score in scores.items()
        if score > average
    }

    print(f"Initial list of players: {players}")
    print(
        "New list with all names capitalized: "
        f"{capitalized_players}"
    )
    print(
        "New list of capitalized names only: "
        f"{already_capitalized}"
    )
    print(f"Score dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
