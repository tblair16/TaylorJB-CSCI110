#---------------------------------------------
# Name: Chapter 2
# Purpose: Homework
#
# Author: TaylorJB
# Created: 1/21/2025
#----------------------------------------------
#Problem 1: Storing each word as own variable
a="All"
b="work"
c="and"
d="no"
e="play"
f="makes"
g="Jack"
h="a"
i="dull"
j="boy."
print(a,b,c,d,e,f,g,h,i,j)

#Problem 2: Adding parenthesis to change the value of 6*1-2 from 4 to -6
print(6*(1-2))

#Problem 4:
bruce=6
print(bruce+4)

#Problem 5: Compounding Interest
#P is principal value
P=10000 
#n is number of times interest is compounded annually
n=12
#annual nominal interest rate
r=0.08
#t is the number of years
t=float(input("number of years"))
#formula for final amount after compounded interest
print(P*(1+(r/n)) ** (n*t))

#Problem 8: Clock Time
startingtime=int(input("Time Now (In Hours)"))
waitingtime=int(input("Hours Passed"))
timeaddition=startingtime+waitingtime
currenttime=((timeaddition-1)%12)+1
print(currenttime)
