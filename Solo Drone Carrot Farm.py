clear()

# tills the entire plot in relation to world size.
for i in range(get_world_size()):
	for i in range(get_world_size()):
		till()
		move(North)
	move(East)
	
#planting the carrots, watering them if required, and harvesting them in a loop, ensuring that the entire plot is maintained and harvested as required.
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		plant(Entities.Carrot)
		if get_water() <= 0.75:
			use_item(Items.Water)
		move(North)
	move(East)