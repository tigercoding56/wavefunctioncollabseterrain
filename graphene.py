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
win=Tk()

SRAM = []
colliders = []
speed_X = 1
speed_Y = 1
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
camerax = 0
cameray = 0

# setup ##############
def setup(windx , windy):
    global win
    global canvas
    win.geometry(str(windx) + "x" + str(windy))
    canvas=Canvas(win , width= windx, height= windy)
    canvas.pack()


class sprite:
    def __init__(self, master , x , y , mode):
     path = file=os.getcwd()+'/assets/' + master
     self.img=ImageTk.PhotoImage(file=path)
     self.x = x
     self.y = y
     self.camx = y
     self.camy = x
     self.xtrack = x - 250
     self.ytrack = y - 250
     self.mode = mode
     self.id = canvas.create_image(self.x, self.y, image=self.img, anchor="center")
     self.code = '''io = 0 '''
     self.bounds = (50 , 50 , -50 , -50  )
     self.cx = x
     self.cy = y
     self.shown = "True"
     self.name = "default"
     self.timer = "default"

    def hide(self):
     if self.shown == True:
        canvas.itemconfig(id, state='hidden')
        self.shown = False
    def show(self):
     if self.shown == False :
         canvas.itemconfig(id, state='normal')
         self.show = True
    def move(self):
       canvas.move(self.id, self.x, self.y)
    def rmove(self , x , y):
     self.cx = self.x
     self.cy = self.y 
     self.xtrack = self.xtrack +   x
     self.ytrack = self.ytrack +  y
     self.x = self.x + x
     self.y = self.y + y
   
   
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
####
def NewActiveSprite(name , texture , x , y ,code):
  lstsprite = len(SRAM)
  t = len(SRAM)
  SRAM.append(name)
  ActiveSprite = t
  SRAM[t] = sprite(texture , x , y , "world")
  SRAM[t].code = code
  SRAM[t].name = name
def newsprite(name , texture , x ,y ):
  NewActiveSprite(name ,texture , x ,y , "io = 0 " )

# def  camera(x , y):
#   global SRAM
#   for sprite in SRAM:
#     canvas.move(sprite.id, sprite.x + x , sprite.y + y)
def movecam(x , y):
 global camerax
 global cameray
 #camerax = camerax  + x
 #cameray = cameray + y
 camerax = x
 cameray = y
 
def input_handler(event):
 temp = event.keysym
 if temp == "Up" : 
     movecam( 0 ,speed_Y )
 if temp == 'Down':
     movecam(0 , 0 - speed_Y)
 if temp == 'Left':
     movecam(speed_X , 0)
 if temp == 'Right':
     movecam( 0 - speed_X , 0) 

def bevoreloop():
    global canvas 
    canvas.bind_all('<KeyPress>' , input_handler)

