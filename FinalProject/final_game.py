#---------------------------------------------
# Name: Final Project
# Purpose: Final
#
# Author: TaylorJB
# Created: 5/1/2025
#----------------------------------------------
#Hangman:
import random
import turtle
import sys

keep_playing = True

#Setting up the turtle screen for hangman
wn=turtle.Screen()
wn.bgcolor("Black")
pen=turtle.Turtle()
pen.color("pink")
pen.speed(3)
wn.title("Let's Play Hangman: Animal Edition")

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

def choose_word():
    with open("FinalProject/wordlist.txt", "r" ) as wordfile:
        words=wordfile.readlines()
    wordfile.close()
    return random.choice(words).strip()


def playgame():
    chosen_word=choose_word()
    guessed_letters=[]

    correctcount = 0
    incorrectcount = 0
    mistakes = 0

    print("Welcome to Hangman. The theme is zoo animals. Get ready!")

    while mistakes<10:
        guess=input("Guess a letter: ").lower()
        
        if not guess.isalpha():
            print("Invalid character, please guess again!")
            continue
    
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
        
        word_guessed = all(letter in guessed_letters for letter in chosen_word)
        if word_guessed:
            print("Congratulations! You guessed your word: {}.".format(chosen_word))
            break

    if mistakes == 10: #Result when the player loses the game 
        print ("The game is over. The correct word was {}".format(chosen_word))


    with open("FinalProject/results.txt", "w") as resultfile:
        resultfile.write("{}          {}\n".format("Correct","Incorrect"))
        resultfile.write("==========================\n")
        resultfile.write("{}...................{}".format(correctcount,incorrectcount))
    
    pen.clear()

#-----------------------------------------------------------
#Unit Testing
#Check to see if letter guess is in the word
def unit_test_guess(chosen_word, guess, result): 
    userguess = guess in chosen_word
    if userguess == result:
        return "Pass"
    else:
        return "Fail"

#Check to see if the whole word has been guessed correctly
def unit_test_word(chosen_word, guessed_letters, result):
    userguess = all(letter in guessed_letters for letter in chosen_word)
    if userguess == result:
        return "Pass"
    else:
        return "Fail"

def test_suite():
    test1 = unit_test_guess("elephant", "e", True)
    print(f"Test 1, correct guess: {test1}")

    test2 = unit_test_guess("lion", "f", False)
    print(f"Test 2, incorrect guess: {test2}")

    test3 = unit_test_word("zebra", ["z","e","b","r","a"], True)
    print(f"Test 3, word correctly guessed: {test3}")

    test4 = unit_test_word("monkey", ["m","o","n"], False)
    print(f"Test 4, word not fully guessed: {test4}")

    test5 = unit_test_word("tiger", ["x","y","z"], False)
    print(f"Test 5, all wrong letters: {test5}")

    print("Testing complete")
#--------------------------------------------------------------



test_suite()

#Running code, everything above this is functions
while keep_playing == True:
    playgame() 
    gameplay = str(input("Would you like to keep playing?(Y/N)"))
    if gameplay == "N":
        keep_playing = False   

turtle.done