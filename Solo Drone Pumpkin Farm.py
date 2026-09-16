# till the entire plot in relation to world size.
for i in range(get_world_size()):
	for i in range(get_world_size()):
		till()
		move(North)
	move(East)

# plant, water and harvest pumpkins in a loop, ensuring that the entire plot is maintained and harvested as required.
while True:
	for i in range(get_world_size()):
		for i in range(get_world_size()): 
			if can_harvest():
				harvest()
			plant(Entities.Pumpkin)
			if get_water() <= 0.90:
				use_item(Items.Water)
			move(North)
		move(East)
	
# loop that continues until the entire plot has been harvested and maintained, ensuring that all pumpkins are planted, watered, and harvested as required.
	pumpkin_num = 0
	while pumpkin_num < get_world_size()**2:
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
					plant(Entities.Pumpkin)
				if get_water() <= 0.90:
					use_item(Items.Water)
					use_item(Items.Fertilizer)
				else:
					pumpkin_num += 1
			move(North)
		move(East)