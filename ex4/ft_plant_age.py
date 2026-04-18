#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/05 16:26:32 by tny-onin            #+#    #+#            #
#   Updated: 2026/04/18 09:32:58 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age() -> None:
    age = int(input("Enter plant age in days : "))
    if age > 60:
        print("plant is ready to harvest!")
    else:
        print("plant needs more time to grow.")
