
class chunk():
  def __init__(self,sizex,sizey ):
      self.map = [sizex , sizey]
      for counter in range( 0 , sizex * sizey): 
        self.map.append("None")
        
  def setTile(self ,  x, y , tilename):
      if (x > 0 and x < (self.map[0] + 1)) and ( y > 0 and y < (self.map[1] + 1) ):
        coord = (y * self.map[0] + x ) - 9
        self.map[coord] = tilename
  def returnTile(self, x , y):
       if (x > 0 and x < (self.map[0] + 1)) and ( y > 0 and y < (self.map[1] + 1) ):
        coord = (y * self.map[0] + x ) - 9
        return self.map[coord] 
        
#################

    
