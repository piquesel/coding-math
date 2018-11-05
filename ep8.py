# Coding Math Episode 8
# 
__author__ = "piquesel"

import pygame
import random
import math
from ep7 import Vector as Vector

pygame.init()

NB_LINES = 100
RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
pygame.display.set_caption("Episode 8")

position = Vector(100, 100)
velocity = Vector()
velocity.set_length(3)
velocity.set_angle(math.pi / 6)

main_loop = True
while main_loop:
    pygame.time.delay(10)

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
    pygame.draw.circle(screen, RED, (round(position.get_x()),
                                     round(position.get_y())), 15)
    position.add_to(velocity)
    # screen.blit(label, ((screen_rect.width - label.get_rect().width) // 2,
    #                     (screen_rect.height - 20)))
    pygame.display.update()

pygame.quit()

