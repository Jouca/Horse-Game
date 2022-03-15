import pygame

def affichage_menu_principal(screen, var):
    """
    Affiche le menu principal.
    """
    screen.fill((255, 255, 255))

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