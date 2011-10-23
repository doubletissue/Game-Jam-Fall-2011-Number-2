from __future__ import division
import math

MAX_VELOCITY = 25

class PhysicsObject(object):
  def __init__( self, (x,y), (dx,dy), (sizex,sizey) ):
    self.x, self.y = x,y
    self.dx, self.dy = dx,dy
    self.sizex, self.sizey = sizex, sizey
    self.update_edges()

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

    self.update_edges()

  def update_edges( self ):
    self.top = self.y - self.sizey/2
    self.bottom = self.y + self.sizey/2
    self.left = self.x - self.sizex/2
    self.right = self.x + self.sizex/2

  def isAbove( self, other ):
    return self.bottom < other.top

  def isBelow( self, other ):
    return self.top > other.bottom

  def isLeft( self, other ):
    return self.right < other.left

  def isRight( self, other ):
    return self.left > other.right

  def intersect( self, other ):
    if not self.isAbove( other ) and not self.isBelow( other ):
      if self.top < other.top:
        return "top"
      elif self.bottom > other.bottom:
        return "bottom"
    if not self.isLeft( other ) and not self.isRight( other ):
      if self.left < other.left:
        return "left"
      elif self.right > other.right:
        return "right"
    else:
      return None

  def bounce( self, other ):
    intersection = self.intersect( other )

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