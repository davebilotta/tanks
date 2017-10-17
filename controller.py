'''
This handles the updating of everything
'''

import pygame
import math
from pygame.locals import *
import datetime

class Controller():
	def __init__(self,game):
		self.screen = game.screen
		self.level = game.level

	def tick(self):
		self.check_collisions()
		self.update()

	def check_collisions(self):
		# TODO: Only check collisions within current view

		player = self.level.player
		player_rect = create_rect(player)

		# TODO: Check player with enemies

		# Check player with obstacles
		for obs in self.level.obstacles:
			obs_rect = create_rect(obs)

			if player_rect.colliderect(obs_rect):
				#player.speed = 0
				pass

		for bullet in self.level.bullets:
			bullet_rect = create_rect(bullet)
			remove_bullet = None

			# Check bullet collision with the player (skip own bullets)
			if player_rect.colliderect(bullet_rect) and not bullet.tank == player:
				print ("PLAYER COLLIDED")
				#

			# Check bullet collision with enemies
			for enemy in self.level.enemies:
				enemy_rect = create_rect(enemy)

				if bullet_rect.colliderect(enemy_rect):
					enemy.hit(bullet)
					remove_bullet = bullet
					self.level.add_effect(enemy.position)

			# Check bullet collision with obstacles
			for obs in self.level.obstacles:
				obs_rect = create_rect(obs)

				if bullet_rect.colliderect(obs_rect):
					obs.hit(bullet)
					remove_bullet = bullet
					self.level.add_effect(obs.position)

			# If a bullet was marked for removal, remove now that we're done
			if not remove_bullet == None:
				bullet.alive = False
				self.level.remove_bullet(remove_bullet)

		# Check enemy with obstacles

	def update(self):
		self.update_player()
		self.update_bullets()
		self.update_teammates()
		self.update_enemies()
		self.update_effects()

	def update_bullets(self):
		now = datetime.datetime.now()

		for bullet in self.level.bullets:

			# Check if expired or marked dead on last frame
			if (now >= bullet.create_time + datetime.timedelta(seconds=bullet.ttl) or not bullet.alive):
				self.level.remove_bullet(bullet)

			# TODO: check if off screen?

			# Otherwise, update position and increment counter
			else:
				bullet.position = self.update_position(bullet.position,bullet.rotation,bullet.speed)
				bullet.rect.center = bullet.position

	def update_player(self):
		pos = self.level.player.position
		rot = self.level.player.rotation
		spd = self.level.player.speed

		self.level.player.position = self.update_position(pos,rot,spd)
		self.level.player.rect.center = self.level.player.position

	def update_teammates(self):
		pass

	def update_enemies(self):
		# TODO: Maybe move this later once AI is written
		for enemy in self.level.enemies:
			pos = enemy.position
			rot = enemy.rotation
			spd = enemy.speed

			enemy.position = self.update_position(pos,rot,spd)
			enemy.rect.center = enemy.position

	def update_effects(self):
		now = datetime.datetime.now()

		for effect in self.level.effects:
			# Check if expired or marked dead on last frame
			if (now >= effect.create_time + datetime.timedelta(seconds=effect.ttl)):
				self.level.remove_effect(effect)

	# This is called by tanks and bullets
	def update_position(self,position,rotation,speed):
		x, y = position
		rad = rotation * math.pi / 180

		x -= speed * math.sin(rad)
		y -= speed * math.cos(rad)

		return (x,y)

def create_rect(obj):
	return Rect(obj.position[0],
		obj.position[1],
		obj.image.get_width(),
		obj.image.get_height())