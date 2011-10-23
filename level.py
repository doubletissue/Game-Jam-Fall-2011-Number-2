from __future__ import division

class level(object):
  _obstacles = []
  _holes = []

  def __init__(self):
    for i in range(127):
      self._obstacles[i].append([])
      self._holes[i].append([])
      for j in range(127):
        self._obstacles[i][j] = False
        self._holes[i][j] = False

  def update():
    pass

  def placeObstacle(x, y):
    self.obstacles[x][y] = True
	
  def collision(x, y):
    if self.obstacles[x][y] == True:
      return True
    if self.holes[x][y] == True:
      return True
    return False

