import pygame


class Player:
    size = 48

    def __init__(self):
        self.speed = 1
        # self.vx = 0
        # self.vy = 0
        self.v = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()
        self.dir = "down"
        self.state = "idle"
        self.frame = pygame.Rect(0, 0, self.size, self.size)
        self.sheet = pygame.image.load("assets/player/spritesheet.png").convert_alpha()
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

    def press(self, dir):
        if dir == "up":
            self.v.y -= self.speed
        elif dir == "down":
            self.v.y += self.speed
        elif dir == "left":
            self.v.x -= self.speed
        elif dir == "right":
            self.v.x += self.speed

    def release(self, dir):
        if dir == "up":
            self.v.y += self.speed
        elif dir == "down":
            self.v.y -= self.speed
        elif dir == "left":
            self.v.x += self.speed
        elif dir == "right":
            self.v.x -= self.speed

    def move(self, world):
        new_x = self.pos.x + self.v.x
        new_y = self.pos.y + self.v.y

        # update our location by our speed
        if not world.isWaterAt(new_x + self.size, new_y + self.size + 10):
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

    def animate(self):
        if self.v.x == 0 and self.v.y == 0:
            self.frame.y = 0  # idle part of the sheet
        else:
            self.frame.y = self.size * 4  # walk part of the sheet

        if self.dir == "down":
            self.frame.y += self.size * 0  # idle part of the sheet
        elif self.dir == "up":
            self.frame.y += self.size * 1  # idle part of the sheet
        elif self.dir == "right":
            self.frame.y += self.size * 2  # idle part of the sheet
        elif self.dir == "left":
            self.frame.y += self.size * 3  # idle part of the sheet

        self.frame.x += self.size
        if self.frame.x >= self.sheet.get_width():
            self.frame.x = 0

    def draw(self, screen):
        # pygame.draw.rect(screen, "blue", self.frame)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.sheet, (0, 0), self.frame)
        surface = pygame.transform.scale_by(self.surface, 2)
        screen.blit(surface, self.pos)
