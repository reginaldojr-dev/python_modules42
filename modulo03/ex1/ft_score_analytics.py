import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = []

    for parameter in sys.argv[1:]:
        try:
            scores.append(int(parameter))
        except ValueError:
            print(f"Invalid parameter: '{parameter}'")

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total = sum(scores)
    average = total / len(scores)
    high_score = max(scores)
    low_score = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
