# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/03 15:00:29 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:29:25 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total_harvest = day1 + day2 + day3
    print(f"Total harvest: {total_harvest}")
