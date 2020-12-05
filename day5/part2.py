import sys

# F = 0, B = 1
# L = 0, R = 1

# check if id >= current highest id, if so: save; else: discard
seats=[]

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(line[7:].replace('L', '0').replace('R', '1'), 2)
        sid = 8 * row + col
        seats.append(sid)
    
seats.sort()
for i in range(0, len(seats)-1):
    if(seats[i+1]-seats[i] > 1):
        print(f"seat-1: {seats[i]}, seats+1:{seats[i+1]} -> your seat: {seats[i+1]-1}")

# CORRECT!