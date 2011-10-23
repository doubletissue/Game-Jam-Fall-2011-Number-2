from __future__ import division
from physicsobject import PhysicsObject

class Player(PhysicsObject):
  def __init__( self, (x, y) ):
    self.x, self.y = x, y

  def update_controls( self, player_input ):
    pass

  def update_physics( self, physicsobjects ):
    