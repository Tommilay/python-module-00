# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tny-onin <tny-onin@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/05 16:21:41 by tny-onin          #+#    #+#              #
#    Updated: 2026/03/05 16:24:50 by tny-onin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest : "))
    day2 = int(input("Day 2 harvest : "))
    day3 = int(input("Day 3 harvest : "))
    print("Total harvest : ", day1 + day2 + day3)
