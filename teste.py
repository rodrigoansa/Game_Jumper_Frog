import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

largura = 600
altura = 520
pos_lazer_x = 300
pos_lazer_y = 1


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jumper Frog')

lazer = pygame.draw.rect(tela, (255,0,0), (20, 10, 10, 10))


while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    
    
    
    
    

    pygame.draw.rect(tela, (255,255,0), (pos_lazer_x, pos_lazer_y, 3, 20))
    if pos_lazer_y >= altura:
       pos_lazer_y = 10
    pos_lazer_y = pos_lazer_y + 1

    

    

    
    
    
    pygame.display.update()