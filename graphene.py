# Import the required libraries
from tkinter import ALL
from tkinter import *
from PIL import  ImageTk
import os
import time
from pecrs import *
import math
import random
from os.path import exists
import vlc
from threading import Thread
win=Tk()
registered_textures = {}
SRAM = ["","",""]
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
fcamerax = 0
fcameray = 0
###to imrpove performace


# setup ##############
def setup(windx , windy):
    global win
    global canvas
    win.geometry(str(windx) + "x" + str(windy))
    canvas=Canvas(win , width= windx, height= windy)
    canvas.pack()


class sprite:
    def __init__(self, master , x , y , mode):
     self.img= master
     self.x = x
     self.y = y
     self.id = canvas.create_image(self.x, self.y, image=self.img, anchor="center")
     self.code = '''io = 0 '''

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


####
def NewActiveSprite(name , texture , x , y ,code):
  global registered_textures
  #### auto register unknown textures ####
  if not texture in registered_textures :
     path = os.getcwd()+'/assets/' + texture
     registered_textures[texture] = ImageTk.PhotoImage(file=path)     
  ######
  SRAM[0] = sprite(registered_textures[texture] , x , y , "world")
 
def newsprite(name , texture , x ,y ):
  NewActiveSprite(name ,texture , x ,y , "io = 0 " )

# def  camera(x , y):
#   global SRAM
#   for sprite in SRAM:
#     canvas.move(sprite.id, sprite.x + x , sprite.y + y)
def movecam(x , y):
 global fcamerax
 global fcameray
 fcamerax = fcamerax  + y
 fcameray = fcameray  + x
 
 
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

def updatemap(graphene , mapsizey , mapsizex , viewportsize , mapping , camerax , cameray , texturesize ): ## graphene , mapping , camerax , cameray):
 graphene.canvas.delete('all')
 for y in range(0,  int((mapsizey -1) / viewportsize) ):
    for x in range(0, int(mapsizex  / viewportsize) ):
     graphene.newsprite("tile" , str(mapping.returnTile(x + camerax  ,y + cameray  )) + ".png" , x * texturesize , y * texturesize  )
