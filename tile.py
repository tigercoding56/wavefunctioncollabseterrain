abm = []
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
           
  def gettiles(self , x , y ,radius):
    nt = []
    for yd in  range(0 - radius , radius) :
     for xd in range(0 - radius , radius) :
         x = x - int( radius / 2 )
         y = y - int(radius / 2 )
         nt.append(self.returnTile(x + xd , y + yd))
    return nt   
        
#################
def ABM_register(code , chunk , block , chance):
    abm.append[(code , chunk , block, floor(chance + 1))]
    
def ABM_clear():
    abm = []
    
def ABM_run():
 if len(abm) > 0 :
   for thing in abm :
       conlist = abm[thing]
       for i in conlist[3] :
        blockx = random.randint(1 , conlist[1].sizex)
        blocky = random.randint(1 , conlist[1].sizey)
        if conlist[1].returnTile(blockx , blocky) == abm[2] :
           exec(conlist0)
    
