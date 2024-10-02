import pygame


class Player:
    size = 48

    def __init__(self):
        self.speed = 5
        self.run = 1
        # self.vy = 0
        self.v = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()
        self.dir = "down"
        self.action = ""
        self.frame = pygame.Rect(0, 0, self.size, self.size)
        self.sheet = pygame.image.load("assets/player/spritesheet.png").convert_alpha()
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

    def press(self, k):
        if k == "up":
            self.v.y -= self.speed
        elif k == "down":
            self.v.y += self.speed
        elif k == "left":
            self.v.x -= self.speed
        elif k == "right":
            self.v.x += self.speed
        elif k == "shift":
            self.run = 2
        elif k == "t":
            self.action = "till"
        elif k == "c":
            self.action = "chop"
        elif k == "space":
            self.action = "water"

    def release(self, k):
        if k == "up":
            self.v.y += self.speed
        elif k == "down":
            self.v.y -= self.speed
        elif k == "left":
            self.v.x += self.speed
        elif k == "right":
            self.v.x -= self.speed
        elif k == "shift":
            self.run = 1
        elif k == "t" or k == "c" or k == "space":
            self.action = ""

    def update(self, world):
        v = self.v.normalize() if self.v.magnitude() > 0 else self.v
        new_x = self.pos.x + (v.x * self.run)
        new_y = self.pos.y + (v.y * self.run)

        tile = world.getTileAt(new_x + self.size, new_y + self.size + 10)

        # if we are on land
        if tile.tileset != 0:
            self.pos.x = new_x
            self.pos.y = new_y

        if self.v.y > 0:  # down
            self.dir = "down"
        elif self.v.y < 0:  # up
            self.dir = "up"
        elif self.v.x > 0:  # right
            self.dir = "right"
        elif self.v.x < 0:  # left
            self.dir = "left"

        if self.action == "till" and tile.tileset == 4:
            tile.tileset = 5

    def animate(self):
        if self.action == "till":
            self.frame.y = self.size * 12
        elif self.action == "chop":
            self.frame.y = self.size * 16
        elif self.action == "water":
            self.frame.y = self.size * 20
        elif self.v.x == 0 and self.v.y == 0:
            self.frame.y = 0
        elif self.run > 1:
            self.frame.y = self.size * 8
        else:
            self.frame.y = self.size * 4

        if self.dir == "down":
            self.frame.y += self.size * 0
        elif self.dir == "up":
            self.frame.y += self.size * 1
        elif self.dir == "right":
            self.frame.y += self.size * 2
        elif self.dir == "left":
            self.frame.y += self.size * 3

        self.frame.x += self.size
        if self.frame.x >= self.sheet.get_width():
            self.frame.x = 0

    def draw(self, screen):
        # pygame.draw.rect(screen, "blue", self.frame)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.sheet, (0, 0), self.frame)
        surface = pygame.transform.scale_by(self.surface, 2)
        screen.blit(surface, self.pos)
