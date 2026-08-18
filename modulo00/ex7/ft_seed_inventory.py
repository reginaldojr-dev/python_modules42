# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/04 16:02:01 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:17:47 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    upper = seed_type.capitalize()
    if unit == "packets":
        phrase = upper + ": " + str(quantity) + " packets available"
    elif unit == "grams":
        phrase = upper + ": " + str(quantity) + " grams total"
    elif unit == "area":
        phrase = upper + ": " + "covers " + str(quantity) + " square meters"
    else:
        phrase = "Unknown unit type"
    print(f"{phrase}")
