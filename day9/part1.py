import sys
import collections


def checkNumber(buf):
    solutions = [num for num in buf if (buf[buf.maxlen -1] - num) in buf]
    if(not solutions):
        print(f"Invalid number: {buf.pop()}")
        exit()
    


buffer = collections.deque(maxlen=26)
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        buffer.append(int(line))
        if len(buffer) == buffer.maxlen:
            checkNumber(buffer)

# CORRECT!    
