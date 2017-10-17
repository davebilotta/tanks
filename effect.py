import pygame
import math
from pygame.locals import *
from datetime import datetime

class Effect():
	def __init__(self,position):
		self.position = position
		self.create_time = datetime.now()

		self.ttl = 1

		self.image = pygame.image.load("assets/PNG/Smoke/smokeGrey4.png")
		#self.image_original = pygame.image.load("assets/PNG/Bullets/bulletYellow_180.png")

		#self.image = pygame.transform.rotate(self.image_original,self.rotation)

		#self.rect = self.image.get_rect()
		#self.rect.center = self.position

