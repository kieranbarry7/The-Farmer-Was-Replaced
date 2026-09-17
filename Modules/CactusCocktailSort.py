# this code is for a cactus import function that will plant cacti in a column and sort them using cocktail sort (variation of a bubble sort). It uses the utils module for movement and planting functions.
import UtilsMDCactus as utils


# initialises the world size and sets the hat to a cactus hat for planting.

def plant_column(x):
	utils.move_to(x, 0)

	for y in range(get_world_size()):
		if get_entity_type() != Entities.Cactus:
			harvest()

		utils.plant_cactus()

		move(North)

# cocktail sort function that sorts the cacti in a column using a bidirectional bubble sort algorithm. It can sort either north-south or east-west based on the north_south parameter.

def cocktail_sort(x, north_south=True):

	def move_to_yx(x, y):
		utils.move_to(y, x)

	if north_south:
		move_fn = utils.move_to
		direction = North
	else:
		move_fn = move_to_yx
		direction = East

	start = 0
	end = get_world_size() - 1

	while start < end:

		swapped = False

		for j in range(start, end):

			move_fn(x, j)

			if measure() > measure(direction):
				swap(direction)
				swapped = True

		if not swapped:
			break

		swapped = False

		end -= 1

		for j in range(end - 1, start - 1, -1):

			move_fn(x, j)

			if measure() > measure(direction):
				swap(direction)
				swapped = True

		if not swapped:
			break

		start += 1