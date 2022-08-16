
class chunk():
  def __init__(self,sizex,sizey ):
      self.map = []
      self.sizex = sizex
      self.sizey = sizey
      for counter in range( 0 , sizex * sizey): 
        self.map.append("None")
        
  def setTile(self ,  x, y , tilename):
        y = y % self.sizey
        x = x % self.sizex
        coord = (y * self.sizex + x ) - 9
        self.map[coord] = tilename
  def returnTile(self, x , y):
       y = y % self.sizey
       x = x % self.sizex
       coord = (y * self.sizex + x ) - 9
       return self.map[coord] 
      
##################
    
