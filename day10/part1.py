import sys
from collections import Counter

adapters = [0]
with open(sys.path[0] + '/test.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.append(max(adapters) + 3) # append output voltage
adapters.sort()

differences = [adapters[i+1] - val for i, val in enumerate(adapters[:-1])]
jumps = Counter(differences)
print(f"\n#1J: {jumps[1]}, #3J: {jumps[3]}\nAnswer: {jumps[1]*jumps[3]}")

# CORRECT!