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
		#self.update_ui()
		self.update_player()
		self.update_teammates()

		self.update_enemies()
		#self.update_objects()

	def update_player(self):
		x, y = self.level.player.position
		rad = self.level.player.rotation * math.pi / -180

		x += self.level.player.speed * math.sin(rad)
		y += self.level.player.speed * math.cos(rad)


    	# TODO: Check position off screen (how to handle?)

		self.level.player.position = (x, y)

	def update_teammates(self):
		pass

	def update_enemies(self):
		pass