import sys

field = []

with open(sys.path[0] + '/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line.strip()
        field.append(line)

width = len(field[0])

print(f"Length: {len(field)}, width: {len(field[0])}")

trees = 0
x = 0
for y, line in enumerate(field):
    print(f"Coordinates x: {x}, y: {y}")
    char = line[x]
    print(f"char: {char}",end='')
    if char == '#':
        print(' TREE\n')
        trees+=1
    else:
        print("\n")

    x = (x + 3) % (width-1)

print(F"Number of trees: {trees}")

# CORRECT!