from bullet import Bullet
import math
import datetime
import pygame
from pygame.math import Vector2

class Tank():
	def __init__(self,internal_id,game,friendly=False):
		self.id = internal_id
		self.game = game
		self.friendly = friendly

		self.health = 100
		self.rotation = 0                   # Current rotation of tank
		self.rotation_delta = 6             # How many degrees tank rotates (should ideally divide into 360 evenly)
		self.turret_rotation = 0            # Current rotation of turret
		self.turret_rotation_delta = 11.25  # How many degrees turret rotates (should ideally divide into 360 evenly)
		self.fire_rate = 1                  # How many seconds in between firings (lower number = faster firing)
		self.last_fire = None               # When did we last fire

		self.alive = True
		self.moving = False

		self.rect = None

	# Handles movement
	# Rotate to the left
	def right(self):

		center = self.rect.center
		if (self.rotation - self.rotation_delta) <0:
			self.rotation = (360 - self.rotation_delta)

		else:
			self.rotation -= self.rotation_delta

		self.update_image(center)

	# Rotate to the right
	def left(self):
		center = self.rect.center

		if (self.rotation + self.rotation_delta) >= 360:
			self.rotation = 0

		else:
			self.rotation += self.rotation_delta

		self.update_image(center)

	def update_image(self,old_center):
		# Update the image after rotating

		self.image = pygame.transform.rotate(self.image_original,self.rotation)
		self.rect = self.image.get_rect()
		self.rect.center = old_center

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

	def fire(self):
		# TODO: Need to fix position issue
		print ("Fire")

		now = datetime.datetime.now()

		# Check if we're rate limited
		if (self.last_fire == None) or (now >= self.last_fire + datetime.timedelta(seconds=self.fire_rate)):

			bullet = Bullet(self.position,self.rotation,self)

			# Add to level and set last fire time
			self.game.level.add_bullet(bullet)
			self.last_fire = now

		else:
			# TODO: Do we need to do anything if rate limited
			pass

	def hit(self):
		print ("I'M HIT!")

		self.health -= 20

		if self.health <=0:
			self.alive = False
			self.game.level.remove_enemy(self)

	# Rotate the turret to the right - not used at present
	def turret_left(self):
		#self.report_turret_rotation()
		if self.turret_rotation >0:
			self.turret_rotation -= self.turret_rotation_delta

		else:
			self.turret_rotation = (360 - self.turret_rotation_delta)

		#self.report_turret_rotation()

	# Rotate the turret to the right - not used at present
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

