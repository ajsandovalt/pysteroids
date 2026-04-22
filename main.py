import pygame
from logger import log_state
from constants import *
from player import *

def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver} ")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Now we set the screen properties 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instatiate player

    player = Player( SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    # Initiate game loop

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
