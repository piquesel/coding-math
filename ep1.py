# Coding Math Episode 1
# Display Random lines on the screen 
__author__ = "piquesel"

import pygame
import random

pygame.init()

NB_LINES = 100
RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
print(f"Size of the screen ({screen_rect.width}, {screen_rect.height}")
screen_fonts = pygame.font.SysFont("monospace", 12)
label = screen_fonts.render("Press space to change...", 1, (255,255,0))
pygame.display.set_caption("Episode 1")

def random_points():
    points = list()

    for i in range(1, NB_LINES):
        x = round(screen_rect.width * random.random())
        y = round(screen_rect.height * random.random())
        points.append((x, y))

    return points


main_loop = True
begin_points = random_points()
end_points = random_points()
while main_loop:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
                main_loop = False
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE):
            begin_points = random_points()
            end_points = random_points()

    screen.fill((0,0,0))
    for i in range(0, NB_LINES-1):
        pygame.draw.line(screen, RED,
                         [begin_points[i][0], begin_points[i][1]],
                         [end_points[i][0], end_points[i][1]], 1)
    screen.blit(label, ((screen_rect.width - label.get_rect().width) // 2,
                        (screen_rect.height - 20)))
    pygame.display.update()

pygame.quit()

