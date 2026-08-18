#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/06 14:44:49 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:44:49 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = height
        self.age_days = age
        self.growth_rate = growth_rate

    def grow(self):
        self.height = self.height + self.growth_rate

    def age(self):
        self.age_days = self.age_days + 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


def growth_simulation(plant):
    initial_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")

        plant.grow()
        plant.age()
        plant.show()

    total_growth = plant.height - initial_height
    print(f"Growth this week: {round(total_growth)}cm")


def main():
    rose = Plant("Rose", 25.0, 30, 0.5)
    clove = Plant("Clove", 15.0, 20, 0.1)
    daisy = Plant("Daisy", 30.0, 35, 0.8)
    sunflower = Plant("Sunflower", 35.0, 32, 0.7)
    tulip = Plant("Tulip", 13.0, 27, 0.3)

    choice = input("Choose a plant: (rose, clove, daisy, "
                   "sunflower, tulip): ").lower()

    if choice == "rose":
        growth_simulation(rose)
    elif choice == "clove":
        growth_simulation(clove)
    elif choice == "daisy":
        growth_simulation(daisy)
    elif choice == "sunflower":
        growth_simulation(sunflower)
    elif choice == "tulip":
        growth_simulation(tulip)
    else:
        print("Unknown plant")


if __name__ == "__main__":
    main()
