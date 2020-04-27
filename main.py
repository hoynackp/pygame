import pygame
import os
import PIL
pygame.init()

width, height = 800, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame')

bg = pygame.image.load(os.path.join('images', 'bg.jpg')).convert()
bgX1 = 0
bgX2 = 450

clock = pygame.time.Clock()

fps = 30
run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()