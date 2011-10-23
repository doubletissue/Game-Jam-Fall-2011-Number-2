from __future__ import division
import math

MAX_VELOCITY = 25

class PhysicsObject(object):
  def __init__( self, (x,y), (vmag,varg), (sizex,sizey) ):
    self.x, self.y = x,y
    self.vmag, self.varg = vmag,varg
    self.sizex, self.sizey = sizex, sizey
    self.update_edges()

  def __str__( self ):
    return "x: {}, y: {}; vmag: {}, varg: {}; sizex: {}, sizey: {}".format( self.x, self.y, self.vmag, self.varg, self.sizex, self.sizey )

  def start_update( self, a, darg ):
    self.next_varg = (self.varg + darg) % 2*math.pi

    self.next_vmag = self.vmag + a
    if self.next_vmag > MAX_VELOCITY:
      self.next_vmag = MAX_VELOCITY
    if self.next_vmag < 0:
      self.next_vmag = 0

    self.next_x = self.next_vmag*math.cos(self.next_varg)
    self.next_y = self.next_vmag*math.sin(self.next_varg)

  def update_bounce( self, other ):
    intersection = self.intersect( other )
    if intersection == None:
      return
    if intersection in ["top", "bottom"]:
      self.next_dy = -(self.dy + other.dy)/2
    elif intersection in ["left", "right"]:
      self.next_dx = -(self.dx + other.dx)/2

  def execute_update( self ):
    self.x = self.next_x
    self.y = self.next_y
    self.vmag = self.next_vmag
    self.varg = self.next_varg
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

if __name__ == "__main__":
  a = PhysicsObject( (0,0), (0,0), (0,0) )
  print a
  a.start_update( 0, 0 )
  a.execute_update()
  print a
  a.start_update( 1, 0  )
  a.execute_update()
  print a
  a.start_update( 0, math.pi )
  a.execute_update()
  print a
  a.start_update( 1, math.pi )
  a.execute_update()