import pygame
import math
from pygame.locals import *
from datetime import datetime

class Bullet():
	def __init__(self,position,rotation,tank=None):
		# These are created using firing items's position and rotation
		# Note we also store the tank that fired it (may be useful later
		# to store which tank gets credit for kill)

		self.position = position
		self.rotation = rotation
		self.tank = tank
		self.create_time = datetime.now()

		self.damage = {
			'tank': 5,
			'obstacle': 25}

		debug = False
		if debug:
			self.speed = 2.5
			self.ttl = 10

		else:
			self.speed = 50
			self.ttl = 1             # How many seconds does this exist

		# TODO: Should load this up front in an asset manager
		#       Need to destroy on exiting screen

		self.image = pygame.image.load("assets/PNG/Bullets/bulletYellow_180.png")
		self.image_original = pygame.image.load("assets/PNG/Bullets/bulletYellow_180.png")

		self.image = pygame.transform.rotate(self.image_original,self.rotation)

		self.rect = self.image.get_rect()
		self.rect.center = self.position

		self.alive = True



