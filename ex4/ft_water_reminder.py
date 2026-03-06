# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tny-onin <tny-onin@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/05 16:30:47 by tny-onin          #+#    #+#              #
#    Updated: 2026/03/05 16:34:45 by tny-onin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering : "))
    if days > 2 :
        print("Water the plants!")
    else :
        print("Plants are fine")

ft_water_reminder()