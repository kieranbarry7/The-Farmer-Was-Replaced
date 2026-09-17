# this script farms weird substance using more than one drone and a tree as the base for farming.

clear()

world_size = get_world_size()

change_hat(Hats.Brown_Hat)

# this function is responsible for scoping the farm size, harvesting trees, and planting new trees in the farm grid whilst infecting it for the weird substance
def drone_weird_task():

	while True:

		for i in range(world_size):

			# if the tree has matured enough then harvest the tree, replant it, and infect it for the weird substance
			if can_harvest():
				harvest()
				plant(Entities.Tree)

				# infects the tree for the weird substance if the player has fertilizer in their inventory
				if num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)

			else:

			
				if get_entity_type() == None:
					plant(Entities.Tree)

				
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)

				# if the tree already exists, keep fertilizing it
				elif num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)

			# Move to the next tile in this drone's column
			move(North)


# spawns every available drone except the main drone for efficiency
NUM_DRONES_TO_SPAWN = max_drones() - 1


for i in range(NUM_DRONES_TO_SPAWN):

	while num_drones() >= max_drones():
		pass

	spawn_drone(drone_weird_task)

	# makes the drone move right to the next column in the farm grid
	move(East)


# Main drone farms the final column
drone_weird_task()