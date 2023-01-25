import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

largura = 600
altura = 520
pos_car_1 = 250

pos_sap_x = 280
pos_sap_y = 480
sapo_rot = 0

#Importando imagens
pista = pygame.image.load('imagens/road.png')
rio = pygame.image.load('imagens/rio.png')
car_1 = pygame.image.load('imagens/car_1.png')
car_1_rect = car_1.get_rect()
sapo = pygame.image.load('imagens/sapo.png')
sapo_rect = sapo.get_rect()
# sapo_angulo = pygame.transform.rotate(sapo, sapo_rot)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jumper Frog')


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                pos_sap_x = pos_sap_x - 70  
                pygame.transform.rotate(sapo, -90)             
                pos_sap_x = pos_sap_x - 70
                sapo_angulo = pygame.transform.rotate(sapo, 90)                         
            if event.key == K_RIGHT:
                pos_sap_x = pos_sap_x + 70
                sapo_angulo = pygame.transform.rotate(sapo, -90)
            if event.key == K_UP:
                pos_sap_y = pos_sap_y - 70
                sapo_angulo = pygame.transform.rotate(sapo, 0)
            if event.key == K_DOWN:
                pos_sap_y = pos_sap_y + 70
                sapo_angulo = pygame.transform.rotate(sapo, -180)
    
    tela.blit(pista, (0,260))
    tela.blit(pista, (0,475))
    tela.blit(rio, (0,40))
    tela.blit(pista, (0,-180))


    if sapo_rect.colliderect(car_1_rect):
        print('Errou')  
    

    
    tela.blit(car_1, (pos_car_1, 265))   

    
    sapo_pula = tela.blit(sapo, (pos_sap_x,pos_sap_y))

    

    
    
    
    pygame.display.update()