#---------------------------------------------
# Name: Chapter 6 Practice
# Purpose: Practice
#
# Author: TaylorJB

# Created: 1/30/2025
#---------------------------------------------
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(abs(17) == 17)
    test(abs(-17) == 17)
    test(abs(0) == 0)
    test(abs(3.14) == 3.14)
    test(abs(-3.14) == 3.14)

test_suite()        # Here is the call to run the tests

def area(radius):
    b = 3.14159 * radius**2
    return b
print(area(3))
 
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result
print(distance(1, 2,3,4))

def is_divisible(x, y):
    return x % y == 0
print(is_divisible(2,1))