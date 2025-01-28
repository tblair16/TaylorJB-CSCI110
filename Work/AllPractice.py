#---------------------------------------------
# Name: Practice
# Purpose: Practice
#
# Author: TaylorJB
# Created: 1/21/2025
#---------------------------------------------
#Chapter 1 Practice
print ("Hello World")
print ("Hello friend")
print ("Hello now")
print ("Hello")
print (2+2)
print(type("Hello, World!"))
print(len ("Hello world"))
print(2*6)
print(type("Hello world"))
pi=3.1459
print(pi*6)
minutes=645
hours=minutes//60
print(hours)
print (int(3.56))
print (float(173))
print (str(196))
n=input("Please enter your name")
print (5%2)
print (15%12)
print(16%4)\
#----------------------------------------------
#Chapter 3 Practice
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

#Chapter 4 Practice