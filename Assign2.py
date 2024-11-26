"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
d = input("Enter a number ")
D = float(d)
c = input("Enter a number ")
C = float(c)
A = int(input("is one of the numbers the hypotenuse of a right triangle?(put 1 for yes or 2 for no) "))
if A == 2:
    Jim = math.sqrt(D**2 + C**2)
    print(f"The missing side is {Jim}")
elif A == 1:
    if C > D:
        Tim = math.sqrt(C**2 - D**2)
        print(f"The missing side is {Tim}")
    elif D > C:
        Tim = math.sqrt(D**2 - C**2)
        print(f"The missing side is {Tim}")
    else:
        print("I'm pretty sure you lied to me")