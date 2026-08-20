#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/18 14:55:48 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/20 17:00:55 by rgoulart           ###   ########.fr      #
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
        self._statistics = self.Statistics()

        self.set_height(height)
        self.set_age(age)

    class Statistics:
        def __init__(self) -> None:
            self._grow_uses = 0
            self._age_uses = 0
            self._show_uses = 0

        def count_grow(self) -> None:
            self._grow_uses += 1

        def count_age(self) -> None:
            self._age_uses += 1

        def count_show(self) -> None:
            self._show_uses += 1

    def show_statistics(self) -> None:
        print(f"[statistics for {self.name}]")
        print(
            f"Stats: {self._statistics._grow_uses} grow, "
            f"{self._statistics._age_uses} age, "
            f"{self._statistics._show_uses} show"
        )

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height)}cm, "
            f"{self._age} days old"
        )
        self._statistics.count_show()

    def grow(self, days: int = 1) -> None:
        self._height += self._growth_rate * days
        self._statistics.count_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self._statistics.count_age()

    def set_height(self, height: float) -> None:
        if height < 0:
            return
        self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            return
        self._age = age

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def more_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


def display_statistics(plant: Plant) -> None:
    plant.show_statistics()


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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str
    ) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self.seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")


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
        self._statistics: Tree.Statistics = self.Statistics()
        self._trunk_diameter = trunk_diameter
        self._shade = False

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_uses = 0

        def count_shade(self) -> None:
            self._shade_uses += 1

    def produce_shade(self) -> None:
        self._shade = True
        self._statistics.count_shade()

    def show_statistics(self) -> None:
        super().show_statistics()
        print(f"{self._statistics._shade_uses} shade")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

        if self._shade:
            print(
                f"Tree {self.name} now produces a shade of "
                f"{self._height}cm long and "
                f"{self._trunk_diameter}cm wide."
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


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.more_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.more_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.5, "red")
    rose.show()
    rose.show_statistics()

    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(16)
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.1, 5.0)
    oak.show()
    oak.show_statistics()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()
    oak.show_statistics()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 1.5, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(20)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    sunflower.show_statistics()

    print("=== Anonimous")
    anonymous = Plant.anonymous_plant()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
