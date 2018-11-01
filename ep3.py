# Coding Math Episode 3
# Boucing ball 
__author__ = "piquesel"

import pygame
import math
import numpy as np

pygame.init()

RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
centerx = screen_rect.width // 2
centery = screen_rect.height // 2 
offset = screen_rect.height * 0.4
speed = 0.01
angle = 0
print(f"Size of the screen ({screen_rect.width}, {screen_rect.height})")
print(f"Center of the screen ({centerx}, {centery})")
screen_fonts = pygame.font.SysFont("monospace", 12)
label = screen_fonts.render("Press key up or down to change the speed...",
                            1, (255,255,0))
pygame.display.set_caption("Episode 3")

main_loop = True
amplifier = 200

while main_loop:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
                main_loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            speed += 0.01
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            speed -= 0.01

    y = round(centery + math.sin(angle) * offset)
    screen.fill((0,0,0))
    pygame.draw.circle(screen, RED, (centerx,y), 15)
    angle += speed;
    screen.blit(label, ((screen_rect.width - label.get_rect().width) // 2,
                        (screen_rect.height - 20)))
    pygame.display.update()


pygame.quit()

