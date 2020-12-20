import sys
import re

tiles = dict()

with open(sys.path[0] + '/test.txt') as f:
    for line in f:
        line = line.strip()
        newId = re.findall(r"\d+", line)
        if not line:
            continue
        elif not newId: # append tile to current tile if applicable
            L += line[0]
            R += line[9]
            if row == 0:
                tiles[id].append(line)
            elif row == 9:
                tiles[id].append(line)
                tiles[id].append(L)
                tiles[id].append(R)
            row += 1
        else: 
            id = int(newId[0])
            tiles[id] = list()
            row = 0
            R = ''
            L = ''

print(f"{len(tiles)} tiles were found")

def checkForEdgeMatch(selfId, edge):
    matching_tiles = []
    for id in tiles: 
        if id == selfId:
            continue
        if edge in tiles[id] or edge[::-1] in tiles[id]:
            matching_tiles.append(id)
    return matching_tiles

# find possible neighbors
solution = 1
for id in tiles:
    tile = tiles[id]
    matches = []
    for edge in tile:
        connectingEdges = checkForEdgeMatch(id, edge)
        for e in connectingEdges:
            matches.append(e)
    if(len(matches) == 2):
        solution *= id
    print(f"tile {id} matches tiles {matches}")

print(f"Solution: {solution}")

# CORRECT!