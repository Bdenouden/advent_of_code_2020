import sys
import re

mask = '0'*36
mem = {}

def getAddresses(m):
    output = []
    for i in range(2**m.count('X')):
        bits = format(i, '036b')
        mout = []
        foundXs = 1
        for bit in m:
            if bit == 'X':
                mout.append(bits[-foundXs])
                foundXs+=1
            else:
                mout.append(bit)        
        mout = ''.join(mout)
        output.append(mout)
    return output

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        line = line.strip().split(' = ')
        if (line[0]) == 'mask':
            mask = line[1]
        else:
            membin = format(int(re.findall(r"\d+", line[0])[0]), '036b') # format mem addr in bin
            memmask = ''.join(membin[i] if mbit == '0' else mbit for i,mbit in enumerate(mask)) # apply mask
            adresses = getAddresses(memmask)
            for a in adresses:
                mem[a] = int(line[1])

print(sum(mem.values()))

# CORRECT!

