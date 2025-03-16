#---------------------------------------------
# Name: Chapter 7 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 2/7/2025
#---------------------------------------------
# Problem 9 Printing triangular numbers

def print_triangular_numbers(n):
    for i in range (1,n+1):
        number= i*(i+1)//2
        print(i,number)

n=int(input("How many triangular numbers?"))
print_triangular_numbers(n)