clear()

# set to grid of preference, this is preset to 32x32 for the longest dinosaur path possible.
set_world_size(32)

change_hat(Hats.Dinosaur_Hat)

# starting the farm_bones function, which will sweep the entire grid in a zig-zag pattern to collect bones.
def farm_bones():
	n = get_world_size()
	
	# loops through each column in the specified grid moving up and down to collect bones, changing hats if blocked by a wall.
	for x in range(n):
		if x % 2 == 0:
			target_y = n - 1
			dir_vertical = North
		else:
			target_y = 1
			dir_vertical = South

		# Vertical column sweep
		while get_pos_y() != target_y:
			if can_move(dir_vertical):
				move(dir_vertical)
			else:
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)

		# Step East to next column
		if x < n - 1:
			if can_move(East):
				move(East)
			else:
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)

	# returns from along the bottom row to the starting position (0, 0) to repeat the process.
	while get_pos_y() > 0:
		if can_move(South):
			move(South)
			
	while get_pos_x() > 0:
		if can_move(West):
			move(West)

while True:
	farm_bones()