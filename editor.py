import random
texturesize = 10
import tile as tile
import graphene
import terrain as wc
import time 
mapsizex = 40
mapsizey = 40
viewportsize = 2 #### higher = smaller postion of map visible at once 
map = tile.chunk(mapsizex - 1 ,mapsizey - 1 )
y = 0 
movementx = 0
movementy =0
camerax = 0
cameray =  0
texturesize = 10 

for y in range(0  , mapsizey):
    for x in range(0, mapsizex):
     map.setTile(x,y , "none")     

######## wave function collapse implementation  probably  bad #####
for counter in range(1, 10 ):
 x = random.randint(0, mapsizex )
 y = random.randint(0, mapsizey )
 tile = wc.randTile(map,x,y)
 map.setTile(x,y , tile )

for y in range(0  , mapsizey):
    for x in range(0, mapsizex):
     tile = wc.randTile(map , x ,y)
     map.setTile(x,y , tile )
###CLEANUP###
for y in range(0  , mapsizey):
    for x in range(0, mapsizex):
     if map.returnTile(x,y ) == "sand" :
       if not "grass" in wc.getntiles(map , x ,y )  :
           map.setTile(x , y , "water" )
###now remove sand from grass ####
for y in range(0  , mapsizey):
    for x in range(0, mapsizex):
     if map.returnTile(x,y ) == "sand" :
       if not "water" in wc.getntiles(map , x ,y )  :
           map.setTile(x , y , "grass" )
####we just have to add structures now how about trees first ?
           
        
print(map.map)
graphene.setup( int((texturesize * mapsizex) / viewportsize)  , int((texturesize * mapsizey) /  viewportsize))
graphene.bevoreloop()
def  updatemap():
 global map
 global camerax
 global cameray
 graphene.canvas.delete('all')
 for y in range(0,  int((mapsizey -1) / viewportsize) ):
    for x in range(0, int(mapsizex  / viewportsize) ):
     graphene.newsprite("tile" , str(map.returnTile(x + cameray  ,y + camerax  )) + ".png" , x * texturesize , y * texturesize  )

#graphene.NewActiveSprite("tile" ,"cursor.png" , (mapsizex * texturesize) / 2 , (mapsizey * texturesize) / 2  , "io = 0")
updatemap()
pointer = graphene.SRAM[len(graphene.SRAM) - 1]

while True:
    graphene.win.update()
    cameray = cameray + 1
    updatemap()
    time.sleep(0.15)
