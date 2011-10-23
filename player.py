from __future__ import division
from physicsobject import PhysicsObject
import math

DEFAULT_DMAG = 5
DEFAULT_DARG = math.pi / 18000
PLAYER_SIZEX, PLAYER_SIZEY = 32, 32

class Player(PhysicsObject):
  def __init__( self, level, (x, y) ):
    PhysicsObject.__init__( self, (x,y), (0,0), (PLAYER_SIZEX,PLAYER_SIZEY) )
    self.level = level

  def update_controls( self, player_input ):
    mag = 0
    arg = 0
    if "up" in player_input:
      mag += DEFAULT_DMAG
    if "down" in player_input:
      mag -= DEFAULT_DMAG
    if "left" in player_input:
      arg -= DEFAULT_DARG
    if "right" in player_input:
      arg += DEFAULT_DARG

    self.start_update( mag, arg )

  def update_physics( self, physicsobjects ):
    for x in physicsobjects:
      self.update_bounce( x )

if __name__ == "__main__":
  a = Player( None, (1,1) )
  print a
  a.update_controls([])
  a.execute_update()
  print a
  a.update_controls( ["up"] )
  a.execute_update()
  print a
  a.update_controls( ["left"] )
  a.execute_update()
  print a

  b = Player( None, (1,1) )
  b.update_controls([])
  b.execute_update()

  print "COLLIDE"

  for i in range(15):
    a.update_controls([])
    #a.update_physics([b])
    a.execute_update()
    print a
