import random
import pygame

from static_game_object import StaticGameObject
from enemy import Enemy
from effect import Effect

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
		self.effects = []

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

	def remove_bullet(self,bullet):
		self.bullets.remove(bullet)

	def remove_enemy(self,enemy):
		self.enemies.remove(enemy)
		self.score += 1

	def remove_obstacle(self,obstacle):
		self.obstacles.remove(obstacle)

	def add_effect(self,position):
		self.effects.append(Effect(position))

	def remove_effect(self,effect):
		self.effects.remove(effect)
