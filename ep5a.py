# Coding Math Episode 5a
# Draw an arrow whose head is always following the position of the mouse
# pointer
import math
import pygame


pygame.init()

CLOCK = pygame.time.Clock()
GRAY = pygame.color.THECOLORS['gray50']
WHITE = pygame.color.THECOLORS['white']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()  # A rect with the size of the screen.
surface = pygame.Surface((50, 50), pygame.SRCALPHA)
# surface.fill((0, 50, 150))  # Fill the surface to make it visible.
# Use the local coordinate system of the surface to draw the lines.
pygame.draw.line(surface, WHITE, (0, 0), (25, 0), 1)
pygame.draw.line(surface, WHITE, (0, 0), (25, 25), 1)
pygame.draw.line(surface, WHITE, (0, 0), (0, 25), 1)
# I rotate it so that the arrow is pointing to the right (0° is right).
surface = pygame.transform.rotate(surface, -135)
rect = surface.get_rect()
angle = 0
# If you're using Python 3.6+, you can use f-strings.
print(f"Size of the screen {screen.get_size()}")
print(f"Center of the screen {screen_rect.center}")

def calculate_angle(mouse_position):
    dx = mouse_position[0] - screen_rect.centerx
    dy = mouse_position[1] - screen_rect.centery
    return math.atan2(dy, dx)

main_loop = True
while main_loop:
    for event in pygame.event.get():
        # You shouldn't use `pygame.key.get_pressed` in the event loop.
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            main_loop = False

    pos = pygame.mouse.get_pos()
    angle = math.degrees(calculate_angle(pos))
    screen.fill(GRAY)
    # Now just rotate the original surface and get a new rect.
    rotated_surface = pygame.transform.rotate(surface, -angle)
    rect = rotated_surface.get_rect(center=(screen_rect.center))
    screen.blit(rotated_surface, rect)
    pygame.display.update()
    CLOCK.tick(30)


pygame.quit()
