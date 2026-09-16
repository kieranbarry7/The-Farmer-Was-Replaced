# this seeds a cactus at the current position, tilling the ground if required.

def seed_cactus():
    if get_ground_type() != Grounds.Soil:
        till()

    plant(Entities.Cactus)

# this function navigates the drone to a specified (x, y) coordinate, mapping to the world size.

def navigate_to(x, y = None):
    if y == None:
        x, y = x[0], x[1]

    world_size = get_world_size()

    mx = x - get_pos_x()
    my = y - get_pos_y()

    if 2 * mx > world_size:
        mx -= world_size

    if 2 * mx < -world_size:
        mx += world_size

    if 2 * my > world_size:
        my -= world_size

    if 2 * my < -world_size:
        my += world_size

    if mx >= 0:
        for step in range(mx):
            move(East)
    else:
        for step in range(-mx):
            move(West)

    if my >= 0:
        for step in range(my):
            move(North)
    else:
        for step in range(-my):
            move(South)