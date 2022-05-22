import pygame
import random
from PIL import ImageOps, Image
try:
    from constant import FONT_HEIGHT, COLOR, LISTE_ECURIES, LISTE_ECHELLE
    from paul import dico_plato, player_turn
except ModuleNotFoundError:
    from .constant import FONT_HEIGHT, COLOR, LISTE_ECURIES, LISTE_ECHELLE
    from .paul import dico_plato, player_turn

def get_font_size(font_height):
    """récupère une valeur de taille de police selon `font_height` un entier
    naturel représentant la hauteur de font voulu en nombre de pixel sur la
    fenêtre de jeu."""
    if font_height < 19:
        return 12
    i = 0
    try:
        while font_height > FONT_HEIGHT[i]:
            i += 1
    except IndexError:
        pass
    return i + 12


def apply_color(image, color):
    alpha = image.split()[3]  # [r, g, b, a][3] -> a

    colored = ImageOps.colorize(
        image.convert("L"), black=(0, 0, 0), white=color
    )
    colored.putalpha(alpha)

    return colored


def load_PIL_image(image_path):
    """Charge une image en utilisant PIL"""
    return Image.open(image_path)


def convert_PIL_to_pygame(image):
    """
    Convertit une image PIL en image pygame.
    """
    mode = image.mode
    size = image.size
    data = image.tobytes()

    py_image = pygame.image.fromstring(data, size, mode)
    return py_image


def select_first_player(list_players):
    """
    Sélectionne le premier joueur qui va jouer en premier.
    """
    player_turn = random.randint(0, len(list_players) - 1)
    return list_players[player_turn], player_turn


def players_list(integer):
    """
    Crée la liste des joueurs en fonction du nombre de joueurs dans la partie.
    """
    if integer == 2:
        return ["blue", "green"]
    return ["blue", "red", "green", "yellow"][:integer]


def draw_horses(plateau, var):
    """
    Dessine les chevaux sur le plateau.
    """
    for player in var["playerList"]:
        for horse in var[f"player{player}Horses"]:
            horse.draw(plateau)


def init_horses(var):
    """
    Initialise les chevaux.
    """
    for player in var["playerList"]:
        for id in range(1, var["nbHorses"]+1):
            var[f"player{player}Horses"].append(
                Horse(
                    player,
                    id,
                )
            )
    return var


def check_player_can_enter(var, player, horse):
    confirm = False
    for horse_enter in var[f"player{player}Horses"]:
        if player == "blue":
            if horse_enter.get_position() == "15":
                confirm = True
        elif player == "red":
            if horse_enter.get_position() == "29":
                confirm = True
        elif player == "green":
            if horse_enter.get_position() == "43":
                confirm = True
        elif player == "yellow":
            if horse_enter.get_position() == "1":
                confirm = True
    if confirm is False:
        var["actions"].append([player, horse, "exit_ecure"])


def check_player_not_colliding_same_color(var, player, position):
    """
    Vérifie si le joueur ne peut pas rentrer dans un autre cheval de la même couleur.
    """
    confirm = False
    for player_other in var[f"player{player}Horses"]:
        if player_other.get_position() == position:
            confirm = True
    return confirm


def check_horse_collision(var, horse_position, player):
    """
    Vérifie si un cheval est en collision avec un autre cheval.
    """
    confirm = False
    for player_other in var["playerList"]:
        if player_other != player:
            for player_horse in var[f"player{player_other}Horses"]:
                if player_horse.get_position() == horse_position:
                    confirm = True
                    break
            if confirm is True:
                break
    return confirm, (player_other, player_horse.get_id(), player_horse)


def check_move(var, player, horse, position):
    """
    Vérifie si le cheval peut se déplacer.
    """
    if player == "blue":
        if horse.get_position() == "14" and var["diceResult"] == 1:
            horse.set_position("1_blue")
        elif horse.get_position() == "1_blue" and var["diceResult"] == 2:
            horse.set_position("2_blue")
        elif horse.get_position() == "2_blue" and var["diceResult"] == 3:
            horse.set_position("3_blue")
        elif horse.get_position() == "3_blue" and var["diceResult"] == 4:
            horse.set_position("4_blue")
        elif horse.get_position() == "4_blue" and var["diceResult"] == 5:
            horse.set_position("5_blue")
        elif horse.get_position() == "5_blue" and var["diceResult"] == 6:
            horse.set_position("6_blue")
        elif horse.get_position() == "6_blue" and var["diceResult"] == 6:
            print("Vous avez gagné !")
        elif int(position) > 14 and int(horse.get_position()) <= 14 and int(horse.get_position()) >= 8:
            horse.set_position(str(14 - (int(position) - 14)))
        else:
            horse.set_position(str(int(position) % 56))
    elif player == "red":
        if horse.get_position() == "28" and var["diceResult"] == 1:
            horse.set_position("1_red")
        elif horse.get_position() == "1_red" and var["diceResult"] == 2:
            horse.set_position("2_red")
        elif horse.get_position() == "2_red" and var["diceResult"] == 3:
            horse.set_position("3_red")
        elif horse.get_position() == "3_red" and var["diceResult"] == 4:
            horse.set_position("4_red")
        elif horse.get_position() == "4_red" and var["diceResult"] == 5:
            horse.set_position("5_red")
        elif horse.get_position() == "5_red" and var["diceResult"] == 6:
            horse.set_position("6_red")
        elif horse.get_position() == "6_red" and var["diceResult"] == 6:
            print("Vous avez gagné !")
        elif int(position) > 28 and int(horse.get_position()) <= 28 and int(horse.get_position()) >= 22:
            horse.set_position(str(28 - (int(position) - 28)))
        else:
            horse.set_position(str(int(position) % 56))
    elif player == "green":
        if horse.get_position() == "42" and var["diceResult"] == 1:
            horse.set_position("1_green")
        elif horse.get_position() == "1_green" and var["diceResult"] == 2:
            horse.set_position("2_green")
        elif horse.get_position() == "2_green" and var["diceResult"] == 3:
            horse.set_position("3_green")
        elif horse.get_position() == "3_green" and var["diceResult"] == 4:
            horse.set_position("4_green")
        elif horse.get_position() == "4_green" and var["diceResult"] == 5:
            horse.set_position("5_green")
        elif horse.get_position() == "5_green" and var["diceResult"] == 6:
            horse.set_position("6_green")
        elif horse.get_position() == "6_green" and var["diceResult"] == 6:
            print("Vous avez gagné !")
        elif int(position) > 42 and int(horse.get_position()) <= 42 and int(horse.get_position()) >= 36:
            horse.set_position(str(42 - (int(position) - 42)))
        else:
            horse.set_position(str(int(position) % 56))
    elif player == "yellow":
        # Merci à RealistikDash de m'avoir aidé sur cette partie de code TwT
        ladder_point = 0
        if horse.get_position() == str(ladder_point) and var["diceResult"] == 1:
            horse.set_position("1_yellow")
        elif horse.get_position() == str(ladder_point) and var["diceResult"] != 1:
            new_pos = int(horse.get_position()) - var["diceResult"]
            horse.set_position(str(new_pos % 56))
        elif "_" in horse.get_position():
            field, colour = horse.get_position().split("_")
            field = int(field)
            if field == 6 and var["diceResult"] == 6:
                print("Vous avez gagné !")
            elif field == var["diceResult"] - 1:
                horse.set_position(f"{field + 1}_{colour}")
        else:
            normalised_pos = int(position) % 56
            old_pos = int(horse.get_position())

            if old_pos > 50 and normalised_pos < 6:
                new_pos = 56 - normalised_pos
                horse.set_position(str(new_pos) if new_pos != 56 else "0")
            else:
                horse.set_position(str(normalised_pos))
    else:
        horse.set_position(str(int(position) % 56))
    return var, horse.get_position()


def check_ladder(var, player, horse):
    """
    Vérifie si le cheval peut se déplacer sur une escalier.
    """
    if player == "blue":
        if horse.get_position() == "1_blue" and var["diceResult"] == 2:
            return True
        elif horse.get_position() == "2_blue" and var["diceResult"] == 3:
            return True
        elif horse.get_position() == "3_blue" and var["diceResult"] == 4:
            return True
        elif horse.get_position() == "4_blue" and var["diceResult"] == 5:
            return True
        elif horse.get_position() == "5_blue" and var["diceResult"] == 6:
            return True
        elif horse.get_position() == "6_blue" and var["diceResult"] == 6:
            return True
    elif player == "red":
        if horse.get_position() == "1_red" and var["diceResult"] == 2:
            return True
        elif horse.get_position() == "2_red" and var["diceResult"] == 3:
            return True
        elif horse.get_position() == "3_red" and var["diceResult"] == 4:
            return True
        elif horse.get_position() == "4_red" and var["diceResult"] == 5:
            return True
        elif horse.get_position() == "5_red" and var["diceResult"] == 6:
            return True
        elif horse.get_position() == "6_red" and var["diceResult"] == 6:
            return True
    elif player == "green":
        if horse.get_position() == "1_green" and var["diceResult"] == 2:
            return True
        elif horse.get_position() == "2_green" and var["diceResult"] == 3:
            return True
        elif horse.get_position() == "3_green" and var["diceResult"] == 4:
            return True
        elif horse.get_position() == "4_green" and var["diceResult"] == 5:
            return True
        elif horse.get_position() == "5_green" and var["diceResult"] == 6:
            return True
        elif horse.get_position() == "6_green" and var["diceResult"] == 6:
            return True
    elif player == "yellow":
        if horse.get_position() == "1_yellow" and var["diceResult"] == 2:
            return True
        elif horse.get_position() == "2_yellow" and var["diceResult"] == 3:
            return True
        elif horse.get_position() == "3_yellow" and var["diceResult"] == 4:
            return True
        elif horse.get_position() == "4_yellow" and var["diceResult"] == 5:
            return True
        elif horse.get_position() == "5_yellow" and var["diceResult"] == 6:
            return True
        elif horse.get_position() == "6_yellow" and var["diceResult"] == 6:
            return True
    
    

def handling_horses(var, player):
    """
    Gère les déplacements des chevaux d'un joueur.
    """
    for horse in var[f"player{player}Horses"]:
        try:
            horse_position = str(int(horse.get_position()) + var["diceResult"])
            if int(horse_position) > 55:
                horse_position = str(-56 + int(horse_position) + var["diceResult"])
        except ValueError:
            if player == "red":
                horse_position = "29"
            elif player == "blue":
                horse_position = "15"
            elif player == "green":
                horse_position = "43"
            elif player == "yellow":
                horse_position = "1"
        if horse.get_position() in LISTE_ECURIES and var["diceResult"] == 6:
            check_player_can_enter(var, player, horse)
        elif horse.get_position() in LISTE_ECHELLE:
            if check_ladder(var, player, horse):
                var["actions"].append([player, horse, "move"])
        elif horse.get_position() not in LISTE_ECURIES:
            if check_player_not_colliding_same_color(var, player, horse_position) is False:
                var["actions"].append([player, horse, "move"])
    print(var["actions"])
    if len(var["actions"]) >= 2:
        var["menuSelect"] = "action"
    elif len(var["actions"]) == 1:
        var = horse_moving(var, 0)
        var = update_horses(var)
        var["actions"] = []
        var["playerTurn"], var["nbrTurn"] = player_turn(var)
    elif len(var["actions"]) == 0:
        var["playerTurn"], var["nbrTurn"] = player_turn(var)
    return var


def horse_moving(var, id):
    horse_position = None
    player = var["actions"][id][0]
    horse = var["actions"][id][1]
    action_type = var["actions"][id][2]
    if action_type == "exit_ecure":
        if player == "red":
            horse.set_position("29")
            horse_position = horse.get_position()
        elif player == "blue":
            horse.set_position("15")
            horse_position = horse.get_position()
        elif player == "green":
            horse.set_position("43")
            horse_position = horse.get_position()
        elif player == "yellow":
            horse.set_position("1")
            horse_position = horse.get_position()
    elif action_type == "move":
        try:
            var, horse_position = check_move(var, player, horse, str(int(horse.get_position()) + var["diceResult"]))
        except ValueError:
            var, horse_position = check_move(var, player, horse, horse.get_position())
    if check_horse_collision(var, horse_position, player)[0] is True:
        player_collisioned, id, horse_collisioned = check_horse_collision(var, horse_position, player)[1]
        horse_collisioned.set_position(f"{player_collisioned}_start{id}")
    return var


def update_horses(var):
    for action in range(len(var["actions"])):
        if var["actions"][action][0] == "red":
            var["playerredHorses"][var["actions"][action][1].get_id()-1] = var["actions"][action][1]
        elif var["actions"][action][0] == "blue":
            var["playerblueHorses"][var["actions"][action][1].get_id()-1] = var["actions"][action][1]
        elif var["actions"][action][0] == "green":
            var["playergreenHorses"][var["actions"][action][1].get_id()-1] = var["actions"][action][1]
        elif var["actions"][action][0] == "yellow":
            var["playeryellowHorses"][var["actions"][action][1].get_id()-1] = var["actions"][action][1]
    return var


class Horse():
    """
    Classe représentant un cheval.
    """
    def __init__(self, player, horse_id):
        self.player = player
        self.horse_id = horse_id
        self.position = dico_plato[f"{player}_start{horse_id}"]
        self.position_name = f"{player}_start{horse_id}"
        self.image = load_PIL_image(f"ressources/sprites/chess.png")
        self.image = apply_color(self.image, COLOR[player.upper()])
        self.image = convert_PIL_to_pygame(self.image)
        self.image = pygame.transform.scale(self.image, (40, 40))

    def draw(self, surface):
        surface.blit(self.image, (self.position[0] - 20, self.position[1] - 20))

    def draw_id(self, surface):
        font = pygame.font.SysFont("Arial", 25)
        font_background = pygame.font.SysFont("Arial", 29)
        text = font.render(f"{self.horse_id}", True, (255, 255, 255))
        text2 = font_background.render(f"{self.horse_id}", True, (0, 0, 0))
        surface.blit(text2, (self.position[0] - 6, self.position[1] - 17))
        surface.blit(text, (self.position[0] - 5, self.position[1] - 15))

    def get_position(self):
        return self.position_name

    def get_id(self):
        return self.horse_id

    def get_player(self):
        return self.player

    def set_position(self, position):
        self.position = dico_plato[position]
        self.position_name = position


class Button:
    """crée un bouton visuel formaté avec le style général du jeu.
    Bouton ayant la spécificité d'être de forme carré."""

    def __init__(self, window, relative_position, color):
        """méthode constructeur de la classe :
        - `window` est la fenêtre sur laquelle est créé le bouton ;
        - `relative_position` correspond à un 4-uple (`x`, `y`, `w`, `h`) - ou 4-
        uple sans que la dernière valeur soit gênante au code - indiquant la
        position et les dimensions relatives selon les dimensions `window` sur
        la fenêtre de jeu, toutes les valeurs doivent être comprises entre 0
        et 1 exclus afin que le bouton soit visible, dans l'ordre :
            - position relative `x`, positionnement x par rapport à la largeur
            de la fenêtre (sur bord gauche lorsque `x` vaut 0, droit lorsque
            `x` vaut 1 (sort du cadre)) ;
            - position relative `y`, positionnement y par rapport à la longueur
            de la fenêtre (sur le bord haut lorsque `y` vaut 0, sur le bord bas
            lorsque `y` vaut 1 auquel cas ne sera pas visible puisque le bouton
            sortira du cadre de la fenêtre)) ;
            - valeur `w`, représente la largeur du bouton selon la largeur de
            la fenêtre (pour `w` égal à 0, le bouton est inexistant ce qui
            n'est pas très intéressant, lorsque `w` vaut 1, le bouton possède
            une largeur égale à celle de la fenêtre) ;
            valeur `h`, représente la hauteur du bouton selon la hauteur de
            la fenêtre (pour `h` égal à 0, le bouton est inexistant ce qui
            n'est pas très intéressant, lorsque `h` vaut 1, le bouton possède
            une hauteur égale à celle de la fenêtre) ;
        - `color`, enfin est la couleur du bouton, un 3-ple correspondant aux
        niveau de rouge, vert et de bleu (format RGB de couleur)."""
        self.relative_position = relative_position
        self.resize(window)
        self.color = color

    def resize(self, window):
        """méthode permettant de redimensionner selon une surface et ce par
        rapport à la taille de la fenêtre pygame. `window` est un objet
        pygame.Surface."""
        # définition des valeurs d'emplacement du bouton selon la surface
        # `window` spécifié
        window_w, window_h = window.get_size()
        x_value = round(self.relative_position[0] * window_w)
        y_value = round(self.relative_position[1] * window_h)
        w_value = round(self.relative_position[2] * window_w)
        h_value = round(self.relative_position[3] * window_h)
        # dans le cas où window.rect.x existe, `window` est une surface
        # ayant été blit sur la fenêtre de jeu
        try:
            # il s'agit de définir les vraies coordonnées en tenant compte
            # du décalage dû à `window` qui n'est pas la fenêtre de jeu
            x_value += window.rect.x
            y_value += window.rect.y
        # autrement la surface est bien celle de la fenêtre de jeu,
        # décalage non nécéssaire.
        except AttributeError:
            pass
        # attribution des valeurs d'emplacement
        self.rect = pygame.Rect(x_value, y_value, w_value, h_value)

    def draw(self, surface):
        """permet de dessiner le bouton sur une surface `surface` devant
        être un objet pygame.Surface."""
        # dessin du fond du bouton rempli avec la couleur attribuée
        pygame.draw.rect(surface, self.color, self.rect)
        # dessin de l'encadré du bouton avec un niveau de gris
        pygame.draw.rect(surface, (150, 150, 150), self.rect, 3)

    def is_pressed(self, event):
        """permet de détecter si le joueur a fait un clic gauche
        sur le bouton. Renvoie un booléen, True si le bouton est cliqué,
        False sinon. `event` correspond à un objet pygame.Event."""
        # dans le cas où le joueur appuie avec le bouton gauche de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # dans le cas où l'appuie est effectué sur un bouton
                if self.mouse_on(event):
                    # le son "click" est joué 
                    return True        
        return False
    
    def get_color(self):
        """renvoie la couleur de fond du bouton."""
        return self.color
    
    def change_color(self, color):
        """change la couleur du bouton pour `color` un 3-tuple au format
        RGB de couleur."""
        self.color = color

    def mouse_on(self, event):
        """détecte si la souris est sur le bouton. La méthode renvoie
        True si c'est bien le cas, autrement elle renvoie False."""
        if self.rect.collidepoint(event.pos):
            return True            
        return False

    def get_size(self):
        """renvoie les dimensions du bouton sous la forme d'un 2-uple
        largeur et longueur du bouton."""
        return (self.rect.w, self.rect.h)

    def get_height(self):
        """renvoie la longueur du bouton."""
        return self.rect.h
    
    def get_width(self):
        """renvoie la largeur du bouton."""
        return self.rect.w

class Button1(Button):
    """crée un bouton visuel contenant un texte centré."""

    def __init__(self, window, relative_position, text, color=COLOR['BLACK']):
        """méthode constructeur de la classe :
        - `window` est la fenêtre sur laquelle est créé le bouton ;
        - `relative_position` correspond à un 4-uple (`x`, `y`, `w`, `h`)
        indiquant la position et les dimensions relatives selon les dimensions
        de la fenêtre, toutes les valeurs doivent être comprises entre 0 et 1
        exclus afin que le bouton soit visible, dans l'ordre :
            - position relative `x`, positionnement x par rapport à la largeur
            de la fenêtre (sur bord gauche lorsque `x` vaut 0, droit lorsque
            `x` vaut 1 (sort du cadre)) ;
            - position relative `y`, positionnement y par rapport à la longueur
            de la fenêtre (sur le bord haut lorsque `y` vaut 0, sur le bord bas
            lorsque `y` vaut 1 auquel cas ne sera pas visible puisque le bouton
            sortira du cadre de la fenêtre)) ;
            - valeur `w`, représente la largeur du bouton selon la largeur de
            la fenêtre (pour `w` égal à 0, le bouton est inexistant ce qui
            n'est pas très intéressant, lorsque `w` vaut 1, le bouton possède
            une largeur égale à celle de la fenêtre) ;
            - valeur `h`, représente la longueur du bouton selon la longueur
            de la fenêtre (pour `h` égal à 0, le bouton est inexistant ce qui
            n'est pas très intéressant, lorsque `w` vaut 1, le bouton possède
            une longueur égale à celle de la fenêtre)
        - `text` est le texte associé au bouton, doit être une chaîne de
        caractères ;
        - `font_size`, un entier spécifiant la taille de la police pour le texte
        à afficher sur le bouton visuel, dans le cas où elle n'est pas
        indiqué, la taille dépendra de la hauteur du bouton."""
        self.text = text
        super().__init__(window, relative_position, color)

    def resize(self, window):
        super().resize(window)
        window_h = window.get_height()
        h_value = round(self.relative_position[3] * window_h)
        self.rect.h = h_value
        font_size = get_font_size(round(self.rect.h * 0.6))
        font = pygame.font.SysFont("./fonts/PetMe64.ttf", font_size)
        self.text_image = font.render(self.text, 1, COLOR['WHITE'])
        self.text_pos = self.text_image.get_rect(center=self.rect.center)

    def draw(self, surface):
        """permet de dessiner le bouton sur une surface `surface` devant
        être un objet pygame.Surface"""
        super().draw(surface)
        surface.blit(self.text_image, self.text_pos)

    def change_color(self, color):
        super().change_color(color)


class Text:
    """modélise un texte visuel formaté avec le style général du jeu."""

    def __init__(self, window, relative_position, text, left_align=False, color=COLOR['WHITE']):
        """méthode constructeur de la classe :
        - `window` est la fenêtre sur laquelle est créé le bouton ;
        - `relative_position` correspond à un 4-uple (`x`, `y`, `w`, `h`)
        indiquant la position et les dimensions relatives selon les dimensions
        de la fenêtre, toutes les valeurs doivent être comprises entre 0 et 1
        exclus afin que le bouton soit visible, dans l'ordre :
            - position relative `x`, positionnement x par rapport à la largeur
            de la fenêtre (sur bord gauche lorsque `x` vaut 0, droit lorsque
            `x` vaut 1 (sort du cadre)) ;
            - position relative `y`, positionnement y par rapport à la longueur
            de la fenêtre (sur le bord haut lorsque `y` vaut 0, sur le bord bas
            lorsque `y` vaut 1 auquel cas ne sera pas visible puisque le
            rectangle associé au texte sortira du cadre de la fenêtre)) ;
            - valeur `w`, représente la largeur du texte selon la largeur de
            la fenêtre (pour `w` égal à 0, le texte est apparent, seulement, son
            emplacement sur l'axe des abscisse est peu certaine, ce qui est peu
            recommendable pour contrôler la disposition des objets pour la partie
            graphique. Lorsque `w` vaut 1, le texte possède une largeur dépendant
            fortement de la longueur du texte) ;
            - valeur `h`, représente la longueur du texte selon la proportion par
            rapport à la longueur de la fenêtre. Cette valeur est approximative et
            fait appel à une fonction permettant de trouver la taille de la police
            sient le mieux l'exigence (pour `h` égal à 0, le texte est égal à 12,
            ce qui et peu intéressant vu que cela rend impossible un
            redimensionnement s'adaptant à la taille de la fenêtre vu que fixe.
            Lorsque `h` vaut 1, le texte possède une longueur égale approche celle
            de la fenêtre ou soulèvera une erreur si la résolution de l'écran est
            supérieur à la marge laissé au préalable).
        - `text` est le texte à afficher, doit être une chaîne de caractères ;
        - `color` est la couleur du texte, par défaut `color` est `COLOR['WHITE']`
        >>> text = Text((0.3, 0.4, 0.4, 0.2), "Hello world !")"""
        window_w, window_h = window.get_size()
        x_value = round(relative_position[0] * window_w)
        y_value = round(relative_position[1] * window_h)
        w_value = round(relative_position[2] * window_w)
        font_size = get_font_size(round(relative_position[3] * window_h))
        font = pygame.font.SysFont("./others/Anton-Regular.ttf", font_size)
        self.text = text
        self.text_image = font.render(text, 1 , color)
        try:
            x_value += window.rect.x
            y_value += window.rect.y
        # dans le cas où l'objet n'est pas dépendant d'un autre mais de la fenêtre de jeu
        except AttributeError:
            pass
        self.rect = pygame.Rect(x_value, y_value, w_value, font_size)
        self.text_pos = self.text_image.get_rect(center = self.rect.center)
        if left_align:
            self.text_pos[0] = x_value

    def draw(self, surface):
        """permet de dessiner le bouton sur une surface `surface` devant
        être un objet pygame.Surface"""
        surface.blit(self.text_image, self.text_pos)
    
    def get_text(self):
        return self.text