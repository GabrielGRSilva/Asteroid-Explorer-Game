
import pygame     #opensource Python library for games
import sys        #sys commands like sys.exit()
from player import Player, Shot
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
    shots = pygame.sprite.Group()                #shots from the ship

    Player.containers = (updatablegroup, drawablegroup)     #includes Player(s) to above groups
    Asteroid.containers = (asteroids, updatablegroup, drawablegroup)
    AsteroidField.containers = (updatablegroup)
    Shot.containers = (shots, updatablegroup, drawablegroup)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #create player ship
    AsteroidField()
    dt = 0

    while True:                                     #Eternal game loop (True is always True)
        for event in pygame.event.get():            #For Loop to make the quit "X" work
            if event.type == pygame.QUIT:
              return
            
        updatablegroup.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    pygame.sprite.Sprite.kill(shot)  #removes the shot if it hits the target
                    asteroid.split()                 #see split method in asteroids.py

        screen.fill("black")

        for obj in drawablegroup:
            obj.draw(screen)                #update the player's position/rotation
                     
        pygame.display.flip()               #Update the full display Surface to the screen
        
        dt = (fpsclock.tick(60)) /1000                   ##This limits the FPS to 60

if __name__ == "__main__":
    main()