import pygame
from pygame.locals import *

class Renderer():
	def __init__(self,game):
		self.screen = game.screen
		self.level = game.level

		# TODO: Move all of this to asset class?
		self.sand = pygame.image.load("assets/PNG/Environment/sand.png")
		self.grass = pygame.image.load("assets/PNG/Environment/grass.png")
		self.dirt = pygame.image.load("assets/PNG/Environment/dirt.png")

		self.tree_small_sand = pygame.image.load("assets/PNG/Environment/treeSmall_sand.png")
		self.tree_small_grass = pygame.image.load("assets/PNG/Environment/treeSmall_grass.png")
		self.tree_small_dirt = pygame.image.load("assets/PNG/Environment/treeSmall_dirt.png")

		self.tree_large_sand = pygame.image.load("assets/PNG/Environment/treeLarge_sand.png")
		self.tree_large_grass = pygame.image.load("assets/PNG/Environment/treeLarge_grass.png")
		self.tree_large_dirt = pygame.image.load("assets/PNG/Environment/treeLarge_dirt.png")

		self.ui_font = pygame.font.SysFont("monospace",24,bold=True)

		self.bkg = []
		self.bkg.append(["S","S","LS","S","S","LS","S","S"])
		self.bkg.append(["S","S","S","S","S","S","S","S"])
		self.bkg.append(["S","SS","S","S","S","S","S","S"])
		self.bkg.append(["S","S","S","S","S","S","S","S"])
		self.bkg.append(["LS","S","S","S","SS","S","S","SS"])
		self.bkg.append(["S","LS","S","S","S","S","S","S"])

		self.colors = {
			   "red": (200,0,0),
			  "blue": (0,0,255),
			"orange": (255,165,0),
		}

		self.debug_mode = False

	def render(self,game):
		self.render_bkg()
		self.render_ui(game)
		self.render_bullets()
		self.render_player()
		self.render_teammates()
		self.render_enemies()
		self.render_obstacles()

	def render_bkg(self):
	    bkg_w = 128
	    bkg_h = 128

	    for y in range(0,6):
	        for x in range(0,8):
	            self.level.background.blit(self.get_bkg_image(x,y),(bkg_w*x,bkg_h*y))

	    self.screen.blit(self.level.background,(0,0))

	def get_bkg_image(self,x,y):
		# TODO: Fix this later
		img = self.bkg[y][x]

		if img == "S":
			return self.sand
		elif img == "SS":
			return self.tree_small_sand
		elif img == "LS":
			return self.tree_large_sand
		elif img == "D":
			return self.dirt
		elif img == "SD":
			return self.tree_small_dirt
		elif img == "LD":
			return self.tree_large_dirt
		elif img == "G":
			return self.grass
		elif img == "SG":
			return self.tree_small_grass
		elif img == "LG":
			return self.tree_large_grass

		# Need to do the others
		else:
			return self.sand

	def render_ui(self,game):
		''' This renders the FPS, UI components (ex: score, level, etc.) '''
		fps = game.clock.get_fps()
		offset_x = 10
		offset_y = 5

		# Render the FPS in the Title Bar
		caption = "FPS: " + str(round(fps))
		pygame.display.set_caption(caption)

		# Render score in the top left
		score_text = self.ui_font.render(("Score: " + str(game.level.score)),1,self.colors['red'])
		self.screen.blit(score_text,(offset_x,offset_y))

		# Render speed below score
		speed_text = self.ui_font.render(("Speed: " + str(game.player.speed)),1,self.colors['orange'])
		self.screen.blit(speed_text,(offset_x,(offset_y + score_text.get_height() + (offset_y/2))))

		# Render level number in top right
		level_text = self.ui_font.render(("Level: " + str(game.level.number)),1,self.colors['blue'])
		self.screen.blit(level_text,((self.screen.get_width() - level_text.get_width() - offset_x), offset_y))

		# Render health below level number
		health_text = self.ui_font.render(("Health: " + str(game.player.health)),1,self.colors['blue'])
		self.screen.blit(health_text,((self.screen.get_width() - health_text.get_width() - offset_x), (offset_y + health_text.get_height() + (offset_y/2))))

	def render_bullets(self):
		red = (255,0,0)
		for bullet in self.level.bullets:
			self.screen.blit(bullet.image,bullet.rect)

			if self.debug_mode:
				pygame.draw.circle(self.screen, red, (int(bullet.position[0]),int(bullet.position[1])), 10, 5)

	def render_player(self):
		red = (255,0,0)
		player = self.level.player

		self.screen.blit(player.image,player.rect)

		if self.debug_mode:
			pygame.draw.circle(self.screen, red, (int(player.position[0]),int(player.position[1])), 50, 5)

	def render_teammates(self):
		for teammate in self.level.teammates:
			self.screen.blit(teammate.image,teammate.rect)

	def render_enemies(self):
		for enemy in self.level.enemies:
			self.screen.blit(enemy.image,enemy.rect)

	def render_obstacles(self):
		for obstacle in self.level.obstacles:
			self.screen.blit(obstacle.image,obstacle.position)
