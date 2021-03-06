import pygame
try:
    from diego import load_PIL_image, convert_PIL_to_pygame, select_first_player, draw_horses
    from diego import players_list, init_horses, handling_horses, horse_moving, update_horses
    from diego import check_win, reset_var
    from paul import show_table
    from antoine import de
    from noa import MenuSelection
    from constant import COLOR
except ModuleNotFoundError:
    from .diego import load_PIL_image, convert_PIL_to_pygame, select_first_player, draw_horses
    from .diego import players_list, init_horses, handling_horses, horse_moving, update_horses
    from .diego import check_win, reset_var
    from .paul import show_table, player_turn
    from .antoine import de
    from .noa import MenuSelection
    from .constant import COLOR


def affichage_menu_principal(screen, var):
    """
    Affiche le menu principal.
    """
    screen.fill(COLOR["SILVER"])
    var["button"]["jouer"].change_color(COLOR["BLUE_PAUL"])
    var["button"]["jouer"].draw(screen)
    logo = pygame.image.load("./ressources/sprites/logo.png")
    screen.blit(pygame.transform.scale(logo, (300, 300)), (300, 40))

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
    score_font = pygame.font.SysFont("Arial", 40)
    text = score_font.render("Score :", True, COLOR["BLACK"])
    screen.blit(text, (725, 30))
    for player_id in range(len(var["playerList"])):
        player = var["playerList"][player_id]
        score = score_font.render(
            f"{player} : " + str(var[f"nbHorse{player}finished"]), True, COLOR[player.upper()]
        )
        screen.blit(score, (710, 100 + 50 * player_id))
    return var


def affichage_menu_win(screen, var):
    """
    Affiche le menu de fin de partie.
    """
    screen.fill(COLOR["SILVER"])
    plateau = show_table()
    draw_horses(plateau, var)
    screen.blit(plateau, (0, 0))
    score_font = pygame.font.SysFont("Arial", 40)
    text = score_font.render("Score :", True, COLOR["BLACK"])
    screen.blit(text, (725, 30))
    for player_id in range(len(var["playerList"])):
        player = var["playerList"][player_id]
        score = score_font.render(
            f"{player} : " + str(var[f"nbHorse{player}finished"]), True, COLOR[player.upper()]
        )
        screen.blit(score, (710, 100 + 50 * player_id))
    pygame.draw.rect(screen, COLOR["BLACK"], (95, 165, 460, 310))
    rect = pygame.Rect(100, 170, 450, 300)
    pygame.draw.rect(screen, COLOR[var["win"].upper()], (100, 170, 450, 300))
    win_font = pygame.font.SysFont("Arial", 40, bold=True)
    win_text = win_font.render(f"{var['win']} a gagn?? !", True, COLOR["BLACK"])
    win_rect = win_text.get_rect(center=rect.center)
    screen.blit(win_text, (win_rect[0], win_rect[1] - 80))
    var["button"]["rejouer"].draw(screen)
    var["button"]["menu"].draw(screen)
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
    text = font.render("S??lectionner le pion avec les", True, COLOR["BLACK"])
    text2 = font.render("boutons ci-dessous", True, COLOR["BLACK"])
    screen.blit(text, (665, 370))
    screen.blit(text2, (700, 390))
    for action in var["actions"]:
        var["button"][str(action[1].get_id())].draw(screen)
    score_font = pygame.font.SysFont("Arial", 40)
    text = score_font.render("Score :", True, COLOR["BLACK"])
    screen.blit(text, (725, 30))
    for player_id in range(len(var["playerList"])):
        player = var["playerList"][player_id]
        score = score_font.render(
            f"{player} : " + str(var[f"nbHorse{player}finished"]), True, COLOR[player.upper()]
        )
        screen.blit(score, (710, 100 + 50 * player_id))
    return var


def affichage_menu_select_gamemode(var, screen):
    """
    Affiche le menu de s??lection du mode de jeu.
    """
    screen.fill(COLOR["SILVER"])
    MenuSelection(screen, var)
    var["text"]["select_gamemode"].draw(screen)
    var["button"]["jouer"].change_color(COLOR["YELLOW"])
    var["button"]["jouer"].draw(screen)
    return var


def affichage_menu(var, screen, clock):
    """
    Permet de g??rer l'affichage des menus.
    """
    if var["menuSelect"] == "principal":
        var = affichage_menu_principal(screen, var)
    elif var["menuSelect"] == "select_gamemode":
        var = affichage_menu_select_gamemode(var, screen)
    elif var["menuSelect"] == "jeu":
        var = affichage_menu_jeu(screen, var)
    elif var["menuSelect"] == "action":
        var = affichage_menu_action(screen, var)
    elif var["menuSelect"] == "win":
        var = affichage_menu_win(screen, var)

    pygame.display.flip()
    return var


def controles_principal(var, event):
    """
    Gestion des contr??les du menu principal.
    """
    if var["button"]["jouer"].is_pressed(event):
        var["menuSelect"] = "select_gamemode"
        var["nbPlayers"] = 4
        var["nbHorses"] = 4
    return var


def controles_select_gamemode(var, event):
    """
    Gestion des contr??les du menu de s??lection du mode de jeu.
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
    Gestion des contr??les du jeu.
    """
    if var["button"]["dice"].is_pressed(event):
        var["diceResult"] = de()
        handling_horses(var, var["playerTurn"])
        var = check_win(var)
    return var


def controles_action(var, event):
    """
    Gestion des contr??les du menu d'action.
    """
    for action in range(len(var["actions"])):
        if var["button"][str(var["actions"][action][1].get_id())].is_pressed(event):
            var = horse_moving(var, action)
            var = update_horses(var)
            var["actions"] = []
            var["playerTurn"], var["nbrTurn"] = player_turn(var)
            var["menuSelect"] = "jeu"
            var = check_win(var)
            break
    return var


def controles_win(var, event):
    """
    Gestion des contr??les du menu de fin de partie.
    """
    if var["button"]["rejouer"].is_pressed(event):
        var["menuSelect"] = "jeu"
        var["win"] = None
        var["playerblueHorses"] = []
        var["playerredHorses"] = []
        var["playergreenHorses"] = []
        var["playeryellowHorses"] = []
        var["nbHorseredfinished"] = 0
        var["nbHorsebluefinished"] = 0
        var["nbHorsegreenfinished"] = 0
        var["nbHorseyellowfinished"] = 0
        var["actions"] = []
        var["playerList"] = players_list(var["nbPlayers"])
        var["playerTurn"], var["nbrTurn"] = select_first_player(var["playerList"])
        var = init_horses(var)
    elif var["button"]["menu"].is_pressed(event):
        var["menuSelect"] = "principal"
        var = reset_var(var, var["screen"])
    return var


def controles(var):
    """
    Occupation de la gestion des contr??les par rapport ?? leur menu.
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
        elif var["menuSelect"] == "win":
            var = controles_win(var, event)
    return var
