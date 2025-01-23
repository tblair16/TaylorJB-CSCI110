#---------------------------------------------
# Name: Chapter 3
# Purpose: Practice
#
# Author: TaylorJB
# Created: 1/23/2025
#----------------------------------------------
import turtle #Setting up the canvas
wn=turtle.Screen()
wn.bgcolor("purple")
wn.title("Star")

pen=turtle.Turtle()
pen.pensize(4)
pen.speed(1)
pen.setheading(72)
for f in range(5):
    pen.forward(100)
    pen.right(144)

wn.mainloop()