from __future__ import division
import math

MAX_VELOCITY = 25

class PhysicsObject(object):
  def __init__( self, (x,y), (dx,dy), (sizex,sizey) ):
    self.x, self.y = x,y
    self.dx, self.dy = dx,dy
    self.sizex, self.sizey = sizex, sizey

  def update( self, a, dr ):
    mag = abs(complex(self.x,self.y))
    arg = math.tan2( self.y, self.x )

    arg = (arg + dr)

    abs(complex(self.dx,self.dy))

  def isAbove( self, other ):
    return self.y < other.y

  def isBelow( self, other ):
    return self.y > other.y

  def isLeft( self, other ):
    return self.x < other.x

  def isRight( self, other ):
    return self.x > other.x

  def intersect( self, other ):
    pass

  def bounce( self, other ):
    pass