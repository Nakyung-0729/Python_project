"""
    Day02 - print, input, operator
    Version : 1.0
    Created : 2022.5.17
    Updated : 2022.5.17
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

# 3. 신씨가 "도둑이야"라고 소리쳤다.
print('신씨가 "도둑이야"라고 소리쳤다.')
print('신씨가 \"도둑이야\"라고 소리쳤다.')

# 4. a = 'first', b = 'second'일 때 first second를 출력하시오
a = 'first'
b = 'second'
print(a + " " + b)
print(a, b)

# print(RED + "2.input" + END)
# a = input()
# print(a)
# b = input("값을 입력하세요 : ")
# print(b)
# a, b = input("두 개의 값을 입력하세요 : ").split(" ")
# c = a + b
# a1 = float(a)
# b1 = float(b)
# c = int(a1) + int(b1)
# d = float(a) + float(b)
# print(a, b, "연산결과:", c, d)

print(GREEN + '3.operator' + END)
print('(1)산술연산자')
a = 'My name'
b = 'is None'
print(a + ' ' + b)
c = 'I\'ll be'
d = 100
print(c + ' ' + str(d))

print('10 - 10.9 =', 10 - 10.9)
# print('my name' - 'my') # 오류, 문자열의 뺄셈은 불가

print('안녕' * 5)
# print('ddd' / 3) # 오류, 문자열의 나눗셈은 불가

print('10 // 3 ->', 10 // 3)
print('10 % 3 ->', 10 % 3)
print('5 ** 1.25 ->', 5 ** 1.25)

print('(2)비교연산자')
a = 30
b = 20
c = not (a > b)
print(c)
print(type(c))
print('10 > 10 :', 10 > 10)
print('10 >= 10 :', 10 >= 10)
print('10 == 20 :', 10 == 20)
print('a != b :', a != b)


