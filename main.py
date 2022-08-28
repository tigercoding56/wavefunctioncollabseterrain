import random
import randomly
texturesize = 10
import tile as tile
import  graphene
import terrain as wc
import time
import schematics as schems
import pickle
####
interactive = 0
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
def mapgen(tile , seed):
    random.seed(seed)
    randomly.random.seed(seed)
    wc.random.seed(seed)
    ##global tile
    global mapsizex
    global mapsizey
    global viewportsize
    global map
    global movementx
    global movementy
    global camerax
    global cameray
    global texturesize
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

    for y in randomly.randomly(0  , mapsizey):
        for x in randomly.randomly(0, mapsizex):
         map.setTile(x,y , "none")     

    ######## wave function collapse implementation  probably  bad #####
    for counter in range(1, 10 ):
     x = random.randint(0, mapsizex )
     y = random.randint(0, mapsizey )
     tile = wc.randTile(map,x,y)
     map.setTile(x,y , tile )
    for y in range(0  , mapsizey + 30 ):
        for x in range(0, mapsizex + 30 ):
         tile = wc.randTile(map , x ,y)
         map.setTile(x,y , tile )
    for y in randomly.randomly(0  , mapsizey + 3 ):
        for x in randomly.randomly(0, mapsizex + 3 ):
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
    ###now remove sand from grass ####
    for y in range(0  , mapsizey):
        for x in range(0, mapsizex):
         if map.returnTile(x,y ) == "grass"  or map.returnTile(x,y ) == "stone" :
           if  "water" in wc.getntiles(map , x ,y )  :
               map.setTile(x , y , "sand" )

######################################################import map
def importmap(file):
    file = str(file) 
    global mapsizex
    global mapsizey
    global viewportsize
    global map
    global movementx
    global movementy
    global camerax
    global cameray
    global texturesize
    global abm
    leveldatafile = open(file , 'rb')
    leveldata = pickle.load(leveldatafile)
    mapsizex = leveldata[1]
    mapsizey = leveldata[2]
    viewportsize = leveldata[3]
    map = leveldata[4]
    y = leveldata[5]
    movementx = leveldata[6]
    movementy = leveldata[7]
    camerax = leveldata[8]
    cameray =  leveldata[9]
    texturesize = leveldata[10]
    leveldatafile.close()
#################################################### export map
def savemap(file):
    file = str(file) + ".cmp"
    leveldata = [""] * 20
    global mapsizex
    global mapsizey
    global viewportsize
    global map
    global movementx
    global movementy
    global camerax
    global cameray
    global texturesize
    leveldatafile = open(file , 'wb')
    leveldata[0] = ["level format made by @celleron56"]
    leveldata[1] = mapsizex 
    leveldata[2] = mapsizey 
    leveldata[3] = viewportsize 
    leveldata[4] = map
    leveldata[5] = 0 
    leveldata[6] = movementx 
    leveldata[7] = movementy 
    leveldata[8] = camerax  
    leveldata[9] = cameray 
    leveldata[10] =  texturesize
    pickle.dump(leveldata , leveldatafile)
    leveldatafile.close()
               


######################################################end
t = input(" import map (i) or generate new map (n) ? " ) 
if t == "i" :
 t = input("map file  ")
 if t == "menu.cmp" :
   t = input("e to execute code i to import  map menu.cmp ")
   if t == "e" :
    exec(input("code to execute "))
    seed = input("map seed " )
    mapgen(tile , seed)   
   if t == "i" :
    importmap("menu.cmp")
else:
  seed = input("map seed " )
  mapgen(tile , seed)               
               
               
graphene.setup( int((texturesize * mapsizex) / viewportsize)  , int((texturesize * mapsizey) /  viewportsize))
graphene.bevoreloop()
def  updatemap():
 global map
 global camerax
 global cameray
 graphene.canvas.delete('all')
 y = 1
 for y in range(0,  int((mapsizey -1) / int(viewportsize)) ):
    for x in range(0, int(mapsizex  / viewportsize) ):
     graphene.newsprite("tile" , str(map.returnTile(x + camerax  ,y + cameray  )) + ".png" , x * texturesize , y * texturesize  )

#graphene.NewActiveSprite("tile" ,"cursor.png" , (mapsizex * texturesize) / 2 , (mapsizey * texturesize) / 2  , "io = 0")
updatemap()
pointer = graphene.SRAM[len(graphene.SRAM) - 1]

while True:
    graphene.win.update()
    cameray = 0 -graphene.fcamerax
    camerax = 0 - graphene.fcameray
    updatemap()
    time.sleep(0.15)
    if graphene.idl == 1 :
        graphene.idl = 0
        if interactive == 1 :
            exec(input("code:"))
            
    






    