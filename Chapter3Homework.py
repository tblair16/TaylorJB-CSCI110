#---------------------------------------------
# Name: Chapter 3
# Purpose: Practice
#
# Author: TaylorJB
# Created: 1/23/2025
#----------------------------------------------
#11 Creating a Star
import turtle 
wn=turtle.Screen()
wn.bgcolor("purple")
wn.title("Star")

pen=turtle.Turtle()
pen.pensize(4)
pen.speed(5)
pen.setheading(72)
for f in range(5):
    pen.forward(100)
    pen.right(144)

#12 Creating a Turtle Clock
turtle.clearscreen()
wn.bgcolor("lightgreen")
wn.title("Turtle Clock")

clockturtle=turtle.Turtle()
clockturtle.setheading(0)
clockturtle.color("Blue")
clockturtle.shape("turtle")
clockturtle.speed(5)
clockturtle.pensize(4)
for i in range(12):
    clockturtle.penup()
    clockturtle.forward(90)
    clockturtle.pendown()
    clockturtle.forward(12)
    clockturtle.penup()
    clockturtle.forward(15)
    clockturtle.stamp()
    clockturtle.backward(120)
    clockturtle.left(30)
wn.mainloop()
turtle.Terminator