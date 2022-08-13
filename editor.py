texturesize = 10
import tile as tile
import graphene
import terrain as wc
mapsizex = 50
mapsizey = 50
map = tile.chunk(mapsizex,mapsizey)
y = 0
movementx = 0
movementy =0
texturesize = 10 
for y in range(1  , mapsizey):
    for x in range(1,1 + mapsizex):
     map.setTile(x,y , "none")
######## wave function collapse implementation  probably  bad #####
for y in range( 2  , -1 + mapsizey):
    for x in range(2, mapsizex):
     tile = wc.randTile(map , x ,y)
     map.setTile(x,y , tile )
    
print(map.map)
graphene.setup(texturesize * mapsizex ,texturesize * mapsizey)
graphene.bevoreloop()
for y in range(1,  mapsizey):
    for x in range(1,1 + mapsizex ):
     graphene.newsprite("tile" , str(map.returnTile(x,y)) + ".png" , x * texturesize , y * texturesize  )

#graphene.NewActiveSprite("tile" ,"cursor.png" , (mapsizex * texturesize) / 2 , (mapsizey * texturesize) / 2  , "io = 0")
pointer = graphene.SRAM[len(graphene.SRAM) - 1]
while True:
   graphene.win.update()
   graphene.canvas.move(pointer.id, graphene.camerax , graphene.cameray)
   graphene.camerax = 0
   graphene.cameray = 0
