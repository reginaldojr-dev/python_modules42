import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = raw.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coordinates: list[float] = []
        valid = True

        for part in parts:
            clean = part.strip()
            try:
                coordinates.append(float(clean))
            except ValueError as error:
                print(f"Error on parameter '{clean}': {error}")
                valid = False
                break

        if valid:
            return (coordinates[0], coordinates[1], coordinates[2])


def distance(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    center = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(distance(first, center), 4)}")

    print("Get a second set of coordinates")
    second = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance(first, second), 4)}"
    )


if __name__ == "__main__":
    main()
