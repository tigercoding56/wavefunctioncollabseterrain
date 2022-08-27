import random
def getntiles(map,x,y):
     nt = []
     nt.append(map.returnTile(x + 1,y))
     nt.append(map.returnTile(x - 1,y))
     nt.append(map.returnTile(x ,y + 1))
     nt.append(map.returnTile(x ,y - 1))
     return nt
    
   
         
         
def  randTile(map , x , y):
    possibletiles = [ "water"  , "grass", "stone" ]
    nt = []
    nt.append(map.returnTile(x + 1,y))
    nt.append(map.returnTile(x - 1,y))
    nt.append(map.returnTile(x ,y + 1))
    nt.append(map.returnTile(x ,y - 1))
    if "stone" in nt :
        if "sand" in nt:
           return "grass"
        elif "water" in nt :
            return "sand"
        elif "grass" in nt:
         if random.randint(1,2) == 1 :
             return "grass"
         else:
          return "stone"
        else :
            if random.randint(1,4) == 1 :
             return "grass"
            else :
             return "stone"
            
   
    if not "grass" in nt and not "stone" in nt :
     if random.randint(1,4) == 1 :
         return "water"
    if nt == ["none" , "none" , "none" , "none"] :
        return possibletiles[random.randint(0,2)]
    if nt == ["water"] * 4:
        return "water"
    if nt == ["sand"] * 4:
        return possibletiles[random.randint(0 , 1)]
    if "water" in  nt and "grass" in nt :
        return "sand"
    if "water" in nt and not "grass" in nt and "sand" in nt  :
        if random.randint(1 , 4) == 2:
         return "sand"
        else:
         return "water"
    if "water" in nt and not "grass" in nt and not "sand" in nt:
     if random.randint(1 , 10) == 2:
         return "sand"
     else:
         return "water"
    if "grass" in nt and not "water" in nt :
     if random.randint(1 , 20) == 2:
         return "sand"
     else:
         return "grass"
    if "grass" in nt and not "water" in  nt and "sand" in nt :
         return "grass"
    if "grass" in nt and "water" in nt :
        return "sand"
    if "water" in nt and not "sand" in nt :
        return "water"
    if "grass" in nt and not "sand" in nt :
        return "grass"
    if "sand" in nt and not "water" in nt:
        return "grass"
    return "sand"
    