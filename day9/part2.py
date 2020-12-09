import sys
from collections import deque

invalid_number = 36845998

buffer = deque()
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        buffer.append(int(line))
        # while the buffer is larger then the invalid number, remove items to the left to displace the set
        while sum(buffer) > invalid_number:
            buffer.popleft()

        if(sum(buffer) == invalid_number):
            print(
                f"\nSolution found! sorted buffer: {sorted(buffer)}\nSmallest number: {sorted(buffer)[0]}, largest number {sorted(buffer)[-1]}")
            print(f"Puzzel solution: {sorted(buffer)[0] + sorted(buffer)[-1]}")
            exit()

# CORRECT!