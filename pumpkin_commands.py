# this script contains functions and mathematics derived from the TFWR open-source community to help with the farming of pumpkins.
# uses TFWR import function to import the custom math module from the library
import pumpkin_custom_math

# function to get the opposite direction of a given direction
def get_opposite(direction):
	if direction == North:
		return South
	elif direction == South:
		return North
	elif direction == East:
		return West
	else:
		return East

# function to move the drone to the starting position (0, 0) on the map to start the farm
def goto_start():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

# function to continue walking in a zig-zag pattern across the map
def continue_walk():
	map_size = get_world_size()
	if get_pos_y() == (map_size - 1):
		move(East)
	move(North)

# function to move the drone to a specific (x, y) coordinate on the map
def goto(x, y):
	cx = get_pos_x()
	cy = get_pos_y()

	px = x - 1
	py = y - 1

	if cx != px:
		while get_pos_x() < px:
			move(East)
		while get_pos_x() > px:
			move(West)

	if cy != py:
		while get_pos_y() < py:
			move(North)
		while get_pos_y() > py:
			move(South)

# function to move the drone to a specific (x, y) coordinate on the map using the shortest path
def goto_fast(x, y):
	map_size = get_world_size()

	cx = get_pos_x() + 1
	cy = get_pos_y() + 1

	if x > cx:
		steps_to_left = map_size + cx - x
		steps_to_right = x - cx
	else:
		steps_to_right = map_size - cx + x
		steps_to_left = cx - x

	if y > cy:
		steps_to_downside = map_size + cy - y
		steps_to_upside = y - cy
	else:
		steps_to_upside = map_size - cy + y
		steps_to_downside = cy - y

	if steps_to_right > steps_to_left:
		for i in range(steps_to_left):
			move(West)
	else:
		for i in range(steps_to_right):
			move(East)

	if steps_to_upside > steps_to_downside:
		for i in range(steps_to_downside):
			move(South)
	else:
		for i in range(steps_to_upside):
			move(North)

# function to calculate the (x, y) position of a point on a circle based on its index and the total number of points
def get_circle_position(index, total, gap=4):
	map_size = get_world_size()
	pi = 3.14159265359
	radius = map_size / 2 - gap
	angle = (2 * pi * index) / total
	center_x = map_size / 2
	center_y = map_size / 2
	start_x = (center_x + radius * pumpkin_custom_math.cos(angle)) // 1
	start_y = (center_y + radius * pumpkin_custom_math.sin(angle)) // 1

	return start_x, start_y


def goto_circle_position(index, total, gap=4):
	start_x, start_y = get_circle_position(index, total, gap)
	goto_fast(start_x + 1, start_y + 1)