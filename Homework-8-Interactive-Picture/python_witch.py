import tkinter
from tkinter import *
import random
import os

def buttonPressed( event ):
   print( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )
   f = random.randrange(8)
   os.system("start ./"+str(f)+".wav")


def buttonReleased( event ):
   print( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

base = tkinter.Tk()
base.title("canvas example")
base.overrideredirect(True)
base.geometry("{0}x{1}+0+0".format(base.winfo_screenwidth(), base.winfo_screenheight()))
canvas = tkinter.Canvas(base, bg="#999A86", height=base.winfo_screenheight(), width=base.winfo_screenwidth())
canvas.pack()

for i in range (8):
	for j in range (8):
		s = random.random()
		
		if((s*100//10%4) == 0):
			myfill="#999A86"
		elif((s*100//10%4) == 1):
			myfill="#949579"
		else:
			myfill="#A7A88A"
		canvas.create_rectangle(i*base.winfo_screenwidth()/8, j*base.winfo_screenheight()/8, (i+1)*base.winfo_screenwidth()/8, (j+1)*base.winfo_screenheight()/8, fill=myfill, outline=myfill)

canvas.create_rectangle(1*base.winfo_screenwidth()/8, 3*base.winfo_screenheight()/8, 7*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(1*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 2*base.winfo_screenwidth()/8, 5*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(6*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 7*base.winfo_screenwidth()/8, 5*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(1*base.winfo_screenwidth()/8, 6*base.winfo_screenheight()/8, 7*base.winfo_screenwidth()/8, 5*base.winfo_screenheight()/8, fill="black", outline="black")

canvas.create_rectangle(2*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 3*base.winfo_screenwidth()/8, 5*base.winfo_screenheight()/8, fill="yellow", outline="yellow")
canvas.create_rectangle(5*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 6*base.winfo_screenwidth()/8, 5*base.winfo_screenheight()/8, fill="yellow", outline="yellow")

canvas.create_rectangle(3*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 5*base.winfo_screenwidth()/8, 8*base.winfo_screenheight()/8, fill="#663300", outline="#663300")

# create feeler (left)
canvas.create_rectangle(2*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 3*base.winfo_screenwidth()/8, 2*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(1*base.winfo_screenwidth()/8, 2*base.winfo_screenheight()/8, 2*base.winfo_screenwidth()/8, 1*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(0*base.winfo_screenwidth()/8, 1*base.winfo_screenheight()/8, 1*base.winfo_screenwidth()/8, 0*base.winfo_screenheight()/8, fill="black", outline="black")
# create feeler (right)
canvas.create_rectangle(5*base.winfo_screenwidth()/8, 4*base.winfo_screenheight()/8, 6*base.winfo_screenwidth()/8, 2*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(6*base.winfo_screenwidth()/8, 2*base.winfo_screenheight()/8, 7*base.winfo_screenwidth()/8, 1*base.winfo_screenheight()/8, fill="black", outline="black")
canvas.create_rectangle(7*base.winfo_screenwidth()/8, 1*base.winfo_screenheight()/8, 8*base.winfo_screenwidth()/8, 0*base.winfo_screenheight()/8, fill="black", outline="black")

canvas.bind( "<Button-1>", buttonPressed )
canvas.bind( "<ButtonRelease-1>", buttonReleased )  
base.mainloop()
