from myutils import *

cprintTitle("Global, Local Variables")

# Step 1
gv = 10

def printVar1():
    print("Step 1 gv :", gv)

printVar1()

# Step 2
def printVar2():
    lv = 20
    print("Step 2 gv :", gv)
    print("Step 2 lv :", lv)
printVar2()
print("Step 2 gv :", gv)

# Step 3
def printVar3():
    gv = 30
    lv = 30
    print("Step 3 gv :", gv)
    print("Step 3 lv :", lv)
printVar3()
print("Step 3 gv :", gv)

# Step 4
def printVar4(gv):
    print("Step 4 gv :", gv)
    gv = 40
    lv = 40
    print("Step 4 gv :", gv)
    print("Step 4 lv :", lv)
printVar4('abcd')
print("Step 4 gv :", gv)

# Step 5
def printVar5():
    lv = 50
    return lv
gv = printVar5()
print("Step 5 gv :", gv)

# Step 6
gv1 = 61
gv2 = 62

def printVar6():
    global gv1
    gv1 = 601
    globals()['gv2'] = 602
    gv2 = 702

printVar6()
print("Step 6 gv1 :", gv1)
print("Step 6 gv2 :", gv2)

# Step 7
if gv1 == 601:
    lv1 = 300

print("Step 7 lv1 :", lv1)

# Step 8
i = 9268226
for i in range(5):
    print(i)

print("Step 8 i :", i)

cprintTitle("Time module")
import time
t1 = time.time()
t2 = time.ctime(t1)
t3 = time.strftime('%Y%m%d %H%M%S')
print("time.time() :", t1)
print("time.ctime() :", t2)
print("time.strftime() :", t3)

cprintTitle("File In/Out")
s1 = 'We are studying Python.'
s2 = 'We are studying Python2.'

f = open("sample.txt", "wt", encoding='utf-8') 
f.write(s1)
f.write('\n')
f.write(s2)
f.close()

f = open("sample.txt", "rt", encoding='utf-8')
while True:
    readstr = f.readline()
    if readstr == '':
        break
    print(readstr)
