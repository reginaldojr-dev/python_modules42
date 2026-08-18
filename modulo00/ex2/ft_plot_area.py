# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: rgoulart <rgoulart@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/02 16:06:43 by rgoulart            #+#    #+#            #
#   Updated: 2026/08/06 14:29:44 by rgoulart           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")
