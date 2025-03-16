#---------------------------------------------
# Name: Chapter 19 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 3/12/2025
#---------------------------------------------
#1
def readposint():
    try:
        integer = int(input("Please enter a positive integer: "))
        if integer > 0:
            return integer
        else:
             # Create a new instance of an exception
            raise ValueError("{0} is not a valid positive integer".format(integer))
    except ValueError:
        print("{0} is not a valid positive integer".format(integer))
       

readposint()