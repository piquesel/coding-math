import pygame
import math

pygame.init()

CLOCK = pygame.time.Clock()
RED = pygame.color.THECOLORS['red']
WHITE = pygame.color.THECOLORS['white']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
surface = pygame.Surface((50, 50), pygame.SRCALPHA)
radius = 200
centerx = 400
centery = 300
rangle = 0
speed = 0.05
# Fill the surface to make it visible
# surface.fill((0, 50, 150))
# Use the local coordinate system of the surface to draw the lines
pygame.draw.line(surface, RED, (0, 0), (15, 0), 1)
pygame.draw.line(surface, RED, (0, 0), (25, 25), 1)
pygame.draw.line(surface, RED, (0, 0), (0, 15), 1)
surface = pygame.transform.rotate(surface, -135)
rect = surface.get_rect()
angle = 0
# f-strings since Python 3.6+
print(f"Size of the screen {screen.get_size()}")
print(f"Center of the screen {screen_rect.center}")
myfont = pygame.font.SysFont("monospace", 12)

pygame.display.set_caption("Episode 5 with moving arrow")

def calculate_angle(mouse_position):
    dx = mouse_position[0] - screen_rect.centerx
    dy = mouse_position[1] - screen_rect.centery
    return math.atan2(dy,dx)


main_loop = True
while main_loop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
            main_loop = False

    pos = pygame.mouse.get_pos()
    angle = math.degrees(calculate_angle(pos))
    screen.fill(WHITE)
    # Rotate the original surface and get a new rect 
    x = round(centerx + math.cos(rangle) * radius)
    y = round(centery + math.sin(rangle) * radius)
    rotated_surface = pygame.transform.rotate(surface, -angle)
    rect = rotated_surface.get_rect(center = (x, y))
    rangle += speed
    screen.blit(rotated_surface, rect)
    pygame.display.update()
    CLOCK.tick(30)


pygame.quit()

