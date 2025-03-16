#---------------------------------------------
# Name: Chapter 13 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 2/24/2025
#---------------------------------------------
#1
def readbackwards(oldfile, newfile): #Creating function to reverse order of words
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")

    text = infile.readlines()
    text.reverse()
    for line in text:
        outfile.write(line) 
    infile.close()
    outfile.close()

readbackwards("oldfile.txt","newfile.txt")