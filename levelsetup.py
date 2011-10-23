from __future__ import division
import level

class levelsetup:
  def create():
    nLevel = level()
    for i in range(127):
      nLevel.placeObstacle(0, i)
      nLevel.placeObstacle(127, i)
      nLevel.placeObstacle(i, 0)
      nLevel.placeObstacle(i, 127)
    return nLevel

