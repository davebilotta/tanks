'''
This handles the updating of everything
'''

import pygame
import math
from pygame.locals import *
import datetime

class Controller():
	def __init__(self,screen,level):
		self.screen = screen
		self.level = level

	def update(self):
		self.update_player()
		self.update_bullets()
		self.update_teammates()
		self.update_enemies()

	def update_bullets(self):
		now = datetime.datetime.now()
		bullet_id = 0

		for bullet in self.level.bullets:

			# Check if expired
			if (now >= bullet.create_time + datetime.timedelta(seconds=bullet.ttl)):
				del(self.level.bullets[bullet_id])
				#bullet.kill()

			# TODO: check if off screen?

			# Otherwise, update position and increment counter
			else:
				bullet.position = self.update_position(bullet.position,bullet.rotation,bullet.speed)

				#bullet.base_rect.center = bullet.position
				bullet.rect.center = bullet.position
				bullet_id += 1

	def update_player(self):
		pos = self.level.player.position
		rot = self.level.player.rotation
		spd = self.level.player.speed

		self.level.player.position = self.update_position(pos,rot,spd)
		self.level.player.rect.center = self.level.player.position

	def update_teammates(self):
		pass

	def update_enemies(self):
		pass

	# This is called by tanks and bullets
	def update_position(self,position,rotation,speed):
		x, y = position
		rad = rotation * math.pi / 180

		x -= speed * math.sin(rad)
		y -= speed * math.cos(rad)

		return (x,y)
