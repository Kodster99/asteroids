import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Assign to Player.containers after groups are defined
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    # Create the Player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField() 
    
    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for sprite in updatable:
            sprite.update(dt)
            
        screen.fill("black")
        # Draw player
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    '''print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")'''







if __name__ == "__main__":
    main()