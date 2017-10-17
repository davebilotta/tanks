import random
import pygame

from static_game_object import StaticGameObject
from enemy import Enemy

class Level():
	def __init__(self,level_number,game,background,player,teammates,enemies):

		self.game = game
		self.score = 0
		self.number = level_number
		self.gameover = False
		self.background = background
		self.player = player
		self.teammates = []
		self.enemies = []
		self.bullets = []

		# These are random for testing - remove later one real level is determined
		self.load_obstacles()
		self.load_enemies()

	def load_obstacles(self):
		# Get some random oil, sandbags, etc.
		self.obstacles = []

		num_obstacles = random.randint(1,5)

		for i in range(0,num_obstacles):
			# For now just always default to oil
			self.obstacles.append(StaticGameObject(self.game,(random.randint(0,self.game.screen.get_width()),random.randint(0,self.game.screen.get_height()))))

	def load_enemies(self):
		self.enemies = []

		num_enemies = random.randint(1,3)

		for i in range(0,num_enemies):
			self.enemies.append(Enemy(self.game))

	def add_bullet(self,bullet):
		self.bullets.append(bullet)

	def remove_enemy(self,enemy):
		for remove_enemy in self.enemies:
			if remove_enemy == enemy:
				self.enemies.remove(enemy)
				self.score += 1

	def remove_obstacle(self,obstacle):
		for remove_obstacle in self.obstacles:
			if remove_obstacle == obstacle:
				self.obstacles.remove(obstacle)
