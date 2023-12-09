import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
file = (r'Day2\D2input.txt')


def colorcount(arg1):
    # max number of each color: 12 red cubes, 13 green cubes, and 14 blue 
    redstart = arg1.find("red")
    bluestart = arg1.find("blue")
    greenstart = arg1.find("green")
    if redstart != -1:
        red = int(arg1[redstart -3:redstart -1])
        if red > 12:
            red = 0
            #print("to many red")
        else:
            red = 1
    else:
        #print("no red")
        red = 1

    if bluestart != -1:
        blue = int(arg1[bluestart -3:bluestart -1])
        if blue > 14:
            blue = 0
            #print("to many blue")
        else:
            blue = 1
    else:
        #print("no blue")
        blue = 1

    if greenstart != -1:
        green = int(arg1[greenstart -3:greenstart -1])
        if green > 13:
            green = 0
            #print("to many green")
        else:
            green = 1

    else:
        #print("no green")
        green = 1

    #print(red,green,blue)

    return (red+blue+green)
    

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

modedlist= []
for i in lines:
    modedlist.append(i[7:].split(';'))

#print(modedlist)

good = []
for i in range(len(modedlist)):
    correct = []
    #print()
    total = 0
    for group in modedlist[i]:
        #print(len(modedlist[i]))
        if (colorcount(group)) == 3:
            correct.append(i+1)
            total += 1
    if total == len(modedlist[i]):
        good.append(i+1)
    
    

print(sum(good))

