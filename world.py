# packages from pypi
import jsonpickle as json

from tile import Tile
from decor import Decor


class World:
    def __init__(self, w, h):
        self.paint_mode = False

        try:
            self.load()
            return
        except FileNotFoundError:
            print("Failed to load world.")

        self.width = w
        self.height = h
        self.tiles = []
        for col in range(w // Tile.size):
            column = []
            for row in range(h // Tile.size):
                column.append(Tile(col, row))
            self.tiles.append(column)

    def update_patterns(self):
        for column in self.tiles:
            for tile in column:
                if tile.tileset > 0:
                    tile.update(self.tiles)

    def bridge(self, pos):
        # get the right tile
        x, y = pos
        col = x // Tile.size
        row = y // Tile.size
        self.tiles[col][row].decor = Decor((x, y))

    def isWaterAt(self, x, y):
        # convert x and y to grid rows and columns
        col = x // Tile.size
        row = y // Tile.size
        # get the right tile
        tile = self.tiles[col][row]
        return tile.tileset == 0

    def click(self, pos):
        # get the right tile
        x, y = pos
        col = x // Tile.size
        row = y // Tile.size
        # switch our material
        self.tiles[col][row].tileset += 1
        if self.tiles[col][row].tileset == len(Tile.tilesets):
            self.tiles[col][row].tileset = 0

        # print("paint mode", self.paint_mode)
        if self.paint_mode:
            # get the material
            material = self.tiles[col][row].tileset
            # find the connected tiles
            connected_tiles = []
            for x in [col - 1, col, col + 1]:
                for y in [row - 1, row, row + 1]:
                    tile = self.tiles[x][y]
                    if tile.tileset != 0:
                        connected_tiles.append(tile)
            # print("connected", connected_tiles)
            # change their tilesets to match
            for tile in connected_tiles:
                tile.tileset = material

        self.update_patterns()

    def remove(self, pos):
        x, y = pos
        col = x // Tile.size
        row = y // Tile.size
        if self.tiles[col][row].tileset == 0:
            return
        self.tiles[col][row].tileset = 0
        if self.tiles[col][row].tileset == len(Tile.tilesets):
            self.tiles[col][row].tileset = 0
        self.update_patterns()

    def load(self):
        with open("data/world.json", "r") as file:
            text = file.read()
            if text != "":
                data = json.decode(text)
                self.height = data.height  # type: ignore
                self.width = data.width  # type: ignore
                self.tiles = data.tiles  # type: ignore
        self.tiles[0][0].load_sheets()

    def save(self):
        print("Saving World")
        with open("data/world.json", "w") as file:
            data = json.encode(self)
            if data is not None:
                file.write(data)

    def draw(self, screen):
        screen.fill("light blue")
        for column in self.tiles:
            for tile in column:
                tile.draw(screen)
