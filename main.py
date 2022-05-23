import pygame
from ressources.menus import controles, affichage_menu
from ressources.inits import init_buttons, init_texts

pygame.init()
screen_size = (900, 660)

def main():
    """
    Boucle du jeu
    """
    pygame.display.set_caption("Jeu des chevaux")
    pygame.display.set_icon(pygame.image.load("./ressources/sprites/chess.png"))
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    var = {
        "jeu_en_cours": True,
        "menuSelect": "principal",
        "screen": screen,
        "button": init_buttons(screen),
        "text": init_texts(screen),
        "nbPlayers": 0,
        "nbHorses": 0,
        "win": None,
        "playerTurn": None,
        "playerList": None,
        "diceResult": 1,
        "playerblueHorses": [],
        "playerredHorses": [],
        "playergreenHorses": [],
        "playeryellowHorses": [],
        "actions": [],
        "nbHorseredfinished": 0,
        "nbHorsebluefinished": 0,
        "nbHorsegreenfinished": 0,
        "nbHorseyellowfinished": 0,
    }

    while var["jeu_en_cours"]:
        var = affichage_menu(var, screen, clock)
        var = controles(var)

        clock.tick(60)

if __name__ == "__main__":
    main()
