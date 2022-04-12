import pygame
try:
    from constant import COLOR, PLAYER_COLORS
except ModuleNotFoundError:
    from .constant import COLOR, PLAYER_COLORS

dico_plato = {
    "0": (None), "1": (None), "2": (None),
    "3": (None), "4": (None), "5": (None),
    "6": (None), "7": (None), "8": (None),
    "9": (None), "10": (None), "11": (None),
    "12": (None), "13": (None), "14": (None),
    "15": (None), "16": (None), "17": (None),
    "18": (None), "19": (None), "20": (None),
    "21": (None), "22": (None), "23": (None),
    "24": (None), "25": (None), "26": (None),
    "27": (None), "28": (None), "29": (None),
    "30": (None), "31": (None), "32": (None),
    "33": (None), "34": (None), "35": (None),
    "36": (None), "37": (None), "38": (None),
    "39": (None), "40": (None), "41": (None),
    "42": (None), "43": (None), "44": (None),
    "45": (None), "46": (None), "47": (None),
    "48": (None), "49": (None), "50": (None),
    "51": (None), "52": (None), "53": (None),
    "54": (None), "55": (None)}

def show_table(window):
    plateau = pygame.Surface((660, 660))
    frame = pygame.Surface((308, 352))
    for couleur in enumerate(PLAYER_COLORS):
        for value in range(7):
            rect_x = pygame.Rect(value * 44, 264, 44, 44)
            rect_y = pygame.Rect(264, value * 44, 44, 44)
            pygame.draw.circle(frame, COLOR[couleur[1]], rect_x.center, rect_x.width // 2)
            pygame.draw.circle(frame, COLOR[couleur[1]], rect_y.center, rect_y.width // 2)
        rect_final = pygame.Rect(0, 308, 44, 44)
        pygame.draw.circle(frame, COLOR[couleur[1]], rect_final.center, rect_final.width // 2)
        rect_stable = pygame.Rect(0, 0, 264, 264)
        pygame.draw.rect(frame, COLOR["LIGHT_"+couleur[1]], rect_stable)
        pygame.draw.rect(frame, COLOR[couleur[1]], rect_stable, 10)

    plateau.blit(frame, (0, 0))
    return plateau