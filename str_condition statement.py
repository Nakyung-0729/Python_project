"""
    Day03 - str, condition statement
    Version : 1.0
    Created : 2022.5.19
    Updated : 2022.5.19
    Author : Nakyung Park
"""
print("Day3 - str.format")
a = 1
print("The value of a is", a)

print("{} is another {} function of {}".format('this','print','usage'))
print("Let's see if it's a number {}".format(10))
print("When there are more inputs than parentheses {}".format('it works','I wonder'))

print("#" * 40)
print("Name:{name} Adress:{addr}".format(name='python',addr='Yeoksamdong'))

print("#" * 40)
print('Day3 - if statement')
a = 1

if a > 0:
    print("a is positive")
if a == 1:
    print("a is 1")
if not a != 1:
    print("a is not 1")

a = -100
if a > 0:
    print("a is positive 2")
   
print("a is positive 5")


if a < 0 : print("a is positive 8"); print("a is positive 9")

from colors import *
print(RED + "if-elif-else" + END )
e = -30
if e > 0:
    print("positive")
elif e == 0:
    print("zero")
else:
    print("negative")














