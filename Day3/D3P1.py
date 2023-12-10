import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
file = (r'Day3\D3input.txt')


#find all symbols and make a set of them to remove dups.
#start at first line and then find each symbol location.
#now search if there is a number left or right, up or down, diagnal,  add to list.  then set(list) to remove dups

def find_symbols(lines):
    #find all symbols in puzzle, removes dups
    junk= ('1','2','3','4','5','6','7','8','9','0','.')
    symbols =[]
    for line in lines[:10]:
        for char in line:
            if char not in junk:
                symbols.append(char)
    return set(symbols)


with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

symbols = (find_symbols(lines))

print(symbols)





