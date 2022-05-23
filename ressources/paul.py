import pygame
try:
    from constant import COLOR, PLAYER_COLORS, PLATEAU_PLAYERS_COORDINATES
except ModuleNotFoundError:
    from .constant import COLOR, PLAYER_COLORS, PLATEAU_PLAYERS_COORDINATES

dico_plato = {
    "0": (22, 330), "1": (22, 286), "2": (66, 286),
    "3": (110, 286), "4": (154, 286), "5": (198, 286),
    "6": (242, 286), "7": (286, 286), "8": (286, 242),
    "9": (286, 198), "10": (286, 154), "11": (286, 110),
    "12": (286, 66), "13": (286, 22), "14": (330, 22),
    "15": (374, 22), "16": (374, 66), "17": (374, 110),
    "18": (374, 154), "19": (374, 198), "20": (374, 242),
    "21": (374, 286), "22": (418, 286), "23": (462, 286),
    "24": (506, 286), "25": (550, 286), "26": (594, 286),
    "27": (638, 286), "28": (638, 330), "29": (638, 374),
    "30": (594, 374), "31": (550, 374), "32": (506, 374),
    "33": (462, 374), "34": (418, 374), "35": (374, 374),
    "36": (374, 418), "37": (374, 462), "38": (374, 506),
    "39": (374, 550), "40": (374, 594), "41": (374, 638),
    "42": (330, 638), "43": (286, 638), "44": (286, 594),
    "45": (286, 550), "46": (286, 506), "47": (286, 462),
    "48": (286, 418), "49": (286, 374), "50": (242, 374),
    "51": (198, 374), "52": (154, 374), "53": (110, 374),
    "54": (66, 374), "55": (22, 374),
    "1_yellow": (66, 330), "2_yellow": (110, 330), "3_yellow": (154, 330),
    "4_yellow": (198, 330), "5_yellow": (242, 330), "6_yellow": (286, 330),
    "1_blue": (330, 66), "2_blue": (330, 110), "3_blue": (330, 154),
    "4_blue": (330, 198), "5_blue": (330, 242), "6_blue": (330, 286),
    "1_red": (594, 330), "2_red": (550, 330), "3_red": (506, 330),
    "4_red": (462, 330), "5_red": (418, 330), "6_red": (374, 330),
    "1_green": (330, 594), "2_green": (330, 550), "3_green": (330, 506),
    "4_green": (330, 462), "5_green": (330, 418), "6_green": (330, 374),
    "yellow_start1": (50, 50), "yellow_start2": (150, 50), "yellow_start3": (50, 150),
    "yellow_start4": (150, 150),
    "blue_start1": (450, 50), "blue_start2": (550, 50), "blue_start3": (450, 150),
    "blue_start4": (550, 150),
    "red_start1": (450, 450), "red_start2": (450, 550), "red_start3": (550, 450),
    "red_start4": (550, 550),
    "green_start1": (50, 450), "green_start2": (150, 450), "green_start3": (50, 550),
    "green_start4": (150, 550),
    "finished": (-200, -200)
}


def show_table():
    """
    Affiche la table du jeu.
    """
    plateau = pygame.Surface((660, 660))
    frame = pygame.Surface((308, 352))
    for couleur in enumerate(PLAYER_COLORS):
        coord_x, coord_y, rotate = PLATEAU_PLAYERS_COORDINATES[couleur[0]]
        for value in range(7):
            rect_x = pygame.Rect(value * 44, 264, 44, 44)
            rect_y = pygame.Rect(264, value * 44, 44, 44)
            pygame.draw.circle(frame, COLOR[couleur[1]], rect_x.center, rect_x.width // 2)
            pygame.draw.circle(frame, COLOR[couleur[1]], rect_y.center, rect_y.width // 2)
        rect_final = pygame.Rect(0, 308, 44, 44)
        pygame.draw.circle(frame, COLOR[couleur[1]], rect_final.center, rect_final.width // 2)
        rect_stable = pygame.Rect(0, 0, 264, 264)
        pygame.draw.rect(frame, COLOR["LIGHT_" + couleur[1]], rect_stable)
        pygame.draw.rect(frame, COLOR[couleur[1]], rect_stable, 10)
        for value in range(1, 7):
            rect_case = pygame.Rect(44 * value, 308, 44, 44)
            pygame.draw.rect(frame, COLOR["LIGHT_" + couleur[1]], rect_case)
            pygame.draw.rect(frame, COLOR["BLACK"], rect_case, 2)
            font = pygame.font.Font(None, 40)
            text = font.render(str(value), True, COLOR["BLACK"])
            text_rect = text.get_rect(center=rect_case.center)
            frame.blit(text, text_rect)
        plateau.blit(pygame.transform.rotate(frame, rotate), (coord_x, coord_y))
    return plateau


def player_turn(var):
    """
    Permet de faire tourner les joueurs
    """
    nbr_turn = (var["nbrTurn"] + 1) % (len(var["playerList"]))
    return var["playerList"][nbr_turn], nbr_turn
