import sys
import re
import numpy as np

# define orientation parameters
up, right, down, left = 0, 1, 2, 3


class Tile:
    all = dict()
    fixed = []

    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.match = {dir: None for dir in [up, right, down, left]}

    def getEdge(self, edge=up):
        if(edge == up):
            return [c for c in self.content[0]]
        elif edge == down:
            return [c for c in self.content[-1]]
        elif edge == right:
            return [c[-1] for c in self.content]
        elif edge == left:
            return [c[0] for c in self.content]
        else:
            exit(f"Invalid edge called for tile {self.id}")

    def getContent(self):
        return np.array([line[1:-1] for line in self.content[1:-1]])

    def rotateCW(self, k):
        self.content = np.rot90(self.content, k=k, axes=(1, 0))

    def flipud(self):
        self.content = np.flipud(self.content)

    @classmethod
    def fromInput(cls, string):
        info = string.strip().split("\n")
        id = re.findall(r"\d+", info[0])[0]
        content = np.array([[c for c in line] for line in info[1:]])
        cls.all[id] = cls(id, content)


def checkFixedEdges(tile):
    """
    Move the `tile` around the edges of the fixed tiles until it fits, 
    then ensure all adjacent tiles are added to the tile.match dict.

    Returns `True` if the tile could be fitted to the fixed tiles, else `False`
    """
    succes = False
    for refTile in [Tile.all[id] for id in Tile.fixed]:
        for dir in [dir for dir in refTile.match if refTile.match[dir] is None]:
            dir2 = (dir+2) % 4
            if np.array_equal(refTile.getEdge(dir), tile.getEdge(dir2)):
                if(refTile.match[dir] is not None):
                    exit(
                        f"refTile {refTile.id} matches both {refTile.match[dir]} and {tile.id} on the same side")
                refTile.match[dir] = tile.id
                tile.match[dir2] = refTile.id
                succes = True
    return succes


def checkTileMatch(tile):
    """
    Try to attach the `tile` argument to the fixed tiles
    """
    for f in ['non-flipped', 'flipped']:
        if(f == 'flipped'):
            tile.flipud()
        for k in [0, 1, 1, 1]:      # check each rotation, first no rotation
            tile.rotateCW(k)
            if checkFixedEdges(tile):
                Tile.fixed.append(tile.id)
                return
        tile.rotateCW(1)  # restore original position before flipping
    tile.flipud()  # restore original position before returning
    return


def getTopLeftTile():
    for tile in Tile.all.values():
        if (
            tile.match[up] is None
            and tile.match[right] is not None
            and tile.match[down] is not None
            and tile.match[left] is None
        ):
            return tile.id
    exit("Could not find topleft tile")


def expandBotRight(tile, x, y):
    """
    Expands the global variable `sea` starting at the topleft most tile 
    """
    global sea
    c = tile.getContent()
    for yi in range(y, y+8):
        for xi in range(x, x+8):
            sea[yi][xi] = c[yi % 8][xi % 8]

    if tile.match[right] is not None:
        expandBotRight(Tile.all[tile.match[right]], x+len(c[0]), y)

    if (x == 0 and y < len(sea)):
        if tile.match[down] is not None:
            expandBotRight(Tile.all[tile.match[down]], x, y+len(c))

def findNessy(sea):
    """
    Ahoy! lets go on an adventure searchin' th' `sea` fer th' monsters!
     
    I shall tell ye `which we 'ave spotted` once we be back
    """
    uniqueMonsters = set()

    # regex pattern matching nessy
    monster1 = r".{18}#"
    monster2 = r"#.{4}##.{4}##.{4}###"
    monster3 = r".#(?:.{2}#){5}"

    for k in [0, 1, 1, 1]:
        srot = np.rot90(sea, k=k, axes=(1, 0))
        for s in [srot, np.flipud(srot)]:
            for line in range(len(s[:-3])):
                for i in range(len(s[line][:-19])):
                    m1 = re.findall(monster1, ''.join(s[line][i:i+20]))
                    m2 = re.findall(monster2, ''.join(s[line+1][i:i+20]))
                    m3 = re.findall(monster3, ''.join(s[line+2][i:i+20]))
                    if(m1 and m2 and m3):
                        uniqueMonsters.add((line, i))
            if len(uniqueMonsters) > 0:
                return uniqueMonsters
    return uniqueMonsters


# get tiles from input file
f = open(sys.path[0] + '/input.txt').read().split("\n\n")
for tile in f:
    Tile.fromInput(tile)

tiles = list(Tile.all.keys())
Tile.fixed.append(tiles[0])

while len(Tile.fixed) < len(Tile.all):
    for tileId in [id for id in tiles if id not in Tile.fixed]:
        checkTileMatch(Tile.all[tileId])
    print("placing tiles...")
print("Tiles placed!")

refTile = getTopLeftTile()  # this is the topleft tile
length = 12*8   # square root of the amount of tiles multiplied by the size of their content without edges
sea = np.array([[' ']*length for _ in range(length)])
expandBotRight(Tile.all[refTile], 0, 0)

uniqueMonsters = findNessy(sea)
print(f"{len(uniqueMonsters)} monsters encoutered")

hastagCount = 0
for line in sea:
    for char in line:
        if char == '#':
            hastagCount += 1

print(f"#: {hastagCount}, monster: {len(uniqueMonsters)}, roughness = {hastagCount-15*len(uniqueMonsters)}")

# CORRECT!
