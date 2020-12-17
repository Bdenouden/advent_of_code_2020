import sys
from pprint import pprint

space = {0: {0: list()}}


with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        space[0][0].append([c for c in line.strip()])


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


def checkNeigbors(Cx, Cy, Cz, Cw):
    activeCount = 0
    yLen = len(space[0][0])
 
    wMin = max(Cw-1, min(space))
    wMax = min(Cw+2, max(space)+1)
    
    # iterate over w space
    for w in range (wMin, wMax):
        
        # check layer above and below this one
        zMin = max(Cz-1, min(space[w]))
        zMax = min(Cz+2, max(space[w])+1)
        for i in range(zMin, zMax):
            activeCount += checkXY(Cx, Cy, space[w].get(i, [['.']*yLen]*yLen))

    # return active neighbors and correct for own value
    return activeCount - (space[Cw][Cz][Cy][Cx] == '#')


def enforeRules(nCx, nCy, nCz, nCw, activeNb, nextCubeConfig):
    isActive = space[nCw][nCz][nCy][nCx] == '#'

    if(isActive and 2 <= activeNb <= 3):
        nextCubeConfig[nCw][nCz][nCy][nCx] = '#'
    elif(not isActive and activeNb == 3):
        nextCubeConfig[nCw][nCz][nCy][nCx] = '#'
    else:
        nextCubeConfig[nCw][nCz][nCy][nCx] = '.'
    return nextCubeConfig
                


def expandSpace(space):
    yLen = len(space[0][0]) + 2       
    for w in space.copy():
        for z in space[w].copy():
            # append start and end .
            for y in range(len(space[w][z])):
                space[w][z][y].append('.')
                space[w][z][y].insert(0, '.')

            # append new top, bottom row
            space[w][z].insert(0, ['.']*yLen)
            space[w][z].append(['.']*yLen)

        # append new layers
        space[w][min(space[w])-1] =  [['.']*yLen]*yLen
        space[w][max(space[w])+1] =  [['.']*yLen]*yLen
    
    # set new w spaces
    for w in [min(space)-1, max(space)+1]:
        space[w] = {}
        for z in space[0]:
            space[w][z] = [['.']*yLen]*yLen

    return space


cycle = 0
while cycle < 6:
    # Cycle through each element on the Z layers and the one above and below

    space = expandSpace(space)    
    nextSpace = {wkey: {zkey: [[x for x in y] for y in val] for zkey, val in wval.items()} for wkey, wval in space.items()}

    for w in range(min(space), max(space)+1):
        zField = space[w]
        
        for z in range(min(zField), max(zField)+1):
            xyPlane = zField[z]

            # this iteration should expand each xy plane as well
            for y in range(len(xyPlane)):
                for x in range(len(xyPlane[0])):
                    neighbors = checkNeigbors(x, y, z, w)
                    nextSpace = enforeRules(x, y, z,w, neighbors, nextSpace)

    space = {wkey: {zkey: [[x for x in y] for y in val] for zkey, val in wval.items()} for wkey, wval in nextSpace.items()}
    cycle += 1
        
counter = 0
for w in sorted(space):
    for z in sorted(space[w]):
        for y in space[w][z]:
            for x in y:
                if x == '#':
                    counter += 1

print(f"A total of {counter} active nodes was found")

# CORRECT!
