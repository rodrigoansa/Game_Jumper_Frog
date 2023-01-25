import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((500, 500))
ret = pygame.draw.polygon(tela, (255,55,55), ((100, 100), (100, 100), (400, 400), (200, 100), (150, 000)))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    pygame.display.update()