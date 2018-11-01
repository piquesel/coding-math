# Coding Math Episode 4a
# Display shapes (circles) uniformy distributed on a circle
import pygame
import math

pygame.init()

RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
screen_width, screen_height = screen.get_size()
centerx = screen_rect.width // 2
centery = screen_rect.height // 2
radius = 200
angle = 0
numobjects = 20
slice = (math.pi * 2) / numobjects

print(f"Size of the screen ({screen_rect.width}, {screen_rect.height})")
print(f"Center of the screen ({centerx}, {centery})")
myfont = pygame.font.SysFont("monospace", 12)

pygame.display.set_caption("Episode 4a")

main_loop = True
amplifier = 200

while main_loop:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
                main_loop = False

    for i in range(0, numobjects):
        angle = i * slice
        x = round(centerx + math.cos(angle) * radius)
        y = round(centery + math.sin(angle) * radius)
        pygame.draw.circle(screen, RED, (x,y), 10)
    pygame.display.update()

pygame.quit()

