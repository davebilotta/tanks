class Level():
	def __init__(self,background,player,teammates,enemies):

		self.score = 0
		self.gameover = False
		self.background = background
		self.player = player
		self.teammates = []
		self.enemies = []
		self.bullets = []

	def add_bullet(self,bullet):
		self.bullets.append(bullet)