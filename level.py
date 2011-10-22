from future import division

class level:
  bool obstacles[128][128]
  bool holes[128][128]

  def __init__(self):
    for i in 0 to 127:
    for j in 0 to 127:
      obstacles[i][j] = False
      holes[i][j] = False

  def update():
    # todo

  def placeObstacle(x, y):
    self.obstacles[x][y] = True
	
  def collision(x, y):
    if self.obstacles[x][y] == True:
      return True
    if self.holes[x][y] == True:
      return True
    return False

