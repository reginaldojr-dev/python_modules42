#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 17:24:06 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/27 17:03:35 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        15 / 0
    elif operation_number == 2:
        open("arquivo_que_nao_existe.txt", "r")
    elif operation_number == 3:
        "abc" + 1
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")
    for operation in range(0, 5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        else:
            garden_operations(operation)
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
