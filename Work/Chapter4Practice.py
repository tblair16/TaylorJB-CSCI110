#---------------------------------------------
# Name: Practice
# Purpose: Practice
#
# Author: TaylorJB
#
# Created: 1/28/2025
#---------------------------------------------
import turtle
def draw_square(t,sz):
    """Make turtle t draw a square of sz"""
    for i in range(4):
      t.forward(sz)
      t.left(90)

def draw_rectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex=turtle.Turtle()
draw_square (alex,50)
draw_rectangle (alex,50,30)
wn.mainloop()