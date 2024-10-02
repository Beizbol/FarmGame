import pygame


class Tile:
    size = 32
    patterns = [
        # col 1
        [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1],
        ],
        [
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 1],
        ],
        [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        # col 2
        [
            [0, 0, 0],
            [1, 1, 1],
            [1, 1, 1],
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [],
        # col 3
        [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0],
        ],
        [
            [1, 1, 0],
            [1, 1, 0],
            [1, 1, 0],
        ],
        [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
        ],
        [],
        # col 4
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ],
        [],
        # col 5
        [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 1],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 0],
        ],
        # col 6
        [
            [0, 0, 0],
            [1, 1, 1],
            [1, 1, 0],
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 0],
        ],
        [
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 1],
        ],
        [
            [1, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 0],
        ],
        # col 7
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 1],
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 1],
        ],
        [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ],
        [
            [0, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 1],
            [1, 1, 1],
            [0, 1, 1],
        ],
        # col 8
        [
            [0, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
        ],
        [
            [1, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [1, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
        ],
        # col 9
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [1, 1, 1],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        # col 10
        [
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1],
        ],
        [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 1],
        ],
        [
            [0, 1, 1],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [],
        # col 11
        [],
        [],
        [
            [0, 1, 0],
            [1, 1, 1],
            [1, 1, 0],
        ],
        [
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [],
    ]
    tilesets = [
        "Water",
        "Grass_Base",
        "Grass_Base_Dark",
        "Grass_Hill",
        "Grass_Hill_Dark",
        "Soil_Base",
        "Soil_Base_Dark",
        "Soil_Hill",
        "Soil_Hill_Dark",
        "Stone_Base",
        "Stone_Hill",
        "Bush",
        "Grass_Ramp",
        "Grass_Ramp_Dark",
    ]
    sheets = []
    water_sheet = None
    water_part = pygame.Rect(0, 0, size, size)

    def __init__(self, col, row):
        self.decor = ""
        self.col = col
        self.row = row
        self.x = col * self.size
        self.y = row * self.size
        self.tileset = 0
        self.pattern = self.patterns.index(
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ]
        )
        if self.sheets == []:
            self.load_sheets()
        print("sheets", self.sheets)

    def load_sheets(self):
        for name in self.tilesets:
            sheet = pygame.image.load(f"assets/tilesets/{name}.png").convert_alpha()
            sheet = pygame.transform.scale2x(sheet)
            self.sheets.append(sheet)
        Tile.water_sheet = self.sheets[0]
        # print(self.sheets)

    def update(self, tiles):
        # print("updating tile:", row, col)
        pattern = []
        for r in [self.row - 1, self.row, self.row + 1]:
            pr = []
            for c in [self.col - 1, self.col, self.col + 1]:
                # if we are on the edge
                if c < 0 or r < 0 or c >= len(tiles) or r >= len(tiles):
                    pr.append(0)
                else:
                    t = tiles[c][r]  # the neighbour tile
                    pr.append(min(1, t.tileset))  # 0 = water otherwise 1
            pattern.append(pr)

        # trim the pattern
        # if middle top is 0
        if pattern[1][0] == 0:
            # clear the top corners
            pattern[0][0] = 0
            pattern[2][0] = 0

        # if middle bottom is 0
        if pattern[1][2] == 0:
            # clear the bottom corners
            pattern[0][2] = 0
            pattern[2][2] = 0

        # if left middle is 0
        if pattern[0][1] == 0:
            pattern[0][0] = 0
            pattern[0][2] = 0

        # if right middle is 0
        if pattern[2][1] == 0:
            pattern[2][0] = 0
            pattern[2][2] = 0

        # set the pattern number
        try:
            self.pattern = self.patterns.index(pattern)
        except ValueError:
            print("No Match: ")
            for r in pattern:
                print(r)

    def draw(self, screen):
        sheet = self.sheets[self.tileset]
        position = (self.x, self.y)
        row = self.pattern % 5
        col = self.pattern // 5
        sheet_part = (col * self.size, row * self.size, self.size, self.size)
        screen.blit(self.water_sheet, position, self.water_part)
        screen.blit(sheet, position, sheet_part)
        # if self.decor != "":
        #     self.decor.draw(screen)
