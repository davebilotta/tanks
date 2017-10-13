import pygame
from pygame.locals import *

class Renderer():
	def __init__(self,screen,level):
		self.screen = screen
		self.level = level

		self.sand = pygame.image.load("assets/PNG/Environment/sand.png")
		self.grass = pygame.image.load("assets/PNG/Environment/grass.png")
		self.dirt = pygame.image.load("assets/PNG/Environment/dirt.png")

		self.tree_small_sand = pygame.image.load("assets/PNG/Environment/treeSmall_sand.png")
		self.tree_small_grass = pygame.image.load("assets/PNG/Environment/treeSmall_grass.png")
		self.tree_small_dirt = pygame.image.load("assets/PNG/Environment/treeSmall_dirt.png")

		self.tree_large_sand = pygame.image.load("assets/PNG/Environment/treeLarge_sand.png")
		self.tree_large_grass = pygame.image.load("assets/PNG/Environment/treeLarge_grass.png")
		self.tree_large_dirt = pygame.image.load("assets/PNG/Environment/treeLarge_dirt.png")

		self.bkg = []
		self.bkg.append(["LS","S","S","S","S","LS","S","S"])
		self.bkg.append(["S","S","S","S","S","S","S","S"])
		self.bkg.append(["S","SS","S","S","S","S","S","S"])
		self.bkg.append(["S","S","S","S","S","S","S","S"])
		self.bkg.append(["LS","S","S","S","SS","S","S","SS"])
		self.bkg.append(["S","LS","S","S","S","S","S","S"])

		self.debug_mode = False

	def render(self,tanks_object):
		self.render_bkg()
		self.render_ui(tanks_object)
		self.render_bullets()
		self.render_player()
		self.render_teammates()
		self.render_enemies()
		self.render_objects()

	def render_bkg(self):
		#self.screen.blit(self.level.background, (0,0))

	    #screen.blit(background, (0, 0))
	    bkg_w = 128
	    bkg_h = 128
	    blit_cnt = 0

	    for y in range(0,6):
	        for x in range(0,8):
	            #background.blit(bkg_img,(bkg_w*x,bkg_h*y))
	            self.level.background.blit(self.get_bkg_image(x,y),(bkg_w*x,bkg_h*y))

	    self.screen.blit(self.level.background,(0,0))

	def get_bkg_image(self,x,y):
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

	def render_ui(self,tanks_object):
		fps = tanks_object.clock.get_fps()
		#print(fps)

		caption = "FPS: " + str(round(fps))
		pygame.display.set_caption(caption)

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
		pass

	def render_enemies(self):
		pass

	def render_objects(self):
		pass



