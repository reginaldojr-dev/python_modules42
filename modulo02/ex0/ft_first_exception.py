#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/15 13:14:06 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/18 17:44:15 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
