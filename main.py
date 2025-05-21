
import pygame     #opensource Python library for games
from player import Player
from constants import *
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsclock = pygame.time.Clock()

    updatablegroup = pygame.sprite.Group()       #all objects that are updated in the loop
    drawablegroup = pygame.sprite.Group()        #all objects that are drawn in the loop
    asteroids = pygame.sprite.Group()            #group with asteroid objects

    Player.containers = (updatablegroup, drawablegroup)     #includes Player(s) to above groups
    Asteroid.containers = (asteroids, updatablegroup, drawablegroup)
    AsteroidField.containers = (updatablegroup)

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #create player ship
    AsteroidField()
    dt = 0

    while True:                                     #Game Loop
        for event in pygame.event.get():            #For Loop to make the quit "X" work
            if event.type == pygame.QUIT:
              return
            
        updatablegroup.update(dt) 

        screen.fill("black")

        for obj in drawablegroup:
            obj.draw(screen)  #update the player's position/rotation
                     
        pygame.display.flip()               #Update the full display Surface to the screen
        
        dt = (fpsclock.tick(60)) /1000                   ##This limits the FPS to 60

if __name__ == "__main__":
    main()