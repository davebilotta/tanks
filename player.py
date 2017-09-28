import pygame
from pygame.locals import *
from tank import Tank

class Player(Tank):
	def __init__(self):
		Tank.__init__(self)

		#self.image = pygame.image.load("assets/PNG/playerShip1_orange.png")
		self.image = pygame.image.load("assets/PNG/Tanks/tankRed_with_barrel.png")
		#self.barrel_image = pygame.image.load("assets/PNG/Tanks/barrelRed.png")

		self.position = (400,400)
		self.speed = 0
		self.max_speed_fwd = 5
		self.max_speed_rev = -2.5

		self.speed_delta = 0.5      # How much does speed change

		self.friendly = True
		self.enemy = False


