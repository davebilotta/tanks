import pygame
from pygame.locals import *
from tank import Tank

class Player(Tank):
	def __init__(self,game):
		Tank.__init__(self,0,game)

		self.image = pygame.image.load("assets/PNG/Tanks/tankRed_with_barrel_180.png")
		self.image_original = pygame.image.load("assets/PNG/Tanks/tankRed_with_barrel_180.png")

		self.position = (400,400)
		self.speed = 0
		self.max_speed_fwd = 5
		self.max_speed_rev = -2.5

		self.speed_delta = 0.5      # How much does speed change

		self.friendly = True
		self.enemy = False

		self.rect = self.image.get_rect()
		self.rect.center = self.position

