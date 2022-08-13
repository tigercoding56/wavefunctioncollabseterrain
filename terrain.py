import random
def  randTile(map , x , y):
    possibletiles = [ "water" ,"sand" , "grass"]
    nt = []
    nt.append(map.returnTile(x + 1,y))
    nt.append(map.returnTile(x - 1,y))
    nt.append(map.returnTile(x ,y + 1))
    nt.append(map.returnTile(x ,y - 1))
    if nt == ["none" , "none" , "none" , "none"] :
        return possibletiles[random.randint(0,len(possibletiles) - 1)]
    if nt == ["water"] * 4:
        return "water"
    if nt == ["sand"] * 4:
        return possibletiles[random.randint(0 , 2)]
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
     if random.randint(1 , 10) == 2:
         return "sand"
     else:
         return "grass"
    if "grass" in nt and not "water" in  nt and "sand" in nt :
     if random.randint(1 , 4) == 2:
         return "sand"
     else:
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