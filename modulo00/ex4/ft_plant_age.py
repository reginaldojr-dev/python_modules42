# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/04 12:54:42 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:28:56 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age < 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
