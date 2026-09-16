while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			
		if get_pos_x()%2 == 0 and get_pos_y()%2 == 0:
			plant(Entities.Tree)
		elif get_pos_x()%2 == 1 and get_pos_y()%2 == 1:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		if get_water() <= 0.65:
			use_item(Items.Water)
		move(North)
	move(East)
				