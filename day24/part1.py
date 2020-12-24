import sys
import re


class Tile:
    all = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'white'
        Tile.all[(x, y)] = self

    def toggleColor(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'


dir = {
    'ne':   {'dx': 2,   'dy': 3},
    'e':    {'dx': 4,   'dy': 0},
    'se':   {'dx': 2,   'dy': -3},
    'sw':   {'dx': -2,  'dy': -3},
    'w':    {'dx': -4,  'dy': 0},
    'nw':   {'dx': -2,  'dy': 3},
}


with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        directions = re.findall(r"nw|sw|se|ne|w|e", line.strip())
        x, y = 0, 0
        for d in directions:
            x += dir[d]['dx']
            y += dir[d]['dy']

        tile = Tile.all.get((x, y))
        if not tile:
            tile = Tile(x, y)
        tile.toggleColor()

bTiles, wTiles = 0, 0
for tile in Tile.all.values():
    if tile.color == 'black':
        bTiles += 1
    else:
        wTiles += 1

print(f"Black tiles:  {bTiles}")

# CORRECT!
