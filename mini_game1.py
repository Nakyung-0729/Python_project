"""
    1. Print "Enter your name" and receive input.
    2. Print "Enter the last digit of your social security number" and receive the input.
    3. "Month" if the last digit is 1,6 .... "Fri" if 5,0
    4. "***'s inoculation date is *day of the week. Please follow the day of the week."
"""
# 1.
nam = input("Enter your name : ")

# 2.
fnum = input("Enter the last digit of your social security number : ")

# 3-1 Math
if int(fnum) % 5 == 1:
    day = "mon"
elif int(fnum) % 5 == 2:
    day = "tue"
elif int(fnum) % 5 == 3:
    day = "wed"
elif int(fnum) % 5 == 4:
    day = "thur"
else:
    day = "fri"

# 3-2
if fnum == "1": day = "mon"
elif fnum == "2": day = "tue"
elif fnum == "3": day = "wed"
elif fnum == "4": day = "thur"
elif fnum == "5": day = "fri"
elif fnum == "6": day = "mon"
elif fnum == "7": day = "tue"
elif fnum == "8": day = "wed"
elif fnum == "9": day = "thur"
elif fnum == "0": day = "fri"

# 3-3
if fnum in "16": day = "mon"
elif fnum in "27": day = "tue"
elif fnum in "38": day = "wed"
elif fnum in "49": day = "thur"
elif fnum in "50": day = "fri"

# if fnum in ["1","6"]:

# 4.
print("{}'s inoculation date is {} day of the week. Please keep the day of the week.".format(nam,day))
