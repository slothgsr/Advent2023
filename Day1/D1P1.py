import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
file = (r'Day1\D1input.txt')


def findnumbers(arg1):
    FN = None   
    LN = None
    for i in arg1:
        try:
            i == int(i)
            if i.isdigit:
                FN = i
            break
        except:
            continue
    for i in arg1[::-1]:
        try:
            i == int(i)
            if i.isdigit:
                LN = i
            break
        except:
            continue
    return int(FN+LN)
        

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

numberlist = []
for i in lines:
    numberlist.append(findnumbers(i))
print(sum(numberlist))



