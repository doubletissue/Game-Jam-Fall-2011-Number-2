from __future__ import division
import math

MAX_VELOCITY = 25

def polar_to_rect( mag, arg ):
  return mag*math.cos(arg), mag*math.sin(arg)

def rect_to_polar( x, y ):
  mag = math.sqrt(x*x + y*y)
  arg = math.atan2( y, x )
  if x < 0:
    arg = -arg
  arg = arg % (2*math.pi)
  return mag, arg

class PhysicsObject(object):
  def __init__( self, (x,y), (vmag,varg), (sizex,sizey) ):
    self.x, self.y = x,y
    self.vmag, self.varg = vmag,varg
    self.sizex, self.sizey = sizex, sizey
    self.top = self.y - self.sizey/2
    self.bottom = self.y + self.sizey/2
    self.left = self.x - self.sizex/2
    self.right = self.x + self.sizex/2
    self.next_top = self.top
    self.next_bottom = self.bottom
    self.next_left = self.left
    self.next_right = self.right

  def __str__( self ):
    return "x: {0}, y: {1}; vmag: {2}, varg: {3}".format( self.x, self.y, self.vmag, self.varg)

  def start_update( self, a, darg ):
    self.next_varg = (self.varg + darg) % (2*math.pi)

    if a == 0:
      a = -0.5
    self.next_vmag = self.vmag + a
    if self.next_vmag > MAX_VELOCITY:
      self.next_vmag = MAX_VELOCITY
    if self.next_vmag < 0:
      self.next_vmag = 0

    self.next_x, self.next_y = polar_to_rect( self.next_vmag, self.next_varg )
    self.next_x, self.next_y = self.next_x + self.x, self.next_y + self.y

    self.next_top = self.next_y - self.sizey/2
    self.next_bottom = self.next_y + self.sizey/2
    self.next_left = self.next_x - self.sizex/2
    self.next_right = self.next_x + self.sizex/2

  def update_bounce( self, other ):
    selfdx, selfdy = polar_to_rect( self.vmag, self.varg )
    otherdx, otherdy = polar_to_rect( other.vmag, other.varg )

    intersection = self.intersect( other )

    if intersection == None:
      return

    self.next_x = self.x
    self.next_y = self.y

    if intersection == "top":
      self.next_y = other.y - 16
      selfdy = -(selfdy + otherdy)/2
    elif intersection == "bottom":
      self.next_y = other.y + 16
      selfdy = -(selfdy + otherdy)/2
    elif intersection == "left":
      self.next_x = other.x - 16
      selfdx = -(selfdx + otherdx)/2
    elif intersection == "right":
      self.next_x = other.x + 16
      selfdx = -(selfdx + otherdx)/2

    self.next_vmag, self.next_varg = rect_to_polar( selfdx, selfdy )

    dx, dy = polar_to_rect( self.next_vmag, self.next_varg )
    self.next_x, self.next_y = self.next_x + dx, self.next_y + dy

  def execute_update( self ):
    self.x = self.next_x
    self.y = self.next_y
    self.vmag = self.next_vmag
    self.varg = self.next_varg
    self.top = self.next_top
    self.bottom = self.next_bottom
    self.left = self.next_left
    self.right = self.next_right

  def isAbove( self, other, updated=False ):
    if updated == True:
      return self.next_bottom < other.next_top
    return self.bottom < other.top

  def isBelow( self, other, updated=False ):
    if updated == True:
      return self.next_top > other.next_bottom
    return self.top > other.bottom

  def isLeft( self, other, updated=False ):
    if updated == True:
      return self.next_right < other.next_left
    return self.right < other.left

  def isRight( self, other, updated=False ):
    if updated == True:
      return self.next_left > other.next_right
    return self.left > other.right

  def intersect( self, other ):
    if not self.isAbove( other, True ) and not self.isBelow( other, True ) and not self.isLeft( other, True ) and not self.isRight( other, True ):
      print "Collision"
      if self.isAbove( other ):
        print "top"
        return "top"
      elif self.isBelow( other ):
        print "top"
        return "bottom"
      elif self.isLeft( other ):
        print "top"
        return "left"
      elif self.isRight( other ):
        print "top"
        return "right"
    else:
      return None

if __name__ == "__main__":
  a = PhysicsObject( (0,0), (0,0), (0,0) )
  print a
  a.start_update( 0, 0 )
  a.execute_update()
  print a
  a.start_update( 1, 0 )
  a.execute_update()
  print a
  a.start_update( 0, math.pi )
  a.execute_update()
  print a
  a.start_update( 1, math.pi )
  a.execute_update()