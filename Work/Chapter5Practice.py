#---------------------------------------------
# Name: Chapter 5 Practice
# Purpose: Practice
#
# Author: TaylorJB
#
# Created: 1/29/2025
#---------------------------------------------
age = 18
old_enough_to_get_driving_licence = age >= 17
print(old_enough_to_get_driving_licence)

age=input("How old are you?")
age=int(age)
if age < 17:
    print("Hey, you're too young to drive!")
if (age >=17):
    print("You can get your drivers licence!")

import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()