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
    else:
        print("no red")
        red = 0
        
    if bluestart != -1:
        blue = int(arg1[bluestart -3:bluestart -1])
    else:
        print("no blue")
        blue = 0

    if greenstart != -1:
        green = int(arg1[greenstart -3:greenstart -1])
    else:
        print("no blue")
        green = 0

    return (red,blue,green,)
    

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

Day= []
for i in lines:
    Day.append(i[7:].split(';'))
good =[]
for i in range(len(Day)):
    redmax = 0
    bluemax = 0
    greenmax = 0
    for round in Day[i]:       
        if colorcount(round)[0] > redmax:
            redmax = colorcount(round)[0]
        if colorcount(round)[1] > bluemax:
            bluemax = colorcount(round)[1]
        if colorcount(round)[2] > greenmax:
            greenmax = colorcount(round)[2]
    good.append(redmax*bluemax*greenmax)

print(sum(good))



    

