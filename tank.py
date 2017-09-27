class Tank():
	def __init__(self):

		self.x_delta = 10            # How much will we change on the x axis - no longer used
		self.y_delta = 10            # How much will we change on the y axis - no longer used
		self.health = 100

		self.alive = True
		self.moving = False

		self.rotation = 180
		self.rotation_delta = 11.25
		self.turret_rotation = 0
		self.turret_rotation_delta = 11.25

	# Handles movement
	# Rotate to the left
	def left(self):
		#self.report_rotation()
		if self.rotation >0:
			self.rotation -= self.rotation_delta

		else:
			self.rotation = (360 - self.rotation_delta)

		#self.report_rotation()

	# Rotate to the right
	def right(self):
		#self.report_rotation()

		if (self.rotation + self.rotation_delta) >= 360:
			self.rotation = 0

		else:
			self.rotation += self.rotation_delta

		#self.report_rotation()

	# Increase speed
	def up(self):
		if self.speed < self.max_speed:
			self.speed += self.speed_delta

		self.position = (self.position[0],self.position[1] - 10)

	# Decrease speed
	def down(self):
		if self.speed > self.speed_delta:
			self.speed -= self.speed_delta

		else:
			self.speed = 0

		self.position = (self.position[0],self.position[1] + 10)

	# Fire them guns
	def fire(self):
		print("Fire")

	# Rotate the turret to the right
	def turret_left(self):
		#self.report_turret_rotation()
		if self.turret_rotation >0:
			self.turret_rotation -= self.turret_rotation_delta

		else:
			self.turret_rotation = (360 - self.turret_rotation_delta)


		#self.report_turret_rotation()

	# Rotate the turret to the right
	def turret_right(self):
		#self.report_turret_rotation()

		if (self.turret_rotation + self.turret_rotation_delta) >= 360:
			self.turret_rotation = 0

		else:
			self.turret_rotation += self.turret_rotation_delta

		#self.report_turret_rotation()

	# Just report the rotation - used for debugging
	def report_rotation(self):
		print ("Current rotation is " + str(self.rotation))

	# Just report the turret rotation - used for debugging
	def report_turret_rotation(self):
		print ("Current turret rotation is " + str(self.turret_rotation))

