# Coding Math Episode 9b
# Add the acceleration and observe how it impacts velocity (speed + direction)
# on the fireworks
__author__ = "piquesel"

import pygame
import math
import random
from ep7 import Vector as Vector


class Particle:
    'Represents a particle defined by its position, velocity and direction'

    def __init__(self, speed, direction, x=0, y=0, gravity=0):
        'Initialize the particle'
        self.x = x
        self.y = y
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.velocity.set_length(speed)
        self.velocity.set_angle(direction)
        self.gravity = Vector(0, gravity)

    def accelerate(self, accel):
        self.velocity.add_to(accel)

    def update(self):
        self.velocity.add_to(self.gravity)
        self.position.add_to(self.velocity)


pygame.init()

NB_LINES = 100
RED = pygame.color.THECOLORS['red']
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
pygame.display.set_caption("Episode 9b")

particles = []
NUM_PARTICLES = 300
gravity = Vector(0, 0.1)

for i in range(0, NUM_PARTICLES):
    particles.append(Particle(random.random() * 5 + 2,
                              random.random() * math.pi * 2,
                              screen_rect.width/2,
                              screen_rect.height/3,
                              0.01))

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
        p.accelerate(gravity)
        p.update()
        pygame.draw.circle(screen, RED, (round(p.position.get_x()),
                                         round(p.position.get_y())), 5)
    pygame.display.update()


pygame.quit()
