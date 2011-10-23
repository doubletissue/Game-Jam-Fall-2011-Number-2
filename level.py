from __future__ import division
import random

#GLOBAL VARS
PROB_HOLES = .7


class level(object):
  _obstacles = []
  _holes = []
  _holes_progress = {}

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
      
      try:
        self._holes_progress[(x, y)] += 1
      except KeyError:
        self._holes_progress[(x, y)] = 0
    
    items_to_delete = []
    
    for k, v in self._holes_progress.iteritems():
      v += 1
      if v >= 3:
        print k
        self._holes[k[0]][k[1]] = True
        items_to_delete.append(k)
    
    for i in items_to_delete:
      del self._holes_progress[i]

  def placeObstacle(self, x, y):
    self._obstacles[x][y] = True

  def getState(self):
    return (self._obstacles, self._holes, self._holes_progress)

  def getContents(self, center, rotation):
    result = {}
    center_x = center[0]
    center_y = center[1]
    center_x_min = math.floor(center_x - 16*1.414)
    if center_x_min < 0:
      center_x_min = 0
    center_x_max = math.ceil(center_x + 16*1.414)
    if center_x_max > 127:
      center_x_max = 127
    center_y_min = math.floor(center_y - 16*1.414)
    if center_y_min < 0:
      center_y_min = 0
    center_y_max = math.ceil(center_y + 16*1.414)
    if center_y_max > 127:
      center_y_max = 127
    for x in range(int(center_x_min), int(center_x_max)):
      for y in range(int(center_y_min), int(center_y_max)):
        element_x = x - center_x
        element_y = y - center_y
        value = 0
        if self._obstacles[x][y]:
          value = 4
        else if (x, y) in self._holes_progress:
          value = self._holes_progress[(x, y)]
        else if self._holes[x][y]:
          value = 3
        xprime = element_x * math.cos(rotation) - y * math.sin(rotation)
        yprime = element_y * math.sin(rotation) + y * math.cos(rotation)
        result[(xprime, yprime)] = value
    return result

  def collision(self, x, y):
    if self._obstacles[x][y] or self._holes[x][y]:
      return True
    else:
      return False
