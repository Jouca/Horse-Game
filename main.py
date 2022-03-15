import pygame

screen_size = (960, 720)
pygame.init()

def main():
    """
    Boucle du jeu
    """
    pygame.display.set_caption("Pygame")
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 720, 720))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()