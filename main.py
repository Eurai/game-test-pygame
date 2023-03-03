import pygame
from pygame.locals import *
import time

# WINDOW SIZE
width = 1280
height = 720

# VARIABLE SET
camX = 30
camY = 30
x = 0
y = 0
clock = pygame.time.Clock()
blue = (0, 0, 255)

# SCREEN SET
screen = pygame.display.set_mode((width, height))

# SET CAPTION
pygame.display.set_caption('game test')
pImg = pygame.image.load('assets/player.jpeg').convert_alpha()

run = True
while run:
    
# BACKGROUND SET
    screen.fill(blue)
    screen.blit(pImg, (0,  0))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

# PLAYER CLASS
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

if __name__ == "__main__":
    main()