# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/06 14:15:48 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:16:35 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_days(current_day):
        if current_day > days:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        count_days(current_day + 1)
    count_days(1)
