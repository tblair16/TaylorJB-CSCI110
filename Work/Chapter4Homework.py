#---------------------------------------------
# Name: Chapter 4 Homework
# Purpose: Homework
#
# Author: TaylorJB
# Created: 1/28/2025
#---------------------------------------------
#Question 2

import turtle

def draw_squares(t,sz):
    """Get turtle t to make a square"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn=turtle.Screen() #window setup
wn.bgcolor("lightgreen")
wn.title("Turtle Squares")

taylor=turtle.Turtle()
taylor.pensize(4)
taylor.speed(4)
taylor.pencolor("hotpink")

size=20  #Starting square size
for i in range(5):
    draw_squares(taylor,size)
    taylor.penup()
    taylor.forward(-20)
    taylor.right(90)
    taylor.forward(20)
    taylor.left(90)
    taylor.pendown()
    size=size+40

wn.mainloop()
