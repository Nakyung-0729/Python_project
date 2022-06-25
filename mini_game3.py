"""
    Calculatr
"""
"""
    1. In an infinite loop, a formula is inputted by the user.
    2. Enter 'X' instead of formula to exit.
    3. Calculate the formula and print the formula and result. Prints the result right-aligned to a total of 40 spaces
    4. If the user continues to input formulas, the existing formulas are printed and
       Outputs the result of calculating the formula in addition to the existing result.
    5. If you input 'C' instead of a formula, 0 is output and all formulas are blank.
"""
from myutils import *
from colors import *

cprintTitle("Calculator for Engineering")

exp_list = []
isfirst = True

while True:

    exp = input("Enter the formula (X for exit, C for initialization):")

    if exp == 'X':
        break
    elif exp == 'C':
        print(0)
        isfirst = True
        exp_list.clear()
        continue

    if isfirst == True:
        exp1 = exp
    else:
        exp1 = str(res) + ' ' + exp

    res = eval(exp1)
    isfirst = False

    exp_list.append(exp1)

    print(exp_list)
    for e in enumerate(exp_list):
        if e[0] == len(exp_list) - 1:
            print(RED + format(e[1], '>40') + END)
        else:
            print(GREEN + format(e[1], '>40') + END)

    print(YELLOW + '-'*40 + END)
    print(format(res, '>40'))
