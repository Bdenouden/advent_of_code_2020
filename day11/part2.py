import sys
import numpy
from pprint import pprint
from collections import Counter

layout = []

# get layout and apply flooring padding to it
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        if(not layout):
            layout.append(['.'] * (len(line.strip())+2))
        line = '.'+line.strip()+'.'
        layout.append([char for char in line])
layout.append(['.'] * len(layout[0]))


def getAdjecentSeats(x, y):
    # move out until seat is reached or end of matrix
    occupied = []
    for row in range(-1, 2):
        for col in range(-1, 2):
            occupied.append(checkWithStepSize(x, y, col, row))
    return Counter(occupied)


def checkWithStepSize(seatx, seaty, dirx, diry):
    x = seatx
    y = seaty

    while True:
        x += dirx
        y += diry
        if(             # end of matrix reached
            x == len(layout[0]) 
            or y == len(layout)
            or x == 0 
            or y == 0
            or (x == seatx and y == seaty)
        ):  
            return '.'

        char = layout[y][x]
        if char == '#':
            return '#'
        elif char == 'L':
            return 'L'

    print("This is not supposed to happen.....")
    exit()


def updateSeatOccupancy(x, y, counter):
    if layout[y][x] == 'L' and counter['#'] == 0:
        actionsLayout[y][x] = '#'
        return True
    elif layout[y][x] == '#' and counter['#'] >= 5:
        actionsLayout[y][x] = 'L'
        return True
    else:
        return False


while True:
    actionsLayout = [x[:] for x in layout] # make copy of layout to save changes
    actions = 0
    for y, val in enumerate(numpy.array(layout)[1:-1, 1:-1]):
        for x, val in enumerate(val):
            if(layout[y+1][x+1] != '.'):
                counter = getAdjecentSeats(x+1, y+1)
                actions += updateSeatOccupancy(x+1, y+1, counter)
    layout = [x[:] for x in actionsLayout] # apply changes
    if actions == 0:
        break
print(Counter([char for row in layout for char in row]))

# CORRECT!