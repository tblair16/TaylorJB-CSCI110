#---------------------------------------------
# Name: Chapter 6 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 1/30/2025
#---------------------------------------------
#7 in 6.9
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def to_secs(x1, y2, z2):
    x=x1*3600
    y=y2*60
    z=z2
    result=x+y+z
    return result



def test_call():
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(20, 50, 50)== 75050)

test_call() #Call to run tests