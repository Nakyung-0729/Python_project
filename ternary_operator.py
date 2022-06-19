score = 90
text = (score > 99) and "a natural result" or "Is that a score?"
print(text)

text = "a natural result" if score > 99 else "Is that a score?"
print(text)

# Quiz
# Receive numeric input from the user.
# Outputs "WAWAWAW...." as many as the number.
# user_input:USER INPUT, result:RESULT
# while True:
#     user_input = input("Please enter a number : ")
#     if user_input.isdigit():
#         user_input = int(user_input)
#         break
#
# # General Coding
# result = ""
# for i in range(int(user_input/2)):
#     result += "WA"
# if user_input % 2 == 1:
#     result += "W"
# print(result)
#
# # Python only
# result = "WA" * int(user_input/2)
# if user_input % 2 == 1:
#     result += "W"
# print(result)
#
# # Python only, only 1 row
# result = "WA" * int(user_input/2) + "수" * (user_input%2)
# print(result)


import myutils as mu
mu.cprintTitle("Built-in Functions")
print(eval('2613623+2673283'))
print("1. eval()")
mu.printExp("200 + 500")

print("2. format()")
mu.printExp("format(34567, ',')")
mu.printExp("format(34567, '_')")

mu.printExp("format('HaHaHa', 'rain<20')")
mu.printExp("format(1234, '0>10')")
mu.printExp("format(1234, '0>+10')")
mu.printExp("format(1234, '<10')")

print("3. str(), float(), int()")
print("str(): " + str(47) + "people are present")
mu.printExp("float(10)")
mu.printExp("int(10.9)")

print("4. divmod()")
mu.printExp("divmod(10, 3)")
a = divmod(10, 3)

b = [1, 2, 2]; print(b)
c = tuple(b);  print(c)
d = set(b);    print(d)
e = list(d);   print(e)

print("5. min(), max()")
c = [1,2,3,4,5]
print(min(c), max(c))
d = ["10000000000000", "2"]
print(max(d))
d = ["10000000000000", "2", "A"]
print(max(d))
d = ["10000000000000", "2", "A", "a"]
print(max(d))

print("6. abs(), pow(), sum()")
mu.printExp("abs(-50.5)")
mu.printExp("pow(10, 2)")
mu.printExp("sum([100,200,300], 1000)")
g = [[10000,200,300],[10000,500,60000]]
print(max(g))

print("7. round")
mu.printExp("round(234.2)")
mu.printExp("round(234.2, 3)")
mu.printExp("round(2.975, 2)")
mu.printExp("round(2.685, 2)")
mu.printExp("round(2.675, 2)")
mu.printExp("round(2.675000001, 2)")

print("8. print")
print('010','1234','5678',sep='-', end='|')
print('010',1234,'5678',sep='')

print("9. input")

print("10. len()")
mu.printExp("len('abcde')")
student = ['A1','B2','Z3']
print(len(student))
print(len(student[0]))
