from __future__ import division
import pygame
from pygame.locals import *
import math, random
import sys,os

from manager import Manager

def main():
  pygame.init()
  
  screen = pygame.display.set_mode((1024, 1024))
  clock = pygame.time.Clock()
  
  game_manager = Manager()
  
  while True:
    clock.tick(30)
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        pygame.quit()
        return
    keys = pygame.key.get_pressed()
    game_manager.update(keys)
    game_manager.draw(screen)
    pygame.display.flip()
    
main()