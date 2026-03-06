# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tny-onin <tny-onin@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/05 16:37:06 by tny-onin          #+#    #+#              #
#    Updated: 2026/03/05 17:21:18 by tny-onin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    d = int(input("Days until harvest : "))
    x = range(1, d + 1)
    for n in x :
        print("day ", n)
    print("Harvest time!")


def ft_count_harvest_recursive():
    d = int(input("Days until harvest : "))
    def ft_count_harvest(n, d):
        if n > d :
            print("Harvest time!")
            return
        print("Day ", n)
        ft_count_harvest(n + 1, d)
    ft_count_harvest(1, d)