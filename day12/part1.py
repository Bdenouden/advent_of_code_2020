import sys
import re

# ship coordinates
x = 0   # E = +x, W = -x
y = 0   # N = +y, S = -y

dir = ['N', 'E', 'S', 'W']
dirInd = 1
instructions = []

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        inst, val = re.split(r"(\d+)", line.strip())[:2]
        val=int(val)
        if(inst == 'F'): inst = dir[dirInd]

        if(inst == 'N'): y+=val
        elif(inst == 'S'): y-=val
        elif(inst == 'E'): x+=val
        elif(inst == 'W'): x-=val
        elif(inst == 'R'): dirInd = int((dirInd + (val/90)) % 4)
        elif(inst == 'L'): dirInd = int((dirInd - (val/90)) % 4)

print(f"x = {x}, y = {y}, dist = {abs(x) + abs(y)}")

# CORRECT!

        