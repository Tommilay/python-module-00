#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/05 16:14:37 by tny-onin            #+#    #+#            #
#   Updated: 2026/04/18 09:32:13 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area() -> None:
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))
    print("Plot area ", (width * length))
