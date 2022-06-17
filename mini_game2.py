"""
    1. Print 'Enter your name:' and receive input.
    2. Print 'Enter the maximum number:' and accept the input.
    3. Create a random number between 1 and the number you entered.
    4. Create a game that takes a number input and guesses whether it is equal to a random number.
       How many answers are there? outputs and receives input.
       Continue until the random number equals the entered number.
       If you don't get it right 5 times, it's over.
    5. If you get the correct answer at once, '*** is amazing'.
       If you get it right within three times, '***, you have excellent grades'.
       If you get it right within five times, '*** is a bit harsh'.
       If you do not get it right five times, 'The correct answer is *. *, are you person?'
"""
nam = input('Enter your name:')

num = input('Enter the maximum number: ')
while True:
    if num.isdecimal() == True:
        break
    num = input('Enter the maximum number: ')

import random
rand_int = random.randint(1, int(num))
print(rand_int)


correct = False
for count in range(1,6):
    ans = input('What is the answer? ')
    if ans.isdecimal():
        if rand_int == int(ans):
            correct = True
            break

if count == 1:
    print('{} is amazing'.format(nam))
elif count <= 3:
    print('{}, you have excellent grades'.format(nam))
elif count <= 5 and correct == True:
    print('{} is a bit harsh'.format(nam))
else:
    print('The correct answer is {}. {}, are you person?'.format(rand_int, nam))

