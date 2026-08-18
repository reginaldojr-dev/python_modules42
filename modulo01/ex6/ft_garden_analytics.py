#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/18 14:55:48 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/18 20:18:36 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate
        self._statistics = self.Statistics()

        self.set_height(height)
        self.set_age(age)

    class Statistics:
        def __init__(self):

            self._grow_uses = 0
            self._age_uses = 0
            self._show_uses = 0

        def count_grow(self):
            self._grow_uses += 1

        def count_age(self):
            self._age_uses += 1

        def count_show(self):
            self._show_uses += 1

    def show_statistics(self):
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self._statistics._grow_uses} grow, "
              f"{self._statistics._age_uses} age, "
              f"{self._statistics._show_uses} show")

    def show(self):
        print(f"{self.name}: {round(self._height)}cm, {self._age} days old")
        self._statistics.count_show()

    def grow(self):
        self._height = self._height + self._growth_rate
        self._statistics.count_grow()

    def age(self, days):
        self._age = self._age + days
        self._statistics.count_age()

    def set_height(self, height):
        if height < 0:
            return
        else:
            self._height = height

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age < 0:
            return
        else:
            self._age = age

    def get_age(self):
        return self._age

    @staticmethod
    def more_than_year(days):
        return days > 365

    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant", 0.0, 0, 0.0)


class Flower(Plant):
    def __init__(self, name, height, age, growth_rate, color):
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name, height, age, growth_rate, color):
        super().__init__(name, height, age, growth_rate, color)
        self.seed_count = 0

    def bloom(self):
        super().bloom()
        self.seed_count = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seed_count}")


class Tree(Plant):
    def __init__(self, name, height, age, growth_rate, trunk_diameter):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    class Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self._shades_uses = 0

        def count_shades(self):
            self._shades_uses += 1

    def produce_shade(self):
        self.shade = True
        self._statistics.count_shades()

    def show_statistics(self):
        super().show_statistics()
        print(f"{self._statistics._shades_uses} shade")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        if self.shade:
            print(f"Tree {self.name} now produces a shade of "
                  f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, age, growth_rate, harvest_season):
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self):
        super().age()
        self.nutritional_value += 1

    def show(self):
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

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    rose.show_statistics()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.1, 5.0)
    oak.show()
    oak.show_statistics()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()
    oak.show_statistics()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.show()
    sunflower.show_statistics()

    print("=== Anonimous")
    Plant.anonymous_plant()


if __name__ == "__main__":
    main()
