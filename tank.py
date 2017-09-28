from bullet import Bullet
import math

class Tank():
	def __init__(self,internal_id,game):
		self.id = internal_id
		self.game = game

		self.health = 100

		self.rotation = 180                 # Current rotation of tank
		self.rotation_delta = 6             # How many degrees tank rotates (should ideally divide into 360 evenly)
		self.turret_rotation = 0            # Current rotation of turret
		self.turret_rotation_delta = 11.25  # How many degrees turret rotates (should ideally divide into 360 evenly)
		self.fire_rate = 2                  # How many seconds in between firings (lower number = faster firing)

		self.alive = True
		self.moving = False

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
		if self.speed < self.max_speed_fwd:
			self.speed += self.speed_delta

	# Decrease speed
	def down(self):
		if self.speed > self.max_speed_rev:
			self.speed -= self.speed_delta

		else:
			self.speed = self.max_speed_rev

	# Fire them guns
	def fire(self):
		# TODO: Need to fix position issue
		# Also need to check fire rate

		pos = self.position

		# 31 = half of width of tank (74/2 = 37) - width of bullet (6)
		#bullet = Bullet([pos[0]+31,pos[1]],self.rotation,self)
		'''x, y = position
		rad = rotation * math.pi / -180

		x += speed * math.sin(rad)
		y += speed * math.cos(rad)'''
		r = self.rotation * math.pi / -180

		x = pos[0] + (31 * math.sin(r))
		y = pos[0] + (1 * math.cos(r))

		#bullet = Bullet([x,y],self.rotation,self)
		bullet = Bullet(self.position,self.rotation,self)

		# Add to level
		self.game.level.add_bullet(bullet)

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

