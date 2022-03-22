try:
    from diego import Button1
except ModuleNotFoundError:
    from .diego import Button1

def init_buttons(screen):
    buttons = {
        "jouer": Button1(screen, (0.4, 0.5, 0.2, 0.2), "Jouer")
    }
    return buttons