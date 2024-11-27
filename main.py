import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Player score
    player_score = 0

   #Load background
    background_img = pygame.image.load("./assets/newbackground.png")
   
    # Create the groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign to Player.containers after groups are defined
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    # Create the Player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField() 

    

    #Create score font
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    fontX = 10
    fontY = 10

    def display_score(x, y):
        score_img = score_font.render(f"Total Score: {str(player_score)}", True, [255, 255, 255])
        screen.blit(score_img, (x, y))
    
    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    
            
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if player.collision_check(asteroid) == True:
                print("Game Over!")
                return
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    shot.kill()
                    asteroid.split()
                    player_score += 1

            
        screen.fill("black")
        screen.blit(background_img, (0, 0))
        # Draw player
        display_score(fontX, fontY)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        #display score
        


        

    '''print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")'''







if __name__ == "__main__":
    main()