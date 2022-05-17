try:
    from diego import Button1, Text
except ModuleNotFoundError:
    from .diego import Button1, Text

def init_buttons(screen):
    buttons = {
        "jouer": Button1(screen, (0.4, 0.55, 0.2, 0.2), "Jouer"),
        "dice": Button1(screen, (0.75, 0.7, 0.22, 0.15), "Lancer les dés")
    }
    return buttons


def init_texts(screen):
    texts = {
        "select_gamemode": Text(screen, (0.1, 0.2, 0.15, 0.15), "Sélectionner votre mode de jeu", 50)
    }
    return texts