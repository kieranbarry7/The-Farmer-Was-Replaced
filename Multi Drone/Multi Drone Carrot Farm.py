clear()

world_size = get_world_size()

change_hat(Hats.Carrot_Hat)

# this function runs a single drone through a column of carrots, harvesting, planting, and watering if required.

def run_carrot_column():
    global world_size

    while True:

        for step in range(world_size):

            # harvest carrot if there is one
            if can_harvest():
                harvest()

            # till the ground if it isn't soil
            if get_ground_type() != Grounds.Soil:
                till()

            # plant a carrot if there isn't one

            if get_entity_type() != Entities.Carrot:
                plant(Entities.Carrot)

            # keep the carrot watered to ensure maximum growth rate
            if get_water() < 0.40:
                use_item(Items.Water)

            # move to the next position in the column
            move(North)

# allocates max number of drones possible to run the function
TARGET_DRONE_COUNT = 31

for drone_idx in range(TARGET_DRONE_COUNT):

    while num_drones() >= max_drones():
        pass

    spawn_drone(run_carrot_column)

    move(East)


# main drone also farms a column
run_carrot_column()