#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/06 18:36:30 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/18 17:41:43 by rgoulart           ###   ########.fr      #
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
        self._height = 0.0
        self._age = 0

        if height >= 0:
            self._height = height

        if age >= 0:
            self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = height
        print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age = age
        print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)

    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-1)
    rose.set_age(-1)

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
