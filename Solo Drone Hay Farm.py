clear()

while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_water() <= 0.5:
			use_item(Items.Water)
		move(North)
	move(East)