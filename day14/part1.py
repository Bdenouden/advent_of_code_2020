import sys
import re

mask = 'X'*36
mem = {}
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        line = line.strip().split(' = ')
        if (line[0]) == 'mask':
            mask = line[1]
        else:
            bin = format(int(line[1]), '036b')
            bin = ''.join(bin[i] if mbit == 'X' else mbit for i,mbit in enumerate(mask))
            memloc = re.findall(r"\d+", line[0])[0]
            mem[memloc] = int(bin, base = 2)

print(sum(mem.values()))

# CORRECT!