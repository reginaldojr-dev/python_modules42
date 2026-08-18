# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/04 14:47:04 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:16:55 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for current_day in range(1, days + 1):
        print(f"Day {current_day}")
    print("Harvest time!")
