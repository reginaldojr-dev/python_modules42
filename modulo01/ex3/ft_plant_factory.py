#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/06 17:44:02 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 17:44:02 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int
    ) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    clove = Plant("Clove", 15.0, 20)
    daisy = Plant("Daisy", 30.0, 35)
    sunflower = Plant("Sunflower", 35.0, 32)
    tulip = Plant("Tulip", 13.0, 27)
    oak = Plant("Oak", 200.0, 365)
    fern = Plant("Fern", 15.0, 120)

    plants = [
        rose,
        clove,
        daisy,
        sunflower,
        tulip,
        oak,
        fern
    ]

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
