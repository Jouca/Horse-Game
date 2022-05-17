import pygame
from pygame.locals import *
try:
    from constant import COLOR
    from diego import Button
except ModuleNotFoundError:
    from .constant import COLOR
    from .diego import Button
def MenuSelection(screen, var):
    pygame.draw.rect(screen, COLOR["BLACK"], (60, 60, 790, 500), 5)
    play_button = Button(screen, (0.35, 0.68, 0.3, 0.12), (255, 255, 255))
    play_button.draw(screen)
    pygame.draw.rect(screen, COLOR["BLACK"], (100, 250, 80, 80), 4)
    pygame.draw.rect(screen, COLOR["BLACK"], (740, 250, 80, 80), 4)
    fleche_haut_1 = Button(screen, (0.11, 0.27, 0.09, 0.1), (COLOR["SILVER"]))
    fleche_haut_1.draw(screen)
    fleche_haut_2 = Button(screen, (0.82, 0.27, 0.09, 0.1), (COLOR["SILVER"]))
    fleche_haut_2.draw(screen)
    fleche_bas_1 = Button(screen, (0.11, 0.52, 0.09, 0.1), (COLOR["SILVER"]))
    fleche_bas_1.draw(screen)
    fleche_bas_2 = Button(screen, (0.82, 0.52, 0.09, 0.1), (COLOR["SILVER"]))
    fleche_bas_2.draw(screen)
    pygame.draw.polygon(screen, COLOR["BLACK"], ((100, 235), (180, 235), (140, 180)), 4)
    pygame.draw.polygon(screen, COLOR["BLACK"], ((100, 345), (180, 345), (140, 400)), 4)
    pygame.draw.polygon(screen, COLOR["BLACK"], ((740, 235), (820, 235), (780, 180)), 4)
    pygame.draw.polygon(screen, COLOR["BLACK"], ((740, 345), (820, 345), (780, 400)), 4)
    font = pygame.font.SysFont(None, 80)
    img = font.render("Jouer" , True, COLOR["BLACK"])
    screen.blit(img, (370, 465))
    font = pygame.font.SysFont(None, 40)
    img = font.render("Selectionner le nombre de joueurs" , True, COLOR["BLACK"])
    screen.blit(img, (220, 80))
    font = pygame.font.SysFont(None, 30)
    img = font.render("Nombres de joueurs" , True, COLOR["BLACK"])
    screen.blit(img, (190, 275))
    img = font.render("Nombres de pions" , True, COLOR["BLACK"])
    screen.blit(img, (535, 275))
    font = pygame.font.SysFont(None, 80)
    img = font.render(str(var["nbPlayers"]), True, COLOR["BLACK"])
    screen.blit(img, (125, 265))
    img = font.render(str(var["nbPlayers"]) , True, COLOR["BLACK"])
    screen.blit(img, (760, 265))