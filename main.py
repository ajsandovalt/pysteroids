import pygame
from pygame.mixer_music import play
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Initiate pygame
    pygame.init()

    #Declare surface to draw stuff on
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Clock to calculate the delta time
    clock = pygame.time.Clock()
    dt = 0
    fps_limit = 144

    #Calculate initial position for player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Sprite groupd to update all our sprites at once
    updatable = pygame.sprite.Group()

    #Sprite group to draw all our sprites on screen.
    drawable = pygame.sprite.Group()

    #Create a new player object and add them to the groups
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    #Gameloop:
    while True:
        #Catch close-window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Update all of the objects on screen
        updatable.update(dt)

        #Background color
        screen.fill("black")

        #Draw all objects on screen
        for sprite in drawable:
            sprite.draw(screen)

        #Update suface 
        pygame.display.flip()

        #Calculate delta time
        dt = clock.tick(fps_limit) / 1000

if __name__ == "__main__":
    main()
