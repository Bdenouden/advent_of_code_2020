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
    occupancy = [['X' if col == x and row == y else layout[row][col] for col in range(x-1, x+2)] for row in range(y-1, y+2)]
    return Counter([char for row in occupancy for char in row])


def updateSeatOccupancy(x, y, counter):
    if layout[y][x] == 'L' and counter['#'] == 0:
        actionsLayout[y][x] = '#'
        return True
    elif layout[y][x] == '#' and counter['#'] >= 4:
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
    print(f"A total of {actions} actions were taken this loop")
    layout = [x[:] for x in actionsLayout] # apply changes
    if actions == 0:
        break

print(Counter([char for row in layout for char in row]))

# CORRECT!