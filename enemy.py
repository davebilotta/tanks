import pygame
from pygame.locals import *
from tank import Tank
import random

class Enemy(Tank):
	def __init__(self,game):
		Tank.__init__(self,0,game,False)

		# TODO: Change this later
		self.image = pygame.image.load("assets/PNG/Tanks/tankBeige.png")
		self.image_original = pygame.image.load("assets/PNG/Tanks/tankBeige.png")

		# Start enemy at random position
		self.position = (random.randint(0,self.game.screen.get_width()),random.randint(0,self.game.screen.get_height()))
		self.speed = 0.5
		self.max_speed_fwd = 5
		self.max_speed_rev = -2.5

		self.speed_delta = 0.5      # How much does speed change

		self.rect = self.image.get_rect()
		self.rect.center = self.position

	def hit(self,bullet):
		self.health -= bullet.damage['tank']

		if self.health <=0:
			self.alive = False
			self.game.level.remove_enemy(self)
