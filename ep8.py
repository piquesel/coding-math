# Coding Math Episode 8
#
__author__ = "piquesel"

import pygame
import math
import random
from ep7 import Vector as Vector


class Particle:
    'Represents a particle defined by its position, velocity and direction'

    def __init__(self, x, y, speed, direction):
        'Initialize the particle'
        self.x = x
        self.y = y
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.velocity.set_length(speed)
        self.velocity.set_angle(direction)

    def update(self):
        self.position.add_to(self.velocity)


pygame.init()

NB_LINES = 100
RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
pygame.display.set_caption("Episode 8")

particles = []
NUM_PARTICLES = 300

for i in range(0, NUM_PARTICLES):
    particles.append(Particle(screen_rect.width/2,
                              screen_rect.height/2,
                              random.random() * 4 + 1,
                              random.random() * math.pi * 2))

main_loop = True
while main_loop:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE):
                main_loop = False

    screen.fill((0, 0, 0))
    for i in range(0, NUM_PARTICLES):
        p = particles[i]
        p.update()
        pygame.draw.circle(screen, RED, (round(p.position.get_x()),
                                         round(p.position.get_y())), 5)
    pygame.display.update()


pygame.quit()
