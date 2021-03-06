try:
    from diego import Button1, Text
except ModuleNotFoundError:
    from .diego import Button1, Text


def init_buttons(screen):
    """
    Initialise les boutons.
    """
    buttons = {
        "jouer": Button1(screen, (0.4, 0.55, 0.2, 0.2), "Jouer"),
        "dice": Button1(screen, (0.75, 0.8, 0.22, 0.15), "Lancer le dé"),
        "up_player": Button1(screen, (0.11, 0.27, 0.1, 0.1), ""),
        "down_player": Button1(screen, (0.11, 0.52, 0.1, 0.1), ""),
        "up_horse": Button1(screen, (0.82, 0.27, 0.1, 0.1), ""),
        "down_horse": Button1(screen, (0.82, 0.52, 0.1, 0.1), ""),
        "1": Button1(screen, (0.73, 0.8, 0.06, 0.1), "1"),
        "2": Button1(screen, (0.8, 0.8, 0.06, 0.1), "2"),
        "3": Button1(screen, (0.87, 0.8, 0.06, 0.1), "3"),
        "4": Button1(screen, (0.94, 0.8, 0.06, 0.1), "4"),
        "rejouer": Button1(screen, (0.13, 0.52, 0.15, 0.15), "Rejouer"),
        "menu": Button1(screen, (0.42, 0.52, 0.15, 0.15), "Menu")
    }
    return buttons


def init_texts(screen):
    """
    Initialise les textes.
    """
    texts = {
        "select_gamemode": Text(
            screen, (0.11, 0.14, 0.15, 0.15), "Sélectionner votre mode de jeu", 50
        )
    }
    return texts
