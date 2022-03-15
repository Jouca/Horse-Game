import pygame
try:
    from constant import COLOR
    from functions import get_font_size
except ModuleNotFoundError:
    from .constant import COLOR
    from .functions import get_font_size

class Button:
    """crée un bouton visuel formaté avec le style général du jeu.
    Bouton ayant la spécificité d'être de forme carré."""

    def __init__(self, window, relative_position, color):
        """méthode constructeur de la classe :
        - `window` est la fenêtre sur laquelle est créé le bouton ;
        - `relative_position` correspond à un 3-uple (`x`, `y`, `w`) - ou 4-
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
        self.rect = pygame.Rect(x_value, y_value, w_value, w_value)

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
                    pygame.mixer.Sound.play(Button1.click)
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