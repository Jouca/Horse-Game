import pygame
try:
    from classes import Button1
    from constant import COLOR
except ModuleNotFoundError:
    from .classes import Button1
    from .constant import COLOR

def affichage_menu_principal(screen, var):
    """
    Affiche le menu principal.
    """
    screen.fill(COLOR["SILVER"])
    # Création du bouton "Jouer"
    bouton_jouer = Button1(screen, (0.4, 0, 0.2, 0.2), "Jouer")
    bouton_jouer.change_color(COLOR["BRONZE"])
    bouton_jouer.draw(screen)

    return var

def affichage_menu(var, screen, clock):
    """
    Permet de gérer l'affichage des menus.
    """
    if var["menuSelect"] == "principal":
        var = affichage_menu_principal(screen, var)

    pygame.display.flip()
    return var

def controles_principal(var, event):
    """
    Gestion des contrôles du menu principal.
    """
    return var

def controles(var):
    """
    Occupation de la gestion des contrôles par rapport à leur menu.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var["jeu_en_cours"] = False

        if var["menuSelect"] == "principal":
            var = controles_principal(var, event)
    return var