#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/20 13:14:06 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/26 17:44:15 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    try:
        print("Input data is '25'")
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    try:
        print("Input data is 'abc'")
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    try:
        print("Input data is '100'")
        temperature = input_temperature("100")
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    try:
        print("Input data is '-50'")
        temperature = input_temperature("-50")
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
