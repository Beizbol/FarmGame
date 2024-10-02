import pygame

from player import Player
from world import World


def run():
    pygame.init()

    width = 640
    height = 640
    fps = 60
    rate = 15
    frame = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Farming Game!")

    player = Player()
    world = World(width, height)

    while True:
        # get all our events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click")
                # pygame, can you please give me the mouse pos?
                mouse_pos = pygame.mouse.get_pos()
                world.click(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    print("Deleting terrain")
                    mouse_pos = pygame.mouse.get_pos()
                    world.remove(mouse_pos)
                elif event.key == pygame.K_b:
                    print("bridge")
                    mouse_pos = pygame.mouse.get_pos()
                    world.bridge(mouse_pos)
                elif event.key == pygame.K_f:
                    print("Saving the map...")
                    world.save()
                elif event.key == pygame.K_w:
                    player.press("up")
                elif event.key == pygame.K_s:
                    player.press("down")
                elif event.key == pygame.K_a:
                    player.press("left")
                elif event.key == pygame.K_d:
                    player.press("right")
                elif event.key == pygame.K_t:
                    player.press("t")
                elif event.key == pygame.K_c:
                    player.press("c")
                elif event.key == pygame.K_SPACE:
                    player.press("space")
                elif event.key == pygame.K_LSHIFT:
                    player.press("shift")
                    world.paint_mode = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.release("up")
                elif event.key == pygame.K_s:
                    player.release("down")
                elif event.key == pygame.K_a:
                    player.release("left")
                elif event.key == pygame.K_d:
                    player.release("right")
                elif event.key == pygame.K_t:
                    player.release("t")
                elif event.key == pygame.K_c:
                    player.release("c")
                elif event.key == pygame.K_SPACE:
                    player.release("space")
                elif event.key == pygame.K_LSHIFT:
                    player.release("shift")
                    world.paint_mode = False

        player.update(world)
        # animate the player at 15fps
        if frame > fps // rate:
            player.animate()
            frame = 0

        # draw the world
        world.draw(screen)
        player.draw(screen)

        # show everything we drew
        pygame.display.update()
        clock.tick(fps)
        frame += 1


if __name__ == "__main__":
    # sushi emoji (U+1F363)
    print("\U0001f363")
    run()
