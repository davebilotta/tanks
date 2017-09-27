class Enemy():
	def __init__(self):
		print ("Enemy Constructor")

		self.image = ""
		self.position = (100,100)
		self.speed = 10
		self.health = 100
		self.alive = True
		self.moving = False

		self.friendly = False
		self.enemy = True

	def get_position(self):
		return self.position

	def get_speed(self):
		return self.speed

	def get_health(self):
		return self.health

	def is_alive(self):
		return self.alive

	def is_moving(self):
		return self.moving
