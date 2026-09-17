# Cannot be MF due to the dino hat being limited to one drone
def move_to(x, y):

	while get_pos_x() != x:

		if get_pos_x() < x:
			if not move(East):
				return False
		else:
			if not move(West):
				return False

	while get_pos_y() != y:

		if get_pos_y() < y:
			if not move(North):
				return False
		else:
			if not move(South):
				return False

	return True


def dinosaur():

	change_hat(Hats.Dinosaur_Hat)

	while True:

		apple_x, apple_y = measure()

		if not move_to(apple_x, apple_y):
			break

	change_hat(Hats.Straw_Hat)


clear()

while True:
	dinosaur()