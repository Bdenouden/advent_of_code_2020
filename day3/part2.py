import sys

field = []

with open(sys.path[0] + '/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line.strip()
        field.append(line)

width = len(field[0])
length = len(field)

print(f"Length: {len(field)}, width: {len(field[0])}")


steps = [
    {
        'x': 1,
        'y': 1
    },
    {
        'x': 3,
        'y': 1
    },
    {
        'x': 5,
        'y': 1
    },
    {
        'x': 7,
        'y': 1
    },
    {
        'x': 1,
        'y': 2
    }
]

for step in steps:
    trees = 0
    x = 0
    print(step)

    for y in range(0, length, step['y']):
        print(f"Coordinates x: {x}, y: {y}")
        char = field[y][x]
        print(f"char: {char}", end='')
        if char == '#':
            print(' TREE\n')
            trees += 1
        else:
            print("\n")

        x = (x + step['x']) % (width-1)

    print(F"Number of trees: {trees}")
    step['result'] = trees

print(steps)

result = 1
for step in steps:
    result = result*step['result']

print(f"Solution = {result}")

# CORRECT!