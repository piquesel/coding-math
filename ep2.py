# Coding Math Episode 2
# Display a sine wave 
import pygame
import math
import numpy as np

pygame.init()

RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
print(f"Size of the screen ({screen_rect.width}, {screen_rect.height})")
screen_fonts = pygame.font.SysFont("monospace", 12)
label = screen_fonts.render("Press key up or down to change the period...",
                            1, (255,255,0))
pygame.display.set_caption("Episode 2")

main_loop = True
amplifier = 200
angles = np.arange(0.0, math.pi * 4, 0.01)

while main_loop:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
                main_loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            amplifier += 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            amplifier -= 5

    screen.fill((0,0,0))
    for angle in angles:
        x = angle * amplifier
        y = math.sin(angle) * amplifier
        pygame.draw.rect(screen, RED, (x, -y + screen_rect.height/2, 2, 2), 1)
    screen.blit(label, ((screen_rect.width - label.get_rect().width) // 2,
                        (screen_rect.height - 20)))
    pygame.display.update()


pygame.quit()

