import pygame
import os
pygame.init()

width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame')

clock = pygame.time.Clock()

fps = 30
run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()