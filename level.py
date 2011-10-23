from __future__ import division
import random

# Christian Johnson
# Christopher Thomas

#GLOBAL VARS
PROB_HOLES = .7

class level(object):
  _obstacles = []
  _holes = []

  def __init__(self):
    for i in range(128):
      self._obstacles.append([])
      self._holes.append([])
      for j in range(128):
        self._obstacles[i].append(False)
        self._holes[i].append(False)
    for i in range(128):
      self.placeObstacle(0, i)
      self.placeObstacle(127, i)
      self.placeObstacle(i, 0)
      self.placeObstacle(i, 127)

  def update(self):
    if random.random() < PROB_HOLES:
      x = random.randint(0,127)
      y = random.randint(0,127)
      self._holes[x][y] = True
      print "Placed hole at %d, %d" % (x,y)

  def placeObstacle(self, x, y):
    self._obstacles[x][y] = True
	
  def collision(self, x, y):
    if self._obstacles[x][y] or self._holes[x][y]:
      return True
    else:
      return False