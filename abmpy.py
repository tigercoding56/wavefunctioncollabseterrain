
def  terrafixabm(blockx , blocky ,conlist ):
 chunk = conlist[1]
 nxtiles = chunk.gettiles(blockx , blocky , 2)
 if "water" in nxtiles :
     chunk.setTile(blockx , blocky , "grass2")
 if "stone" in nxtiles :
     chunk.setTile(blockx , blocky , "grass3")