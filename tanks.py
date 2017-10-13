import pygame, sys, time
from random import randint
from pygame.locals import *

from player import Player
from enemy import Enemy
from level import Level
from renderer import Renderer
from controller import Controller

BLACK = (0,0,0)
WHITE = (255,255,255)
BKG = (234,234,234)

screen = None
background = None

def setup():
    global screen, background, bkg

    # Set up the game and window
    pygame.init()

    WINDOWWIDTH = 1024
    WINDOWHEIGHT = 768
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption("Tanks Game")

    # Display some text
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    screen.blit(background,(0,0))

    pygame.display.flip()

class TankGame():
    def __init__(self):
        self.level = ""
        self.renderer = ""
        self.controller = ""

        self.clock = pygame.time.Clock()

def main():
    setup()
    game = TankGame()

    player = Player(game)

    game.player = player
    teammates = []
    enemies = []

    level = Level("1-A",background,player,teammates,enemies)
    renderer = Renderer(screen,level)
    controller = Controller(screen,level)

    game.level = level
    game.renderer = renderer
    game.controller = controller

    while True:

        # check for the QUIT event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # TODO: Remove this later
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Want elif for second part of these so they can't do left/right or up/down at same time
                if event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()

                # Want elif for second part of these so they can't do left/right or up/down at same time
                if event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_DOWN:
                    player.down()

                else:
                    if event.key == pygame.K_SPACE:
                        player.fire()

        controller.update()
        renderer.render(game)

        pygame.display.update()

        game.clock.tick(30)

main()