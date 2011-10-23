from __future__ import division
import math

MAX_VELOCITY = 25

class PhysicsObject(object):
  def __init__( self, (x,y), (dx,dy), (sizex,sizey) ):
    self.x, self.y = x,y
    self.dx, self.dy = dx,dy
    self.sizex, self.sizey = sizex, sizey

  def __str__( self ):
    return "x: {}, y: {}; dx: {}, dy: {}; sizex: {}, sizey: {}".format( self.x, self.y, self.dx, self.dy, self.sizex, self.sizey )

  def update( self, a, dr ):
    mag = abs(complex(self.x,self.y))
    arg = math.atan2( self.y, self.x )
    if self.x < 0:
      arg = - arg

    #Update the angle
    arg = (arg + dr) % 2*math.pi

    #Update the magnitude
    mag += a
    if mag > MAX_VELOCITY:
      mag = MAX_VELOCITY

    self.dx = mag*math.cos(arg)
    self.dy = mag*math.sin(arg)

    self.x += self.dx
    self.y += self.dy

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

if __name__ == "__main__":
  a = PhysicsObject( (0,0), (0,0), (0,0) )
  print a
  a.update( 0, 0 )
  print a
  a.update( 1, 0  )
  print a
  a.update( 0, math.pi )
  print a
  a.update( 1, math.pi )