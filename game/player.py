import pygame


class Player:
    size = 48

    def __init__(self):
        self.speed = 3
        self.vx = 0
        self.vy = 0
        self.x = 210
        self.y = 120
        self.frame = pygame.Rect(0, 0, self.size, self.size)
        self.sheet = pygame.image.load("assets/player/spritesheet.png").convert_alpha()
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

    def press(self, dir):
        if dir == "up":
            self.vy -= self.speed
        elif dir == "down":
            self.vy += self.speed
        elif dir == "left":
            self.vx -= self.speed
        elif dir == "right":
            self.vx += self.speed

    def release(self, dir):
        if dir == "up":
            self.vy += self.speed
        elif dir == "down":
            self.vy -= self.speed
        elif dir == "left":
            self.vx += self.speed
        elif dir == "right":
            self.vx -= self.speed

    def move(self, world):
        new_x = self.x + self.vx
        new_y = self.y + self.vy

        # update our location by our speed
        if not world.isWaterAt(new_x, new_y):
            self.x = new_x
            self.y = new_y

        # animate
        if self.vx == 0 and self.vy == 0:
            self.frame.y = 0  # idle part of the sheet
        else:
            self.frame.y = self.size * 4  # walk part of the sheet

        if self.vy > 0:  # down
            self.frame.y += self.size * 0  # idle part of the sheet
        elif self.vy < 0:  # updd
            self.frame.y += self.size * 1  # idle part of the sheet
        elif self.vx > 0:  # right
            self.frame.y += self.size * 2  # idle part of the sheet
        elif self.vx < 0:  # lefd
            self.frame.y += self.size * 3  # idle part of the sheet

        self.frame.x += self.size
        if self.frame.x >= self.sheet.get_width():
            self.frame.x = 0

    def draw(self, screen):
        # pygame.draw.rect(screen, "blue", self.frame)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.sheet, (0, 0), self.frame)

        surface = pygame.transform.scale_by(self.surface, 2)

        screen.blit(surface, (self.x, self.y))
