from tkinter import *

from tkinter import messagebox
# Importe o modulo de Tkinter/ como criar a janela principal do aplicativo/ adicione uma ou mais dos widgets no aplicativo.
#class Application:
 #   def __init__(self, master=None):
  #      pass
#root = tkinter.Tk()
#Application(root)
#root.mainloop()
#topmainloop()
#def HelloCallBack():
#	msg = messagebox.showinfo("Hello Python", "Hello World")

#B = Button(top, tex = 'Hello', command = HelloCallBack)
#B.place(x = 50, y = 50)
#topmainloop()

from tkinter import *

from tkinter import messagebox
#
top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Calculadora", command = helloCallBack)
B.place(x = 50,y = 50)

C = Canvas(top, bg = "blue", height = 250, width = 300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Blue", fg = "blue")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Yellow", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text = "Black", fg = "black")
blackbutton.pack( side = BOTTOM)

top.mainloop()