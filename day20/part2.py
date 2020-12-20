import sys
import re
import numpy as np
from pprint import pprint
from copy import deepcopy


class Tile():
    def __init__(self, id, T, R, B, L, content):
        self.id = id
        self.edge = {}
        self.edge[0] = T
        self.edge[90] = R
        self.edge[180] = B
        self.edge[270] = L
        self.rotation = 0
        self.content = np.array(content)
        self.match = {
            0: None,
            180: None,
            270: None,
            90: None
        }
        self.isBTFlipped = False  # bottom and top flipped
        self.flippedEdge = {
            0: False,
            180: False,
            270: False,
            90: False
        }

    def checkIfFlipped(self):
        temp = True
        for k,e in self.match.items():
            if e is not None:
                temp *= self.flippedEdge[k]
        self.isBTFlipped = temp
        return self.isBTFlipped

tiles = []

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        line = line.strip()
        newId = re.findall(r"\d+", line)
        if not line:
            continue
        elif newId:
            id = int(newId[0])
            row = 0
            R = ''
            L = ''
            T = ''
            content = []

        else:  # append tile to current tile if applicable and fix orientation clockwise
            L += line[0]
            R += line[9]

            if row == 0:
                T = line
            elif row == 9:
                tiles.append(Tile(id, T, R, line[::-1], L[::-1], content))
            else:
                content.append(line[1:9])
            row += 1


print(f"{len(tiles)} tiles were found")


def checkForEdgeMatch(tile1, tile2):
    for key1, edge1 in tile1.edge.items():
        edge = edge1[::-1]
        # print(f"Checking tile {tile1.id} edge {key1} {edge} against {tile2.id} {tile2.edge}")
        for key2, edge2 in tile2.edge.items():
            if(edge == edge2):
                # print(f"Match: {tile1.id} edge {key1} connects to {tile2.id} edge {key2}")
                tile1.match[key1] = tile2.id
                tile2.rotation = (key1 + tile1.rotation - key2 - 180) % 360
            elif(edge == edge2[::-1]):
                # print(f"Match: {tile1.id} edge {key1} connects to {tile2.id} edge {key2} Flipped")
                tile1.match[key1] = tile2.id
                tile1.flippedEdge[key1] = True # returns true for each tile bordering a flipped tile


# find possible neighbors
for tile1 in tiles:
    for tile2 in tiles:
        # don't check against self
        if tile1 == tile2:
            continue
        checkForEdgeMatch(tile1, tile2)
    tile1.checkIfFlipped()
    if len([True for e in tile1.match.values() if e is not None]) == 2:
        print(f"{tile1.id} is a corner\n\tRotation = {tile1.rotation}\n\tmatches = {tile1.match}")
print(f"EOF")

# left top corner is tile with id 1093