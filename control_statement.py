"""
    Day04 - control statement
    Version : 1.0
    Created : 2021.10.5
    Updated : 2021.10.5
    Author : Nakyung Park
"""
from colors import *
print(RED + "While" +END)
print('print 1')
print('print 2')
print('print 3')
print('print 4')
print('print 5')
print('print 6')
print('print 7')
print('print 8')
print('print 9')
print('print 10')
print()

print('automation')
i = 1
while i < 11:
    print('print {}'.format(i))
    i = i + 1

i = 0
while i < 10:
    i = i + 1
    print(i)

i = 0

print(GREEN + 'for' + END)
for s in 'strings':
    print(s, end='-')

print()
for l in ['first','second','third']:
    print(l)

print()
season4 = ('Spring','Summer','Fall','Winter')
for t in season4:
    print(t)

print()
season4 = {'Spring','Summer','Fall','Winter'}
for t in season4:
    print(t)

print()
for i in range(1,11):
    print('print {}'.format(i))

print()
person = {'name':'py','age':[100,200,300]}
for i in person:
    print(i, person[i], person.get(i))

# Bringing dict to key-value pair
for key, item in person.items():
    print(key, item)
