import pygame
import os
pygame.init()

width, height = 800, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame')

bg = pygame.image.load(os.path.join('images', 'bg.jpg')).convert()
bgX1 = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

def updateScreen():
    screen.blit(bg, (bgX1,0))
    screen.blit(bg, (bgX2,0))
    pygame.display.update()

fps = 30
run = True
while run:
    updateScreen()
    clock.tick(fps)
    bgX1 -= 2
    bgX2 -= 2
    if bgX1 < bg.get_width() * -1:
        bgX1 = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()