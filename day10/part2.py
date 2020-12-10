import sys

adapters = [0]
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.append(max(adapters) + 3)  # append output voltage
adapters.sort()

differences = [adapters[i+1] - val for i, val in enumerate(adapters[:-1])]

ones = 0
result = 1
for val in differences:
    if(val == 1):
        ones += 1
    elif(ones > 0):
        # result =  P(2^(ones - 1) [- correction if more than 3 1's in a row] )
        result *= 2**(ones-1) - ((ones % 3) * (ones > 3))
        ones = 0

print(f"result = {result}")

# CORRECT!