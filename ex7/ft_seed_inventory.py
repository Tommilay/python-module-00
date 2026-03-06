# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tny-onin <tny-onin@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/05 17:47:50 by tny-onin          #+#    #+#              #
#    Updated: 2026/03/05 17:48:34 by tny-onin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit += " available"
    elif unit == "grams":
        unit += " total"
    elif unit == "area":
        unit += " square meters"
    else:
        unit = "Unknown unit type"
    print(seed_type, ": ", quantity, ": ", unit)
