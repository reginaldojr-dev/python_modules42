#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/06 14:13:21 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:13:21 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25.0, 30)
    sunflower = Plant("Sunflower", 80.0, 45)
    cactus = Plant("Cactus", 15.0, 120)

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
