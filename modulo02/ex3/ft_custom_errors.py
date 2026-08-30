#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 17:24:06 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/27 17:03:35 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_plant_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_water_errors() -> None:
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        check_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    test_plant_errors()
    print("")

    test_water_errors()
    print("")

    test_garden_errors()
    print("")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
