from ast import Mod
import pygame
from ressources.menus import controles, affichage_menu

screen_size = (960, 720)
pygame.init()

def main():
    """
    Boucle du jeu
    """
    pygame.display.set_caption("Pygame")
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    var = {
        "jeu_en_cours": True,
        "menuSelect": "principal",
    }

    while var["jeu_en_cours"]:
        var = affichage_menu(var, screen, clock)
        var = controles(var)

        clock.tick(60)

if __name__ == "__main__":
    main()