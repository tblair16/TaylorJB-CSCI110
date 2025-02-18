#---------------------------------------------
# Name: Chapter 11 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 2/16/2025
#---------------------------------------------
#10
import sys

def test(did_pass):  #Setting up test suite
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Getting the test line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def replace(s, old, new):  #Function to replace old with new 
   old_wds=s.split(old)
   new_wds=new.join(old_wds)
   return (new_wds)
    

#Test Cases 
test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
