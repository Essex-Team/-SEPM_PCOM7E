# test1_pyganim.py - A very very very basic pyganim test program.
#
# This program just runs a single animation. It shows you what you need to do to use Pyganim. Basically:
#   1) Import the pyganim module
#   2) Create a pyganim.PygAnimation object, passing the constructor a list of image filenames and durations.
#   3) Call the play() method.
#   4) Call the blit() method.
#
# The animation images come from POW Studios, and are available under an Attribution-only license.
# Check them out, they're really nice.
# http://powstudios.com/

import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Test 1')

# create the animation objects   ('filename of image',    duration_in_seconds)
duration_in_seconds = 4
boltAnim = pyganim.PygAnimation([('player_idle_0.png', duration_in_seconds),
                                 ('player_idle_1.png', duration_in_seconds),
                                 ('player_idle_2.png', duration_in_seconds),
                                 ('player_idle_3.png', duration_in_seconds),
                                 ('player_idle_4.png', duration_in_seconds),
                                 ('player_idle_5.png', duration_in_seconds),
                                 ('player_idle_6.png', duration_in_seconds),
                                 ('player_idle_7.png', duration_in_seconds)])
boltAnim.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_l:
            # press "L" key to stop looping
            boltAnim.loop = False

    boltAnim.blit(windowSurface, (100, 50))

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.