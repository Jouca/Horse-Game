from tkinter import Variable
import pygame

try:
    from diego import apply_color, load_PIL_image, convert_PIL_to_pygame, select_first_player, draw_horses, init_horses, handling_horses, horse_moving, update_horses
    from diego import players_list
    from paul import show_table
    from antoine import de
    from noa import MenuSelection
    from constant import COLOR
except ModuleNotFoundError:
    from .diego import apply_color, load_PIL_image, convert_PIL_to_pygame, select_first_player, draw_horses, init_horses, handling_horses, horse_moving, update_horses
    from .diego import players_list
    from .paul import show_table, player_turn
    from .antoine import de
    from .noa import MenuSelection
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
    Affiche le menu du jeu.
    """
    screen.fill(COLOR["SILVER"])
    plateau = show_table()
    draw_horses(plateau, var)
    screen.blit(plateau, (0, 0))
    var["button"]["dice"].change_color(COLOR[var["playerTurn"].upper()])
    var["button"]["dice"].draw(screen)
    dice = convert_PIL_to_pygame(load_PIL_image(f"ressources/sprites/face{var['diceResult']}.png"))
    screen.blit(pygame.transform.scale(dice, (80, 80)), (730, 430))
    return var


def affichage_menu_action(screen, var):
    """
    Affiche le menu des actions.
    """
    screen.fill(COLOR["SILVER"])
    plateau = show_table()
    draw_horses(plateau, var)
    for action in var["actions"]:
        action[1].draw_id(plateau)
    screen.blit(plateau, (0, 0))
    dice = convert_PIL_to_pygame(load_PIL_image(f"ressources/sprites/face{var['diceResult']}.png"))
    screen.blit(pygame.transform.scale(dice, (80, 80)), (730, 430))
    font = pygame.font.SysFont("Arial", 23)
    text = font.render("Sélectionner le pion avec les", True, COLOR["BLACK"])
    text2 = font.render("boutons ci-dessous", True, COLOR["BLACK"])
    screen.blit(text, (665, 370))
    screen.blit(text2, (700, 390))
    for action in var["actions"]:
        var["button"][str(action[1].get_id())].draw(screen)
    return var


def affichage_menu_select_gamemode(var, screen):
    """
    Affiche le menu de sélection du mode de jeu.
    """
    screen.fill(COLOR["SILVER"])
    # Création du bouton "Jouer"
    MenuSelection(screen, var)
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
    elif var["menuSelect"] == "action":
        var = affichage_menu_action(screen, var)

    pygame.display.flip()
    return var

def controles_principal(var, event):
    """
    Gestion des contrôles du menu principal.
    """
    if var["button"]["jouer"].is_pressed(event):
        var["menuSelect"] = "select_gamemode"
        var["nbPlayers"] = 4
        var["nbHorses"] = 4
    return var

def controles_select_gamemode(var, event):
    """
    Gestion des contrôles du menu de sélection du mode de jeu.
    """
    if var["button"]["jouer"].is_pressed(event):
        var["menuSelect"] = "jeu"
        var["playerList"] = players_list(var["nbPlayers"])
        var["playerTurn"], var["nbrTurn"] = select_first_player(var["playerList"])
        var = init_horses(var)
    elif var["button"]["up_player"].is_pressed(event):
        if var["nbPlayers"] < 4:
            var["nbPlayers"] += 1
    elif var["button"]["down_player"].is_pressed(event):
        if var["nbPlayers"] > 2:
            var["nbPlayers"] -= 1
    elif var["button"]["up_horse"].is_pressed(event):
        if var["nbHorses"] < 4:
            var["nbHorses"] += 1
    elif var["button"]["down_horse"].is_pressed(event):
        if var["nbHorses"] > 1:
            var["nbHorses"] -= 1
    return var

def controles_jeu(var, event):
    """
    Gestion des contrôles du jeu.
    """
    if var["button"]["dice"].is_pressed(event):
        var["diceResult"] = de()
        handling_horses(var, var["playerTurn"])
    return var

def controles_action(var, event):
    """
    Gestion des contrôles du menu d'action.
    """
    for action in range(len(var["actions"])):
        if var["button"][str(var["actions"][action][1].get_id())].is_pressed(event):
            var = horse_moving(var, action)
            var = update_horses(var)
            var["actions"] = []
            var["playerTurn"], var["nbrTurn"] = player_turn(var)
            var["menuSelect"] = "jeu"
            break
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
        elif var["menuSelect"] == "jeu":
            var = controles_jeu(var, event)
        elif var["menuSelect"] == "action":
            var = controles_action(var, event)
    return var