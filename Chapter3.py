#---------------------------------------------
# Name: Chapter 3
# Purpose: Practice and Homework
#
# Author: TaylorJB
# Created: 1/23/2025
#----------------------------------------------
# Chapter 3 Practice
import turtle
wn=turtle.Screen()
h=input("Background Color?")
wn.bgcolor(h)
wn.title("Turtles")

Taylor=turtle.Turtle()
Taylor.pensize(3)
i=input("Taylor Turtle Color?")
Taylor.color(i)

Taylor.forward(50)
Taylor.left(90)
Taylor.forward(50)

Tesa=turtle.Turtle()
Tesa.shape("turtle")
Tesa.pensize(1)
for f in range(4):
    Tesa.forward(60)
    Tesa.left(90)

snake=turtle.Turtle()
snake.penup()
snake.forward(-50)
snake.pendown()
snake.right(90)
snake.forward(25)

turtle.done()
wn.mainloop()
