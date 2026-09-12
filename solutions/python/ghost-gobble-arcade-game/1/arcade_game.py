""" this function defines that if the pacman eats the ghost or not
parameters:
*power_pallet_status (bool) = it tells that the power pallet of pacman is active or not
*touching_ghost (bool) = it tells that the pacman is touching the ghost or not
returns true only if the pacman is eating the ghost otherwise false"""
def eat_ghost(power_pallet_status,touching_ghost):
    return power_pallet_status and touching_ghost
""" this function defines the score of pacman
parameters:
*power_pallet_status (bool) = it tells that the power pallet of pacman is active or not
*dot_status (bool) = it tells that the pacman is touching the dot or not.
returns true only if the pacman is touching the power pallet or a dot"""
def score(power_pallet_status,dot_status):
    return power_pallet_status or dot_status
""" this functions defines that if pacman loses or not
parameters:
*power_pallet_status (bool) = it tells that the power pallet of pacman is active or not
*ghost_status (bool) = it tells that the pacman is touching the ghost or not
return true if Pac-Man is touching a ghost and does not have a power pellet active"""
def lose(power_pallet_status,ghost_status):
    return ghost_status and not power_pallet_status
def win(eaten_all_dots,power_pallet_status,ghost_status):
    return eaten_all_dots and power_pallet_status or not ghost_status
    
