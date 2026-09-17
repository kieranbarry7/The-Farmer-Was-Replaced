# this script is designed to multi drone farm wood via trees using a grid pattern to ensure efficient planting and harvesting of trees in the farm grid
clear()
world_size = get_world_size()
change_hat(Hats.Brown_Hat)

# mapping directories
companion_mapping = {}
tree_mapping = {}

# this function determines whether the current tile is suitable for planting a tree based on its coordinates
def tree_tile(current_x, current_y):
	return current_x % 2 == current_y % 2

# this function tracks the companion entity associated with a specific tree tile to ensure correct planting and harvesting of trees in the farm grid
def track_companion(current_x, current_y):
	global companion_mapping
	global tree_mapping
	
	result = get_companion()
	
	if result == None:
		return False
		
	target_entity, (target_x, target_y) = result

	if (target_x, target_y) not in companion_mapping:
		companion_mapping[(target_x, target_y)] = target_entity
		tree_mapping[(current_x, current_y)] = (target_x, target_y) 
		return True
		
	return False

# this function is responsible for scoping the farm size, harvesting trees, and planting new trees in the farm grid
def drone_tree_task():
	global world_size
	global companion_mapping
	global tree_mapping
	
	while True: 
		for j in range(world_size):
			currrent_x = get_pos_x()
			current_y = get_pos_y()
			
			if tree_tile(current_x, current_y):
				if can_harvest():
					harvest()
					plant(Entities.Tree)
				else:
					pass
				
				if (current_x, current_y) in tree_mapping:
					companion_pos = tree_mapping.pop((current_x, current_y))
					if companion_pos in companion_mapping:
						companion_mapping.pop(companion_pos)

				track_companion(current_x, current_y)
				
				if get_water() < 0.40: 
					use_item(Items.Water)
					
			elif (current_x, current_y) in companion_mapping:
				target_entity = companion_mapping[(current_x, current_y)]
				harvest()
				
				if target_entity == Entities.Grass:
					if get_ground_type() != Grounds.Grassland:
						till()
						
				elif target_entity == Entities.Carrot:
					if get_ground_type() != Grounds.Soil:
						till()

				plant(target_entity)
				
			else:
				harvest()
				plant(Entities.Bush)
				
			move(North)

# this section is responsible for spawning drones to assist with the farming of trees in the farm grid
NUM_DRONES_TO_SPAWN = 31 

for i in range(NUM_DRONES_TO_SPAWN):
	
	while num_drones() >= max_drones():
		pass 

	spawn_drone(drone_tree_task)
	move(East)

drone_tree_task()