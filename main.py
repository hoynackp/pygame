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
    run_sprites = [pygame.image.load(os.path.join('images', str(x) + '.png')).convert_alpha() for x in range(10)]
    jump_sprites = [pygame.image.load(os.path.join('images', str(x) + '.png')).convert_alpha() for x in range(10,20)]
    slide_sprites = [pygame.image.load(os.path.join('images', str(x) + '.png')).convert_alpha() for x in range(20,30)]
    one = [1]*6
    two = [2]*12
    three = [3]*12
    four = [4]*12
    zero = [0]*25
    negone = [-1]*6
    negtwo = [-2]*12
    negthree = [-3]*12
    negfour = [-4]*12
    jumpList = (one+two+three+four+zero+negone+negtwo+negthree+negfour)
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
    def draw(self, screen):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            screen.blit(self.jump_sprites[round(self.jumpCount//11)], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding:
            if self.slideCount < 50:
                self.y += 1
            elif self.slideCount > 108:
                self.y -= 49
                self.sliding = False
                self.slideCount = 0
                self.runCount = 0
            screen.blit(self.slide_sprites[round(self.slideCount//11)], (self.x,self.y))
            self.slideCount += 1
        else:
            if self.runCount > 32:
                self.runCount = 0
            screen.blit(self.run_sprites[round(self.runCount//3.3)], (self.x,self.y))
            self.runCount += 1

clock = pygame.time.Clock()

def updateScreen():
    screen.blit(bg, (bgX1,0))
    screen.blit(bg, (bgX2,0))
    player.draw(screen)
    pygame.display.update()

player = Ninja(200, 40, 10, 10)

fps = 45
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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(player.jumping):
            player.jumping = True
    if keys[pygame.K_DOWN]:
        if not(player.sliding):
            player.sliding = True
pygame.quit()