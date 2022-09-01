from tkinter import *
selected = 0
io = 0
# def newmap(entry):
#     global selected
#     global io
#     selected = 1
#     io = ["new", entry.get() ]
# 
# def loadmap(entry):
#     global selected
#     global io
#     print("used")
#     selected = 1
# def savemap():
#     global io
#     io = ["save", entry.get() ]
# def loadmap():
#     global io
#     io = ["load", entry.get() ]    
def sentmessage(someinput):
    global io
    io = someinput
    
def menu():
 global selected
 global io
 
 io = "nan"
 menuw = Tk()
 entry= Entry(menuw, width= 40)
 new = Button(menuw , text="new map", width=40 , command=lambda: sentmessage("newmap"))
 load = Button(menuw , text="load map", width=40 , command=lambda: sentmessage("loadmap"))

 load.pack()
 entry.pack()
 new.pack()

 selected = 0
 while io == "nan" :
      menuw.update()
 io = [io, entry.get()]
 menuw.destroy()
 return io


