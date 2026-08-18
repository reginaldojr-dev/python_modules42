#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/07 13:14:06 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/07 13:14:06 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self._height)}cm, {self._age} days old")

    def grow(self):
        self._height = self._height + self._growth_rate

    def age(self):
        self._age = self._age + 1

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_age(self):
        return self._age


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


class Tree(Plant):
    def __init__(self, name, height, age, growth_rate, trunk_diameter):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self):
        self.shade = True

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
    for day in range(1, 21):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
