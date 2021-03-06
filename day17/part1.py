import sys
from pprint import pprint

zLayers = {0: list()}

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        zLayers[0].append([c for c in line.strip()])


def checkXY(Cx, Cy,  plane):
    """
    arguments: cube x, y and z.
    checks how many active neighbours there are in this XY plane
    """
    activeCount = 0
    yMin = max(Cy-1, 0)
    yMax = min(Cy+2, len(plane))

    xMin = max(Cx-1, 0)
    xMax = min(Cx+2, len(plane[0]))

    for y in range(yMin, yMax):
        for x in range(xMin, xMax):
            if(plane[y][x] == '#'):
                activeCount += 1
    # return active neighbors
    return activeCount


def checkNeigbors(Cx, Cy, Cz):
    activeCount = 0
    zLen = len(zLayers[0])

    zMin = max(Cz-1, min(zLayers))
    zMax = min(Cz+2, max(zLayers)+1)

    # check layer above and below this one
    for i in range(zMin, zMax):
        activeCount += checkXY(Cx, Cy, zLayers.get(i, [['.']*zLen]*zLen))
        # print(f"\nZ layer: {i}, Cx: {Cx}, Cy: {Cy}")

    # return active neighbors and correct for own value
    return activeCount - (zLayers[Cz][Cy][Cx] == '#')


def enforeRules(nCx, nCy, nCz, activeNb, nextCubeConfig):
    isActive = zLayers[nCz][nCy][nCx] == '#'

    if(isActive and 2 <= activeNb <= 3):
        nextCubeConfig[nCz][nCy][nCx] = '#'
    elif(not isActive and activeNb == 3):
        nextCubeConfig[nCz][nCy][nCx] = '#'
    else:
        nextCubeConfig[nCz][nCy][nCx] = '.'
    # print(f"Checking z: {nCz}, y: {nCy}, x: {nCx}, nb: {activeNb}, is #: {isActive}, changed: {zLayers[nCz][nCy][nCx] != nextCubeConfig[nCz][nCy][nCx]}")
    return nextCubeConfig


def expandSpace(space):
    zLen = len(space[0]) + 2

    for z in space:
        # append start and end .
        for y in range(len(space[z])):
            space[z][y].append('.')
            space[z][y].insert(0, '.')

        # append new top, bottom row
        space[z].insert(0, ['.']*zLen)
        space[z].append(['.']*zLen)

    # append new layers
    space[min(space)-1] = [['.']*zLen]*zLen
    space[max(space)+1] = [['.']*zLen]*zLen
    return space


cycle = 0


# its an infinite space so only the relevant parts are shown
# https://www.reddit.com/r/adventofcode/comments/ker0wi/2020_day_17_part_1_sample_input_wrong/

while cycle < 6:
    # Cycle through each element on the Z layers and the one above and below

    zLayers = expandSpace(zLayers)
    # nextSpace = copy.deepcopy(zLayers)
    nextSpace = {key: [[x for x in y] for y in val] for key, val in zLayers.items()}

    for z in range(min(zLayers), max(zLayers)+1):
        xyPlane = zLayers[z]

    # this iteration should expand each xy plane as well
        for y in range(len(xyPlane)):
            # print(f"\nz:{z}, y: {y}, x:0-{len(xyPlane[0])-1}")
            for x in range(len(xyPlane[0])):
                neighbors = checkNeigbors(x, y, z)
                # print(f"Active neighbours for this node: {neighbors}")
                nextSpace = enforeRules(x, y, z, neighbors, nextSpace)

    # print(f"Cycle: {cycle}\nCurrent \t\t\t\t Next")
    # for z in sorted(zLayers):
    #     print(f"Layer: {z}")
    #     for y in range(len(zLayers[z])):
    #         print(f"{zLayers[z][y]}\t->\t{nextSpace[z][y]}")

    zLayers = {key: [[x for x in y] for y in val] for key, val in nextSpace.items()}
    cycle += 1
    # exit('test')

counter = 0
for z in sorted(zLayers):
    for y in zLayers[z]:
        for x in y:
            if x == '#' :
                counter += 1

print(f"A total of {counter} active nodes was found")

# CORRECT!