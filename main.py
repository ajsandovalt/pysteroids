import pygame
from pygame.mixer_music import play
from constants import *
from player import *
from asteroid import *
from asteroidsfield import *
import sys

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

    #Sprite group for the asteroids
    asteroids = pygame.sprite.Group()

    #Create a new player object and add them to the groups
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # Add Asteroid to the sprite groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add Asteroidsfield only to updatable group
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #Gameloop:
    while True:
        #Catch close-window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Update all of the objects on screen
        updatable.update(dt)

        #Check for collitions, exit if true
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit(0)

        #Fill surface with color
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
