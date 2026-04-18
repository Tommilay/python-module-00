#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/05 16:30:47 by tny-onin            #+#    #+#            #
#   Updated: 2026/04/18 09:33:14 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    days = int(input("Days since last watering : "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
