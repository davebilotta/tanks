import pygame

class StaticGameObject():
	def __init__(self,game,position):
		self.game = game
		self.position = position

		self.health = 100
		self.rotation = 0

		self.rect = None

		#TODO: Figure this out
		self.image = pygame.image.load("assets/PNG/Obstacles/oil.png")

		self.alive = True

	def hit(self,bullet):
		self.health -= bullet.damage['obstacle']

		if self.health <=0:
			self.alive = False
			self.game.level.remove_obstacle(self)

