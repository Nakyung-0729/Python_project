"""
    Day02 - print, input, operator
    Version : 1.0
    Created : 2021.9.23
    Updated : 2022.9.23
    Author : Nakyung Park
"""
RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

print(RED + '1.print' + END)

# 1. print Hello and name
print('Hello ' + 'Nakyung', end='|')
print()

# 2. Mary's cosmetics
print("Mary's cosmetics")
print('Mary\'s cosmetics')

# 3. Shin shouted 'It's a thief'
print('Shin shouted "It's a thief".')
print('Shin shouted \"It's a thief"\')

# 4. when a = 'first', b = 'second', print 'first second'
a = 'first'
b = 'second'
print(a + " " + b)
print(a, b)

print(GREEN + '3.operator' + END)

a = 'My name'
b = 'is None'
print(a + ' ' + b)
c = 'I\'ll be'
d = 100
print(c + ' ' + str(d))

print('10 - 10.9 =', 10 - 10.9)

print('Hi' * 5)

print('10 // 3 ->', 10 // 3)
print('10 % 3 ->', 10 % 3)
print('5 ** 1.25 ->', 5 ** 1.25)


a = 30
b = 20
c = not (a > b)
print(c)
print(type(c))
print('10 > 10 :', 10 > 10)
print('10 >= 10 :', 10 >= 10)
print('10 == 20 :', 10 == 20)
print('a != b :', a != b)


