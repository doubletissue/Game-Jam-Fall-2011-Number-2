from __future__ import division
import pygame
from pygame.locals import *
import math, random
import sys,os

from level import level
from player import Player

player_keymap = [
                  { K_w: 'up',
                    K_a: 'left',
                    K_s: 'down',
                    K_d: 'right'
                  },
                  
                  { K_i: 'up',
                    K_j: 'left',
                    K_k: 'down',
                    K_l: 'right'
                  },
                  
                  { K_UP   : 'up',
                    K_LEFT : 'left',
                    K_DOWN : 'down',
                    K_RIGHT: 'right'
                  },
                  
                  { K_KP5: 'up',
                    K_KP1: 'left',
                    K_KP2: 'down',
                    K_KP3: 'right'
                  }
                ]

class Manager():
  def __init__( self ):
    self._levels  = [ level( )  ] * 9
    self._players = [ Player( (0,0) ) ] * 4
    self._screens = [ pygame.Surface((512,512)) ] * 4
  
  def update( self, keymap ):
    for level in self._levels:
      level.update( )
    
    for player in self._players:
      player.update_controls( )
      player.update_physics( )
  
  def draw_subscreen(self, i):
    pass
    
    
  def draw( self, screen ):
    screen.fill((0,0,0))
    
    for i, subscreen in enumerate( self._screens ):
      self.draw_subscreen(i)
      screen.blit( subscreen , (0 if i < 2 else 512, 0 if i%2==0 else 512) )