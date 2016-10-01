import pygame, sys
from pygame.locals import *
import random
import time

WIDTH=1000
HEIGHT=800

def rectangle():
    return pygame.Rect(
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT))

def get_intersection(a, b):
    top = max(a.top, b.top)
    bottom = min(a.bottom, b.bottom)
    left = max(a.left, b.left)
    right = min(a.right, b.right)
    return pygame.Rect(left, top, right-left, bottom-top)

def intersect(a, b):
    if b.bottom < a.top or \
       b.right < a.left or \
       b.top > a.bottom or \
       b.left > a.right:
          return False
    return True 

def refresh():
  # draw the white background onto the surface
  windowSurface.fill(WHITE)

  # draw the text's background rectangle onto the surface
  rec1 = rectangle()
  rec2 = rectangle()
  while not intersect(rec1, rec2):
      rec2 = rectangle()

  rec3 = get_intersection(rec1, rec2)

  pygame.draw.rect(windowSurface, RED, rec1)
  pygame.draw.rect(windowSurface, BLUE, rec2)
  pygame.draw.rect(windowSurface, GREEN, rec3)

  # draw the window onto the screen
  pygame.display.update()

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# run the game loop
cont = 0
while True:
    refresh()
    cont += 1
    time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
