# Coding Math Episode 4b
# Playing here with both x and y coordinates 
import pygame
import math

pygame.init()

RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
centerx = screen_rect.width // 2
centery = screen_rect.height // 2
xradius = 200
yradius = 290 
xspeed = 0.01
yspeed = 0.05
xangle = 0
yangle = 0

print(f"Size of the screen ({screen_rect.width}, {screen_rect.height})")
print(f"Center of the screen ({centerx}, {centery})")

pygame.display.set_caption("Episode 4b")

main_loop = True
amplifier = 200

while main_loop:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
                main_loop = False

    x = round(centerx + math.cos(xangle) * xradius)
    y = round(centery + math.sin(yangle) * yradius)

    pygame.draw.circle(screen, RED, (x,y), 5)
    xangle += xspeed
    yangle += yspeed
    pygame.display.update()

pygame.quit()

