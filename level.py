from __future__ import division

class level(object):
  _obstacles = []
  _holes = []

  def __init__(self):
    for i in range(128):
      self._obstacles.append([])
      self._holes.append([])
      for j in range(128):
        self._obstacles[i].append([])
        self._holes[i].append([])
        self._obstacles[i][j] = False
        self._holes[i][j] = False
    for i in range(128):
      self.placeObstacle(0, i)
      self.placeObstacle(127, i)
      self.placeObstacle(i, 0)
      self.placeObstacle(i, 127)

  def update(self):
    pass

  def placeObstacle(self, x, y):
    self._obstacles[x][y] = True
	
  def collision(self, x, y):
    if self._obstacles[x][y] is True or self._holes[x][y] is True:
      return True
    else:
      return False

