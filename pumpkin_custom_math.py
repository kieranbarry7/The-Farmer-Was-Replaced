# uses numerical approximation algorithm found via the TFWR open-source community for the movement of drones in farming pumpkins.

def sin(x):
	pi = 3.14159265359
	while x > pi:
		x -= 2 * pi
	while x < -pi:
		x += 2 * pi

	x2 = x * x
	return x * (1 - x2 / 6 * (1 - x2 / 20 * (1 - x2 / 42)))


def cos(x):
	pi = 3.14159265359
	return sin(x + pi / 2)