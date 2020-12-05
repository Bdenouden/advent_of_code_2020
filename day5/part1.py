import sys

# F = 0, B = 1
# L = 0, R = 1

# check if id >= current highest id, if so: save; else: discard
maxId = 0

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(line[7:].replace('L', '0').replace('R', '1'), 2)
        sid = 8 * row + col
        if (sid>maxId):
            maxId = sid
        print(f"row={row}\t col={col}\t sid={sid}\t max={maxId}")

# CORRECT!