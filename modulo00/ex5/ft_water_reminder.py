# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/04 14:31:35 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:15:23 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    last_watering = int(input("Days since last watering: "))
    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
