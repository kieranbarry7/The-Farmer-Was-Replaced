clear()

world_size = get_world_size()

change_hat(Hats.Brown_Hat)

# this function is responsible for scoping the farm size, harvesting sunflowers, and planting new sunflowers in the farm grid
def drone_sunflower_task():
	while True:
		for i in range(world_size):

			if can_harvest():
				harvest()

			if get_ground_type() != Grounds.Soil:
				till()

			if get_entity_type() != Entities.Sunflower:
				plant(Entities.Sunflower)

			if get_water() < 0.40:
				use_item(Items.Water)

			move(North)

# this section is responsible for spawning drones to assist with the farming of sunflowers in the farm grid

NUM_DRONES_TO_SPAWN = max_drones() - 1

for i in range(NUM_DRONES_TO_SPAWN):
	while num_drones() >= max_drones():
		pass

	spawn_drone(drone_sunflower_task)
	move(East)


drone_sunflower_task()