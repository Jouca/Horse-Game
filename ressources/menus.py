from tkinter import Variable
import pygame
try:
    from diego import apply_color, load_PIL_image, convert_PIL_to_pygame
    from paul import show_table
    from constant import COLOR
except ModuleNotFoundError:
    from .diego import apply_color, load_PIL_image, convert_PIL_to_pygame
    from .paul import show_table
    from .constant import COLOR

def affichage_menu_principal(screen, var):
    """
    Affiche le menu principal.
    """
    screen.fill(COLOR["SILVER"])
    # Création du bouton "Jouer"
    """
    image1 = apply_color(load_PIL_image("ressources/sprites/chess.png"), COLOR["RED"])
    image2 = apply_color(load_PIL_image("ressources/sprites/chess.png"), COLOR["YELLOW"])
    image3 = apply_color(load_PIL_image("ressources/sprites/chess.png"), COLOR["BLUE"])
    image4 = apply_color(load_PIL_image("ressources/sprites/chess.png"), COLOR["GREEN"])
    screen.blit(convert_PIL_to_pygame(image3), (20, 20))
    """
    var["button"]["jouer"].change_color(COLOR["BLUE_PAUL"])
    var["button"]["jouer"].draw(screen)

    return var

def affichage_menu_jeu(screen, var):
    """
    Affiche le menu du jeu (Paul)
    """
    screen.fill(COLOR["SILVER"])
    plateau = show_table(screen)
    screen.blit(plateau, (0, 0))
    pygame.display.flip()
    return var


def affichage_menu_select_gamemode(var, screen):
    """
    Affiche le menu de sélection du mode de jeu.
    """
    screen.fill(COLOR["SILVER"])
    # Création du bouton "Jouer"
    var["text"]["select_gamemode"].draw(screen)
    var["button"]["jouer"].change_color(COLOR["YELLOW"])
    var["button"]["jouer"].draw(screen)
    return var

def affichage_menu(var, screen, clock):
    """
    Permet de gérer l'affichage des menus.
    """
    if var["menuSelect"] == "principal":
        var = affichage_menu_principal(screen, var)
    elif var["menuSelect"] == "select_gamemode":
        var = affichage_menu_select_gamemode(var, screen)
    elif var["menuSelect"] == "jeu":
        var = affichage_menu_jeu(screen, var)

    pygame.display.flip()
    return var

def controles_principal(var, event):
    """
    Gestion des contrôles du menu principal.
    """
    if var["button"]["jouer"].is_pressed(event):
        var["menuSelect"] = "jeu"
    return var

def controles_select_gamemode(var, event):
    """
    Gestion des contrôles du menu de sélection du mode de jeu.
    """
    if var["button"]["jouer"].is_pressed(event):
        var["menuSelect"] = "principal"
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
        elif var["menuSelect"] == "select_gamemode":
            var = controles_select_gamemode(var, event)
    return var