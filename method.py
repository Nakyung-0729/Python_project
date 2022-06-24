from myutils import *

cprintTitle("11. range()")
printExp("range(10)")
print(range(10))
print(type(range(10)))

a = list(range(10))
print(a)
a = list(range(1,100,2))
print(a)
a = list(range(10,0,-1))
print(a)
a = list(range(0,15,-5))
print(a)

cprintTitle("12. sorted()")
student = ['A student11111','a student','B student','12345']
# ASCII : Numbers from 0x30 (16*3 + 1*0 = 48), uppercase letters from 0x41 (16*4 + 1*1 = 65), lowercase letters from 0x61(97)
student_a = sorted(student, reverse=False)
print(student_a)
student_d = sorted(student, reverse=True)
print(student_d)

cprintTitle("13. enumerate(), zip()")
print(enumerate(student))
student_e = list(enumerate(student))
print(student_e)

for s in enumerate(student):
    print(s[0], s[1])

student_i = ['30444','30122','20312','11111']
print(zip(student, student_i))
print(list(zip(student, student_i)))

for s in zip(student, student_i):
    print(s[0], s[1])

# Method
cprintTitle("Method of List")
list_a = [1, 2, 3]
print(list_a)

list_a.append(4)

print(list_a)
list_a.append("abcde")
print(list_a)

list_a.insert(2, 65555)
print(list_a)
list_a.insert(6, 88888)

print(list_a)

list_b = [4, 5, 6, 7, 8]
list_a.extend(list_b)
print('extend01', list_a)
tuple_a = (4444, 5555)
list_a.extend(tuple_a)
print('extend02', list_a)
set_a = {1233, 4566}
list_a.extend(set_a)
print('extend03', list_a)

b = list_a.pop()
print('pop01', list_a)
c = list_a.pop(0)
print('pop02', list_a)
f = list_a.remove('abcde')
print('remove01', f, list_a)
list_a.remove(4)
print('remove02', list_a)

g = list_a.index(4)
print('index01', g, list_a)

list_a.clear()
print(list_a)
