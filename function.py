from colors import *
from myutils import *

tuple_a = (1,2)
print(tuple_a.index(2))

cprintTitle("Set Method")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a.intersection(b)
d = a.union(b)
e = a.difference(b)
print(c, d, e)

cprintTitle("Dictionary Method")
dic = {1: 'one', 'subject':['science','korean'], 'Number':1234}
print(dic)
print(dic[1])
print(dic.keys())  
print(list(dic.keys()))  
print(dic.values())
print(dic.items())

print('dic[1]', dic[1])
print('dic.get(1)', dic.get(1))

print('dic.get(8)', dic.get(8))
print(dic.get(8, "there is no such value"))

person = {'name':'David', 'age':5}

for item in person:
    print(item, person.get(item))

for item in person.items():
    print(item[0], item[1])

cprintTitle("String")
a = "abcdefg"
print(a)
print(a[0], a[1], a[2], a[5])
print(a[1:3])
print(a[3:])
print(a[3::2])

cprintTitle("Array copy")
a = list(range(1,11))
print(a)
b = a[1:8]
print(b)
c = a[1:8:2]
print(c)
d = a[1:]
print(d)

e = (1, 2, 3, 4, 5)
f = e[2:]
print(f)

g = {1, 2, 3, 4, 5}

h = g

cprintTitle("User Function")
printMessage1()
printMessage2("Happy")
printMessage3("Unhappy")
printMessage3()
printMessage4("HHH", 3)
printMessage4(888)
printMessage4(i=10)

val = getRandomDice(10000)
print(val)

v1, v2, v3 = getMultiDice(100)
print(v1, v2, v3)
v = getMultiDice(100)
print(v)

s = addAll(2,3,4,5,6,7,78,9)
print(s)
s = addAll()
print(s)

test = input("Enter the phone number : ")
a, b, c = checkPhoneNumber(test)
print(a, b, c)
