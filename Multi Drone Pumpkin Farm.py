# this script contains functions and mathematics derived from the TFWR open-source community to help with the farming of pumpkins

# importing the pumpkin_commands and plantHandlers modules to use their functions in this script
import pumpkin_commands
import plantHandlers

# this initalises a progress tracking mechanism to monitor soil preparation or plant growth across the farm grid
counter = 0
current_world = get_world_size()
init_counter = current_world * current_world * 4


# this function looks for the entity type "Pumpkin" and then plants a pumpkin and fertilises said square in grid
# if the square in grid is occupied with an entity which isnt a Pumpkin, then it continues
def action():
	while get_entity_type() != Entities.Pumpkin:
		plantHandlers.handle_pumpkin_plant(True, get_entity_type() == Entities.Pumpkin)
		use_item(Items.Fertilizer)
		while not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
			continue

# this function allows for managing the planting process across the farm grid in conjunction to the imported modules.
def planter():
	global counter

	counter += 1
	if counter < 4:
		spawn_drone(planter)

	square = current_world // 2
	if current_world % 2 != 0:
		square += 1

	if counter % 4 == 0:
		plantHandlers.handle_square_plant(current_world, current_world, square, action, 0)
	elif counter % 3 == 0:
		plantHandlers.handle_square_plant(1, 1, square, action, 3)
	elif counter % 2 == 0:
		plantHandlers.handle_square_plant(current_world, 1, square, action, 2)
	elif counter % 1 == 0:
		plantHandlers.handle_square_plant(1, current_world, square, action, 1)

	if num_drones() == 1:
		while not can_harvest():
			continue

		harvest()
		counter = 0
		commands.goto_fast(current_world // 2, current_world // 2)
		spawn_drone(planter)



spawn_drone(planter)