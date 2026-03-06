# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tny-onin <tny-onin@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/05 17:24:25 by tny-onin          #+#    #+#              #
#    Updated: 2026/03/05 17:31:57 by tny-onin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name : ")
    nb_plants = int(input("Enter number of plants : "))
    print("Garden: ", name, end="\n")
    print("Plants: ", nb_plants, end="\n")
    print("Status: Growing well!")
