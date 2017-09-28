'''
This handles the updating of everything
'''

import pygame
import math
from pygame.locals import *

class Controller():
	def __init__(self,screen,level):
		self.screen = screen
		self.level = level

	def update(self):

		self.update_player()

		self.update_bullets()

		self.update_teammates()

		self.update_enemies()
		#self.update_objects()

	def update_bullets(self):
		for bullet in self.level.bullets:
			bullet.position = self.update_position(bullet.position,bullet.rotation,bullet.speed)

	def update_player(self):
		pos = self.level.player.position
		rot = self.level.player.rotation
		spd = self.level.player.speed

		self.level.player.position = self.update_position(pos,rot,spd)

	def update_teammates(self):
		pass

	def update_enemies(self):
		pass

	# This is called by tanks and bullets
	def update_position(self,position,rotation,speed):
		x, y = position
		rad = rotation * math.pi / -180

		x += speed * math.sin(rad)
		y += speed * math.cos(rad)

		return (x,y)
