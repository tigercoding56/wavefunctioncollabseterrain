
class chunk():
  def __init__(self,sizex,sizey ):
      self.map = []
      self.meta = []
      self.sizex = sizex
      self.sizey = sizey
      for counter in range( 0 , sizex * sizey): 
        self.map.append("None")
      for counter in range( 0 , sizex * sizey): 
        self.meta.append("None") 
        
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
  def placeschem(self ,  schem, offsetx , offsety ,):
       for  instruction in schem :
           instruction 
           self.setTile(  instruction[1] + offsetx , instruction[2] + offsety , instruction[0])
           
   
        
#################

    
