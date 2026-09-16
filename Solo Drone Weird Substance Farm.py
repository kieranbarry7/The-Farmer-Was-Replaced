# Farm Weird_Substance using Trees and Fertilizer

def farm_weird_substance_grid():
	world_size = get_world_size()
	
	for x in range(world_size):
		for y in range(world_size):
			move_to(x, y)
			
			# Prepare ground
			if get_ground_type() != Grounds.Soil:
				till()
				
			entity = get_entity_type()
			
			# Plant Tree if empty
			if entity == None:
				plant(Entities.Tree)
				use_item(Items.Fertilizer)
			elif can_harvest():
				# Harvest the infected tree to collect Weird_Substance
				harvest()
				plant(Entities.Tree)
				use_item(Items.Fertilizer)
			else:
				# If already planted, ensure it gets fertilized
				use_item(Items.Fertilizer)

def move_to(target_x, target_y):
	# Grid navigation helper
	while get_pos_x() != target_x:
		if get_pos_x() < target_x:
			move(East)
		else:
			move(West)
			
	while get_pos_y() != target_y:
		if get_pos_y() < target_y:
			move(North)
		else:
			move(South)

# --- Main Loop ---
while True:
	farm_weird_substance_grid()