#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/23 17:51:28 by tny-onin            #+#    #+#            #
#   Updated: 2026/04/18 09:40:45 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive() -> None:
    d = int(input("Days until harvest : "))

    def ft_count_harvest(n: int, d: int) -> None:
        if n > d:
            print("Harvest time!")
            return
        print("Day ", n)
        ft_count_harvest(n + 1, d)
    ft_count_harvest(1, d)
