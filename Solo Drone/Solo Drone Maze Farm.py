# maze farm cant be a mega farm due to the RNG of Maze placement as a maze is centred around the drone that creates it creating another maze destroys any existing maze that the new maze overlaps.

def spawn_maze():
	if get_ground_type() != Grounds.Soil:
		till()
	harvest()
	plant(Entities.Bush)
	size = get_world_size()
	use_item(Items.Weird_Substance, size)

def solve_maze():
	dirs = [North, East, South, West]
	facing = 0
	while get_entity_type() != Entities.Treasure:
		left = (facing - 1) % 4
		if can_move(dirs[left]):
			facing = left
			move(dirs[facing])
		elif can_move(dirs[facing]):
			move(dirs[facing])
		else:
			facing = (facing + 1) % 4
	harvest()

clear()
while True:
	spawn_maze()
	solve_maze()
	