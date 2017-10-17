import pygame

class StaticGameObject():
	def __init__(self,game,position):
		self.game = game
		self.position = position

		self.health = 100
		self.rotation = 0                   # Current rotation of tank

		self.rect = None

		#TODO: Figure this out
		self.image = pygame.image.load("assets/PNG/Obstacles/oil.png")

		self.alive = True

	def hit(self):
		print("OBS IS HIT!")
		self.health -= 20

		if self.health <=0:
			self.alive = False

		# TODO: Figure out how to remove

