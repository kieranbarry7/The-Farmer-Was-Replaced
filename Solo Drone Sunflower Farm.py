clear()

world_size = get_world_size()

change_hat(Hats.Brown_Hat)


def sunflower_task():
	global world_size

	while True:
		for j in range(world_size):

			if can_harvest():
				harvest()

			if get_ground_type() != Grounds.Soil:
				till()

			if get_entity_type() != Entities.Sunflower:
				plant(Entities.Sunflower)

			if get_water() < 0.40:
				use_item(Items.Water)

			move(North)


sunflower_task()