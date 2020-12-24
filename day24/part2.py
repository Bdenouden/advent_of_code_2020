import sys
import re


class Tile:
    all = {}
    dir = {
        'ne':   {'dx': 2,   'dy': 3},
        'e':    {'dx': 4,   'dy': 0},
        'se':   {'dx': 2,   'dy': -3},
        'sw':   {'dx': -2,  'dy': -3},
        'w':    {'dx': -4,  'dy': 0},
        'nw':   {'dx': -2,  'dy': 3},
    }

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
    
    def getSvg(self):
        return f"<polygon stroke='gray' fill='{self.color}' style='stroke-width:.2' points='{self.x},{self.y + 2} {self.x+2},{self.y+1} {self.x+2},{self.y-1} {self.x},{self.y-2} {self.x-2},{self.y-1} {self.x-2},{self.y+1}'></polygon>"

    
    def getBlackNeigbors(self):
        bTiles = 0
        for d in Tile.dir.values():
            nbPosX = self.x+d['dx']
            nbPosY = self.y+d['dy']
            nb = Tile.all.get((nbPosX, nbPosY ))
            if nb and nb.color == 'black':
                    bTiles += 1
            elif not nb:
                Tile(nbPosX, nbPosY) # create new neighbor in case none exists
        return bTiles

    @classmethod
    def createNeighbors(cls):
        for x,y in Tile.all.copy():
            for d in Tile.dir.values():
                nbx = x+d['dx']
                nby =  y+d['dy']
                if (nbx, nby) not in Tile.all:
                    cls(nbx, nby)

def flipTiles(n):
    for i in range(n):
        tilesToToggle = []
        for tile in Tile.all.copy().values(): # cycle through copy since new neighbors will be added each loop
            bTiles = tile.getBlackNeigbors() # count black neigbors and create new tiles if no neighbor exists
            if tile.color == 'black':
                # flip if 0 or >2 black neighbors
                if bTiles == 0 or bTiles > 2:
                    tilesToToggle.append(tile)
            else:  # white tile
                # flip if exactly 2 neigbouring tiles are black
                if(bTiles == 2):
                    tilesToToggle.append(tile)

        # toggle tile colors
        for tile in tilesToToggle:
            tile.toggleColor()


def makeHtml():
    with open(sys.path[0] + '/index.html', "w") as html:
        html.write(
        '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>day24</title>
        </head>
        <body style='text-align:center'>
        <svg viewBox="-250 -250 500 500" xmlns="http://www.w3.org/2000/svg" style='height:100vh'>''')
        for tile in Tile.all.values():
            html.write(tile.getSvg()+"\n")
        html.write('</svg>\n</body>\n</html>')

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        directions = re.findall(r"nw|sw|se|ne|w|e", line.strip())
        x, y = 0, 0
        for d in directions:
            x += Tile.dir[d]['dx']
            y += Tile.dir[d]['dy']

        tile = Tile.all.get((x, y))
        if not tile:
            tile = Tile(x, y)
        tile.toggleColor()

Tile.createNeighbors()

flipTiles(100)

makeHtml()




# count results
bTiles = 0
for tile in Tile.all.values():
    if tile.color == 'black':
        bTiles += 1

makeHtml()
print(f"Black tiles:  {bTiles}")
