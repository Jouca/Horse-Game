from diego import Button
import pygame
from pygame.locals import *

BLANC = (255, 255, 255)
Noir = (0, 0, 0)

def Avancer(Pion, Plateau, ChiffreDe):
    ...

pygame.init()
screen = pygame.display.set_mode(size=(900, 660))
pygame.display.set_caption('Petit')
screen.fill(BLANC)



def MenuSelection():
    pygame.draw.rect(screen, Noir, (60, 60, 790, 500), 5)
    play_button = Button(screen, (0.35, 0.68, 0.3, 0.12), (255, 255, 255))
    play_button.draw(screen)
    pygame.draw.rect(screen, Noir, (100, 250, 80, 80), 4)
    pygame.draw.rect(screen, Noir, (740, 250, 80, 80), 4)
    fleche_haut = Button(screen, (0.11, 0.27, 0.09, 0.1), (255, 255, 255))
    fleche_haut.draw(screen)
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

MenuSelection()



pygame.display.flip()

Perdu = False
while Perdu == False:
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Continue = False
                    pygame.quit()


...