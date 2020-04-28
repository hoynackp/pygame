import pygame
import os
pygame.init()

width, height = 800, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame')

bg = pygame.image.load(os.path.join('images', 'bg.jpg')).convert()
bgX1 = 0
bgX2 = bg.get_width()

class Ninja:
    running = [pygame.image.load(os.path.join('images', str(x) + '.png')).convert() for x in range(10)]
    jumping = [pygame.image.load(os.path.join('images', str(x) + '.png')).convert() for x in range(10,20)]
    sliding = [pygame.image.load(os.path.join('images', str(x) + '.png')).convert() for x in range(20,30)]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.sliding2 = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def draw(self, screen):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            screen.blit(self.jumping[self.jumpCount//12]), (self.x, self.y)
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping
        elif self.sliding:
        else:

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