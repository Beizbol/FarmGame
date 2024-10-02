import pygame


class Decor:
    parts = {
        "bridge_side_left": pygame.Rect(0, 0, 16, 16),
        "bridge_side_mid": pygame.Rect(0, 32, 16, 16),
        "bridge_side_right": pygame.Rect(16, 0, 16, 16),
        "bridge_vert_top": pygame.Rect(48, 0, 16, 16),
        "bridge_vert_mid": pygame.Rect(48, 32, 16, 16),
        "bridge_vert_bot": pygame.Rect(48, 16, 16, 16),
    }

    sheets = {}

    def __init__(self, pos):
        self.pos = pos
        self.style = "bridge_side_left"
        if self.sheets == {}:
            self.sheets["bridge"] = pygame.image.load(
                "assets/decor/Bridge.png"
            ).convert_alpha()

    def draw(self, screen):
        sheet = self.sheets[self.style]
        part = self.parts[self.style]
        screen.blit(sheet, self.pos, part)
