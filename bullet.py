import pygame
import math
from pygame.locals import *

class Bullet():
	def __init__(self,position,rotation,tank=None):
		# These are created using firing items's position and rotation
		# Note we also store the tank that fired it (may be useful later
		# to store which tank gets credit for kill)

		self.position = position
		self.rotation = rotation
		self.tank = tank

		self.speed = 0.25

		# TODO: Should we load this up front in an asset manager of some sort?
		# Check overhead with doing this for every bullet. Also need to destroy
		# upon hit or exiting screen
		self.image = pygame.image.load("assets/PNG/Bullets/bulletYellow.png")