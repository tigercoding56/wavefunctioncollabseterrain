# Import the required libraries
from tkinter import ALL
from tkinter import *
from PIL import Image, ImageTk
import os
import time
from pecrs import *
import math
import random
from os.path import exists
import vlc
from threading import Thread
SRAM = []
colliders = []
speed_X = 10
speed_Y = 10
debug = 0
friends = 0 # for bonus realism because i do not have friends(T.T)
syncy = 250
syncx = 250
playerx = 0
playery = 0
velx = 0
vely = -10
space = Space()
jump = 1
canvas = 0
def setup(windx , windy):
    global win
    global canvas
    win=Tk()
    win.geometry(str(windx) + "x" + str(windy))
    canvas=Canvas(win , width= windx, height= windy)
    canvas.pack()

    



##classes##############

class sprite:
    def __init__(self, master , x , y , mode):
     global canvas 
     path = file=os.getcwd()+'/assets/' + master
     self.img = ImageTk.PhotoImage(file=path)
     self.x = x
     self.y = y
     self.camx = y
     self.camy = x
     self.mode = mode
     self.id = canvas.create_image(self.x, self.y, image=self.img, anchor="center")
     self.code = '''io = 0 '''
     self.bounds = (50 , 50 , -50 , -50  )
     self.cx = x
     self.cy = y
     self.shown = "True"
     self.name = "default"
     self.timer = "default"

     canvas.scale(self.id, 250, 250, 2.0, 2.0)
    def hide(self):
     if self.shown == True:
        canvas.itemconfig(id, state='hidden')
        self.shown = False
    def show(self):
     if self.shown == False :
         canvas.itemconfig(id, state='normal')
         self.show = True
    def move(self, x , y):
        self.x += x
        self.y += y
        canvas.move(self.id, self.x, self.y)
   
    def parralax(self , x , y):
        self.x = self.x * x
        self.y = self.y * y
    def inittimer(self , finish ,  after):
      self.timer = 0
      self.finish = finish
      self.after = after
      
    
    def timercode(self):
     if not self.timer == "default" : 
      self.timer = self.timer + 1
      if self.timer == self.finish :
         self.timer = "default"
         tmp = self.after
         exec(tmp)

#####sprite class wrapper
def  gameworldadd(name , texture , x , y ):
  global SRAM
  global win
  global canvas
  t = len(SRAM)
  SRAM.append(name)
  ActiveSprite = t
  SRAM[t] = sprite(texture , x , y , "world")
  return t
def NewActiveSprite(name , texture , x , y ,code):
  lstsprite = len(SRAM)
  t = len(SRAM)
  SRAM.append(name)
  ActiveSprite = t
  SRAM[t] = sprite(texture , x , y , "world")
  SRAM[t].code = code
  SRAM[t].name = name
  
 
def  hudadd(name , texture , x , y ):
 t = len(SRAM)
 SRAM.append(name)
 ActiveSprite = t
 SRAM[t] = sprite(texture , x , y , "HUD")
def clearrenderlist():
    SRAM = []
    

##input handler    
def input_handler(event):
 temp = event.keysym
 global movementx
 global movementy
 if temp == "Up"   :
  movementy += speed_Y
 if temp == 'Down':
  movementy   += (0 - speed_Y )
 if temp == 'Left':
      movementx   += (0 - speed_X )
 if temp == 'Right':
          movementx   +=  speed_X 
 

# floor = collisionbox(-160 , 90 , 170 , 100)
# collider_add(floor)
# wall_1 = collisionbox(-170,-26,-160,100)
# wall_2 = collisionbox(170,-30,180,100)
# wall_2.code = "print('touched wall2')"
# collider_add(wall_1)
# collider_add(wall_2)
# ########game graphics #########
# NewActiveSprite("background" , "background.png" , 250 , 242 , "SRAM[ActiveSprite].parralax(0.9 ,1)")
# 
# gameworldadd("mansion" , "mansion.png" , 250 , 250)
# NewActiveSprite("ghost" , "test.png" , 250 , 252 , "SRAM[ActiveSprite].ghost()")
# 
# hudadd('character' , 'character.png' , 250 , 250)
def getready():
    canvas.bind_all('<KeyPress>' , input_handler)

########################### main loop ############
def update():
    global win
    global canvas
    win.update()

 



 


