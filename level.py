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
    for i in range(127):
      self.placeObstacle(0, i)
      self.placeObstacle(127, i)
      self.placeObstacle(i, 0)
      self.placeObstacle(i, 127)

  def update():
    pass

  def placeObstacle(x, y):
    self._obstacles[x][y] = True
	
  def collision(x, y):
    if self._obstacles[x][y] == True:
      return True
    if self._holes[x][y] == True:
      return True
    return False

