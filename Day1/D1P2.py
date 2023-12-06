import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
file = (r'Day1\D1input.txt')

def change_to_nums(words):
    newline =[]
    words = words.replace('oneight','18')
    words = words.replace('twone','21')
    words = words.replace('threeight','38')
    words = words.replace('fiveight','58')
    words = words.replace('sevenine','79')
    words = words.replace('eightwo','82')
    words = words.replace('nineight','98')
    words = words.replace('one','1') 
    words = words.replace('two','2')
    words = words.replace('three','3')
    words = words.replace('four','4')
    words = words.replace('five','5')
    words = words.replace('six','6')
    words = words.replace('seven','7')
    words = words.replace('eight','8')
    words = words.replace('nine','9')
    return words
                


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



newlist = []


for i in lines:
    newlist.append(change_to_nums(i))



numberlist = []

for i in newlist:
    numberlist.append(findnumbers(i))
print(numberlist)
print(sum(numberlist))


