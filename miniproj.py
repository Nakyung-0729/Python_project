"""
    Mini Project
    Version : 1.0
    Created : 2021.11.8
    Updated: 2021.12.2
    Author : Nakyung Park
"""
"""
    1. Obtain one random weapon out of 5 types from the treasure chest.
    2. On the way, you will meet a wolf, a bandit, or a dragon at random.
    3. Take a weapon and fight until the energy of one of them is zero.
       The user chooses either attack or recovery, and the opponent only attacks.
    4. Print a message according to victory or defeat.
"""
import time
from colors import *
print("*" * 40)
print("Starting Game of Destiny")
print("*" * 40)

print("You gain " + YELLOW + "[treasure box]" + END)
input("Press any key")

weapon_list = [["Tissue", 1, 3], ["Wood Sword", 3, 5], ["Sword", 5, 10], ["Cannon", 1, 50], ["Gun", 50, 100]]
import random
sel = random.randint(0,4)
print(sel)   
weapon = weapon_list[sel]
print(weapon)

if sel == 0:
    print("You have earned [{}]({}-{}).".format(weapon[0], weapon[1], weapon[2]))
elif sel == 1:
    print("You gain" + GREEN + "[{}]({}-{})".format(weapon[0], weapon[1], weapon[2]) + END)
elif sel == 2:
    print("You gain" + BLUE + "[{}]({}-{})".format(weapon[0], weapon[1], weapon[2]) + END)
elif sel == 3:
    print("You gain" + YELLOW + "[{}]({}-{})".format(weapon[0], weapon[1], weapon[2]) + END)
elif sel == 4:
    print("You gain" + MAGENTA + "[{}]({}-{})".format(weapon[0], weapon[1], weapon[2]) + END)

time.sleep(1)

MYIMAGE = "AAAAAAAAAA"
MONIMAGE = ["BBBBBBBBBB", "CCCCCCCCCC", "DDDDDDDDDD"]

mon_list = [["Wolf", 1, 3], ["Bandit", 5, 10], ["Dragon", 1, 100]]
sel2 = random.randint(0, 2)
mon = mon_list[sel2]
if sel2 == 0:
    print("On the way, you met [{}]({}-{}).".format(mon[0], mon[1], mon[2]))
elif sel2 == 1:
    print("On the way, you met " + GREEN + "[{}]({}-{})".format(mon[0], mon[1], mon[2]) + END)
elif sel2 == 2:
    print("You unfortunately met " + RED + "[{}]({}-{})".format(mon[0], mon[1], mon[2]) + END)

my_energy = 100
mon_energy = 100

while True:
    while True:
        user_input = input("Choose an action (1.attack, 2.recover):")
        if user_input in ["1", "2"]:
            break

    if user_input == "1":
        damage = random.randint(weapon[1], weapon[2])
        mon_energy = mon_energy - damage  
        print("You deal {} damage with your attacks. {} energy: {}".format(damage, mon[0], mon_energy))
        if mon_energy < 0:
            mon_energy = 0

        print(MYIMAGE + " " * 11 + MONIMAGE[sel2])
        energy_str = ""
        if my_energy > 30:
            energy_str += GREEN_BG + " " * int(my_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(my_energy / 5) + END

        energy_str += " " * (21 - int(my_energy / 5))

        if mon_energy > 30:
            energy_str += GREEN_BG + " " * int(mon_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(mon_energy / 5) + END

        print(energy_str)

        if mon_energy <= 0:
            break

    elif user_input == "2":
        heal = random.randint(0, 30)
        my_energy = my_energy + heal
        if my_energy > 100:
            my_energy = 100

        print("You have recovered {} energy from your recovery. your energy: {}".format(heal, my_energy))

        print(MYIMAGE + " " * 11 + MONIMAGE[sel2])
        energy_str = ""
        if my_energy > 30:
            energy_str += GREEN_BG + " " * int(my_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(my_energy / 5) + END

        energy_str += " " * (21 - int(my_energy / 5))

        if mon_energy > 30:
            energy_str += GREEN_BG + " " * int(mon_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(mon_energy / 5) + END

        print(energy_str)

    time.sleep(1)

    damage = random.randint(mon[1], mon[2])
    my_energy = my_energy - damage
    print("You took {} damage from {} attacks. your energy {}".format(mon[0], damage, my_energy))

    if my_energy < 0:
        my_energy = 0

    print(MYIMAGE + " " * 11 + MONIMAGE[sel2])
    energy_str = ""
    if my_energy > 30:
        energy_str += GREEN_BG + " " * int(my_energy / 5) + END
    else:
        energy_str += RED_BG + " " * int(my_energy / 5) + END

    energy_str += " " * (21 - int(my_energy / 5))

    if mon_energy > 30:
        energy_str += GREEN_BG + " " * int(mon_energy / 5) + END
    else:
        energy_str += RED_BG + " " * int(mon_energy / 5) + END

    print(energy_str)

    if my_energy <= 0:
        break

if my_energy > 0:  
    print("{} said. You're strong....".format(mon[0]))
    time.sleep(1)
    print("But on the Black Continent, there are 2917 people stronger than me.")
else:  
    print("{} said. 'Hahaha I can't beat you...'".format(mon[0]))
    time.sleep(1)
    print("He took my luxury bag")

print("The End")
