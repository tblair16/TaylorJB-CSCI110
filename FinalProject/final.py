#---------------------------------------------
# Name: Final Project
# Purpose: Final
#
# Author: TaylorJB
# Created: 5/1/2025
#----------------------------------------------
#Hangman: beep beep
import random
import turtle

#Setting up the turtle screen for hangman
wn=turtle.Screen()
wn.bgcolor("Black")
pen=turtle.Turtle()
pen.color("pink")
pen.speed(3)
wn.title("Let's Play Hangman")

#Hangman figures made by incorrect steps
def create_hangman(mistakes):
    if mistakes == 1:
        pen.penup()
        pen.goto(-100,-100)
        pen.pendown()
        pen.forward(200)
    elif mistakes == 2:
        pen.penup()
        pen.goto(-50, -100)
        pen.pendown()
        pen.goto(-50, 100)
    elif mistakes == 3:
        pen.goto(50, 100)
    elif mistakes == 4: 
        pen.goto(50, 75)
    elif mistakes == 5: 
        pen.penup()
        pen.goto(50, 60)
        pen.pendown()
        pen.circle(10)
    elif mistakes == 6:
        pen.penup()
        pen.goto(50, 50)
        pen.pendown()
        pen.goto(50, 20)
    elif mistakes == 7:
        pen.penup()
        pen.goto(50, 40)
        pen.pendown()
        pen.goto(30, 50)
    elif mistakes == 8:
        pen.penup()
        pen.goto(50, 40)
        pen.pendown()
        pen.goto(70, 50)
    elif mistakes == 9:
        pen.penup()
        pen.goto(50, 20)
        pen.pendown()
        pen.goto(30, 0)
    elif mistakes == 10:
        pen.penup()
        pen.goto(50, 20)
        pen.pendown()
        pen.goto(70, 0)
        turtle.done()
        print("Gameover. The correct word was {}".format(chosen_word))

def choose_word():
    with open("FinalProject/wordlist.txt", "r" ) as wordfile:
        words=wordfile.readlines()
    wordfile.close()
    return random.choice(words).strip()

chosen_word=choose_word()
guess_amount = 10
guessed_letters=[]

correctcount = 0
incorrectcount = 0
mistakes = 0

for i in range(guess_amount):
    guess=input("Guess a letter.").lower()
    
    if guess in guessed_letters:
        print("You guessed that letter already. Guess again!")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        correctcount += 1
        print("Correct!")
    
    else:
        incorrectcount += 1
        mistakes += 1
        print("Wrong guess.")
        create_hangman(mistakes)


    with open("FinalProject/results.txt", "w") as resultfile:
        resultfile.write("{}          {}\n".format("Correct","Incorrect"))
        resultfile.write("==========================\n")
        resultfile.write("{}............{}".format(correctcount,incorrectcount))

turtle.done()