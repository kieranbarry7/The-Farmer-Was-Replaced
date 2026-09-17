# this script contains functions and mathematics derived from the TFWR open-source community to solely help with the farming of pumpkins in a highly optimised pattern. 
# it additionally contains the scripting for all other entities and companion plants that can be found in the game and how to handle them.
# imports pumpkin movement patterns and commands for scoping the grid and plotting movement
import pumpkin_commands

# this function checks for recursion in import pumpkin_commands and handles companion plant and entity if no recursion is detected.
def handle_plant_by_entity(entity, recursion=False):
	if not recursion:
		handle_companion_plant()

	if entity == Entities.Grass:
		handle_grass_plant(True)
	if entity == Entities.Bush:
		handle_bush_plant(True)
	if entity == Entities.Tree:
		handle_tree_plant(True)
	if entity == Entities.Carrot:
		handle_carrot_plant(True)
	if entity == Entities.Pumpkin:
		handle_pumpkin_plant(True)
	if entity == Entities.Cactus:
		handle_cactus_plant(True)
	if entity == Entities.Sunflower:
		handle_sunflower_plant(True)


def handle_companion_plant():
	if get_companion() == None:
		return

# this finds the companion plant and moves the drone to the companion plant's coordinates, handles the companion plant, and then returns to the original position.
	cx = get_pos_x()
	cy = get_pos_y()
	plant_type, (x, y) = get_companion()
	commands.goto_fast((x + 1), (y + 1))
	handle_plant_by_entity(plant_type, True)
	commands.goto_fast((cx + 1), (cy + 1))


# the following functions handles the planting of all entities and harvesting all said types. Additionally checks for water levels and tills the ground if necessary for certain required entities.

def handle_bush_plant(recursion=False):
	handle_harvest(recursion)
	if get_ground_type() != Grounds.Grassland:
		till()
	plant(Entities.Bush)


def handle_tree_plant(recursion=False):
	handle_harvest(recursion)
	if get_ground_type() != Grounds.Grassland:
		till()
	plant(Entities.Tree)


def handle_carrot_plant(recursion=False):
	handle_harvest(recursion)
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)


def handle_grass_plant(recursion=False):
	handle_harvest(recursion)
	if get_ground_type() != Grounds.Grassland:
		till()
	plant(Entities.Grass)


def handle_cactus_plant(recursion=False):
	handle_harvest(recursion)
	if (get_water() < 0.25):
		use_item(Items.Water)
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)


def handle_sunflower_plant(recursion=False):
	handle_harvest(recursion)
	if get_water() < 0.25:
		use_item(Items.Water)
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)


def handle_harvest(recursion=True):
	if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
		if not recursion:
			handle_companion_plant()
		harvest()


def handle_pumpkin_plant(recursion=False, no_harvest=False):
	if not no_harvest:
		handle_harvest(recursion)
	if get_water() < 0.5:
		use_item(Items.Water)
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)


# this function handles the planting of a square of plants in a zig-zag pattern, starting from a given (x, y) coordinate and moving in a specified direction. 
def handle_square_plant(start_x, start_y, map_size=get_world_size(), action=do_a_flip(), direction=0):
	# the following are the numerical directions:
	# 0: top right --> bottom left
	# 1: top left --> bottom right
	# 2: bottom right --> top left
	# 3: bottom left --> top right
	if direction == 0:
		for s in range(2 * start_x, -1, -1):
			y_range = range(start_y)
			if s % 2 == 0:
				y_range = range(start_y - 1, -1, -1)
			for y in y_range:
				x = s - y
				if 0 <= x < start_x and x >= (start_x - map_size) and y >= (start_y - map_size):
					commands.goto_fast((x + 1), (y + 1))
					action()

	elif direction == 1:
		for s in range(start_x + start_y, start_x + start_y + 2 * map_size):
			y_range = range(start_y, start_y + map_size)
			if s % 2 == 0:
				y_range = range(start_y + map_size, start_y - 1, -1)

			for y in y_range:
				x = s - y
				if start_x <= x < (start_x + map_size) and start_y <= y < (start_y + map_size):
					inverted_y = 2 * start_y - y
					if inverted_y > (start_y - map_size):
						commands.goto_fast(x, inverted_y)
						action()

	elif direction == 2:
		for s in range(start_x - start_y, start_x - start_y - 2 * map_size, -1):
			y_range = range(start_y, start_y + map_size)
			if s % 2 == 0:
				y_range = range(start_y + map_size - 1, start_y - 1, -1)

			for y in y_range:
				x = s + y
				if (start_x - map_size) <= x < start_x and start_y <= y < (start_y + map_size):
					commands.goto_fast((x + 1), y)
					action()

	elif direction == 3:
		for s in range(start_x + start_y, start_x + start_y + 2 * map_size):
			y_range = range(start_y, start_y + map_size)
			if s % 2 == 0:
				y_range = range(start_y + map_size - 1, start_y - 1, -1)

			for y in y_range:
				x = s - y
				if start_x <= x < (start_x + map_size) and start_y <= y < (start_y + map_size):
					commands.goto_fast(x, y)
					action()
	else:
		return