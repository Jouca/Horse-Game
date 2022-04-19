import pygame
from pygame.locals import *

BLANC = (255, 255, 255)
Noir = (0, 0, 0)

def MenuSelection():
    pygame.draw.rect(screen, Noir, (60, 60, 790, 500), 5)
    pygame.draw.rect(screen, Noir, (320, 450, 280, 80), 5)
    pygame.draw.rect(screen, Noir, (100, 250, 80, 80), 4)
    pygame.draw.rect(screen, Noir, (740, 250, 80, 80), 4)
    pygame.draw.polygon(screen, Noir, ((100, 235), (180, 235), (140, 180)), 4)
    pygame.draw.polygon(screen, Noir, ((100, 345), (180, 345), (140, 400)), 4)
    pygame.draw.polygon(screen, Noir, ((740, 235), (820, 235), (780, 180)), 4)
    pygame.draw.polygon(screen, Noir, ((740, 345), (820, 345), (780, 400)), 4)
    font = pygame.font.SysFont(None, 80)
    img = font.render("Jouer" , True, Noir)
    screen.blit(img, (370, 465))
    font = pygame.font.SysFont(None, 40)
    img = font.render("Selectionner le nombre de joueurs" , True, Noir)
    screen.blit(img, (220, 80))
    font = pygame.font.SysFont(None, 30)
    img = font.render("Nombres de joueurs" , True, Noir)
    screen.blit(img, (190, 275))
    img = font.render("Nombres de joueurs" , True, Noir)
    screen.blit(img, (535, 275))
    pygame.display.flip()

