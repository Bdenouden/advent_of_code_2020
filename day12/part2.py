import sys
import re

# ship coordinates
x = 0   # E = +x, W = -x
y = 0   # N = +y, S = -y

# waypont coordinates
wayx  = 10
wayy  = 1

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        inst, val = re.split(r"(\d+)", line.strip())[:2]
        val=int(val)
        if(inst == 'F'): 
            x += wayx * val
            y += wayy * val

        elif(inst == 'R' or inst == 'L'): 
            for n in range(int(val/90)):
                temp = wayx
                wayx = wayy * (-(inst == 'L') + (inst =='R'))
                wayy = -temp * (-(inst == 'L') + (inst =='R'))

        elif(inst == 'N'): wayy+=val
        elif(inst == 'S'): wayy-=val
        elif(inst == 'E'): wayx+=val
        elif(inst == 'W'): wayx-=val

        # print(f"INST: i = {inst}, val = {val}")
        # print(f"SHIP: x = {x}, y = {y}")
        # print(f"WAYP: x = {wayx}, y = {wayy}\n")
        

print(f"x = {x}, y = {y}, dist = {abs(x) + abs(y)}")

# CORRECT!
        