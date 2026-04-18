#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/05 16:37:06 by tny-onin            #+#    #+#            #
#   Updated: 2026/04/18 09:33:30 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative() -> None:
    d = int(input("Days until harvest : "))
    x = range(1, d + 1)
    for n in x:
        print("day ", n)
    print("Harvest time!")
