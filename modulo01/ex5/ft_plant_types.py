#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/07 13:14:06 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/18 17:44:15 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float
    ) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate

        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, days: int = 1) -> None:
        self._height += self._growth_rate * days

    def age(self, days: int = 1) -> None:
        self._age += days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age = age

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self) -> None:
        self.shade = True

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

        if self.shade:
            print(
                f"Tree {self.name} now produces a shade of "
                f"{self._height}cm long and "
                f"{self.trunk_diameter}cm wide."
            )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.5, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.1, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    tomato.grow(20)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
