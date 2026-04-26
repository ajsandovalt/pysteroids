import pygame
import sys
from logger import log_state, log_event
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import *

def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver} ")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Add classes to their respective groups
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable) 
    Shot.containers = (shots ,updatable, drawable)



    # Instatiate objs
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player( SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0 # dt = Delta Time


    # Initiate game loop

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Call groups methods
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        # Check for collitions
        for aster in asteroids:
            if aster.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            # Shot collition
            for shot in shots:
                if shot.collides_with(aster):
                    log_event("asteroid_shot")
                    shot.kill()
                    aster.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
