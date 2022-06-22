import random

def cprintTitle(str):
    col = random.randint(0,255)
    print("\033[38;5;{}m".format(col))
    print("*" * 40)
    print(str)
    print("*" * 40)
    print("\033[0m")

def printExp(str):
    print(str + "=> {}".format(eval(str)))

def printMessage1():
    print('***********')

def printMessage2(message):
    print(message)

def printMessage3(message='You did not enter'):
    print(message)

def printMessage4(message='Nothing', i=5):
    for j in range(i):
        print(message)

def getRandomDice(i=6):
    r = random.randint(1, i)
    return r

def getMultiDice(i=6):
    r1 = random.randint(1, i)
    r2 = random.randint(1, i)
    r3 = random.randint(1, i)
    return r1, r2, r3

def addAll(*i):
    res = 0
    for j in i:
        res = res + j
    return res

"""
    1. Check if str consists only of numbers and '-'
    2. Check if the number is 10 or 11 digits
    3. If it is 10 digits, return XXX, XXX, XXXX
       If it is 11 digits, return XXX, XXXX, XXXX
    4. If abnormal, return 999, 9999, 9999
"""
def checkPhoneNumber(str):
    ndigit = 0
    nstring = ""

    for c in str:
        if c in "0123456789-":
            if c == '-':
                pass
            else: 
                ndigit = ndigit + 1
                nstring = nstring + c
        else:
            return '999', '9999', '9999'

    if ndigit == 10:
        return nstring[0:3], nstring[3:6], nstring[6:]
    elif ndigit == 11:
        return nstring[0:3], nstring[3:7], nstring[7:] 
    else:
        return '999', '9999', '9999'
