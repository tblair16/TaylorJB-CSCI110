#---------------------------------------------
# Name: Chapter 5 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 1/29/2025
#---------------------------------------------
#Question 1
def day_name(day): #Defining function 
    if day==0:
        return("Sunday")
    if day==1:
        return("Monday")
    if day==2:
        return("Tuesday")
    if day==3:
        return("Wednesday")
    if day==4:
        return("Thursday")
    if day==5:
        return("Friday")
    if day==6:
        return("Saturday")
    else: #If day is not between 0 and 6, then an error will occur
        return "Invalid day number"

day=int(input("What is the day number?")) #User input
print(day_name(day)) #Calling day_name function and printing result


#question 8 Modify turtle bar chart
def bar_color(t,height):
    """ Get turtle t to draw one bar, of height. """
    if height<100:
        t.fillcolor("green")
    elif height <200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("red")

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    bar_color(t,height)  
    t.begin_fill()    
    t.left(90)
    t.forward(height)
    t.write(""+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()