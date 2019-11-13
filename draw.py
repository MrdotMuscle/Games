import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
FUCHSIA = (255, 0, 255)
MAROON = (128, 0, 0)
TEAL = (0, 128, 128)
OLIVE = (128, 128, 0)

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, MAROON, ((146, 0), (291, 106), (236, 277)
,(56, 277), (0, 106)))
pixobj = pygame.PixelArray(DISPLAYSURF)

pixobj[480][380] = BLACK
pixobj[482][382] = BLACK
pixobj[484][384] = BLACK
pixobj[486][386] = BLACK
pixobj[488][388] = BLACK
del pixobj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
