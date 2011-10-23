from __future__ import division
import pygame
from pygame.locals import *
import math, random
import sys,os

from level import level
from player import Player


floor_image   = pygame.image.load(os.path.join("Art","ground_0.png"))
wall_image    = pygame.image.load(os.path.join("Art","wall.png"    ))
rock_image    = pygame.image.load(os.path.join("Art","rock.png"    ))
player_image  = pygame.image.load(os.path.join("Art","viking_0.png"    ))

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
    self._players = []
    for i in range(4):
      self._players.append(Player( 0, (i+100,i+100) ) )
    self._screens = [ pygame.Surface((512,512)) ] * 4
  
  def update( self, keymap ):
    for level in self._levels:
      level.update( )
    
    for i, player in enumerate(self._players):
      
      d = []
      
      for key in player_keymap[i]:
        if keymap[key]:
          d.append(player_keymap[i][key])
      
      player.update_controls( d )
      player.update_physics( [] )
      player.execute_update( )
    
    
  def draw( self, screen ):
    screen.fill((0,0,0))
    for i, subscreen in enumerate( self._screens ):
      subsubscreen = pygame.Surface((1024,1024))
      player = self._players[i]
      level = self._levels[player.level]
      points = level.getContents( ( player.x , player.y ) , 0 )
      for point_cord, point_type in points.items():
        x,y = point_cord
        x = (x+8)*32 + 256
        y = (y+8)*32 + 256
        if point_type == 0:
          subsubscreen.blit(floor_image,(x,y))
        elif point_type == 5:
          subsubscreen.blit(wall_image,(x,y))
        elif point_type == 4:
          subsubscreen.blit(wall_image,(x,y))
      r = player.varg*180/math.pi
      subsubscreen = pygame.transform.rotate(subsubscreen, r)
      new_rect = subsubscreen.get_rect()
      draw_x = (-new_rect.h + 1024)/2 - 256
      draw_y = (-new_rect.w + 1024)/2 - 256
      subscreen.blit( subsubscreen, (draw_x,draw_y) )
      subscreen.blit(player_image,(256,256))
      screen.blit( subscreen , (0 if i < 2 else 512, 0 if i%2==0 else 512) )