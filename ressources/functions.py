try:
    from constant import FONT_HEIGHT
except ModuleNotFoundError:
    from .constant import FONT_HEIGHT

def get_font_size(font_height):
    """récupère une valeur de taille de police selon `font_height` un entier
    naturel représentant la hauteur de font voulu en nombre de pixel sur la
    fenêtre de jeu."""
    if font_height < 19:
        return 12
    else:
        i = 0
        try:
            while font_height > FONT_HEIGHT[i]:
                i += 1
        except IndexError:
            pass
        return i + 12