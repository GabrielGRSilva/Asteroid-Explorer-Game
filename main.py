
import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  #This should avoid crashes to WSL during development
import pygame     #opensource Python library for games
import sys        #sys commands like sys.exit()
from player import Player, Shot
from constants import *
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    print ("Starting Asteroid Buster!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    print ("Music: Mesmerizing Galaxy by Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 4.0 License http://creativecommons.org/licenses/by/4.0/ ")
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("Mesmerizing Galaxy Loop.mp3") #Load the game music, which will be called later

   # pygame.display.set_icon()          USE THIS LATER WITH A SURFACE ARGUMENT TO UPDATE GAME ICON
    pygame.display.set_caption("Asteroid Buster")

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
    gameloop = True
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    while gameloop == True:
        

        for event in pygame.event.get():            #For Loop to make the quit "X" work
            if event.type == pygame.QUIT:
              return
            
        updatablegroup.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                gameloop = False
                
        
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

    end_img = pygame.image.load('Gameover.png')
    end_screen = pygame.transform.scale(end_img, (SCREEN_WIDTH, SCREEN_HEIGHT)) #fit image to screen
    gow = (SCREEN_WIDTH / 2) - (end_screen.get_width() / 2)
    goh = (SCREEN_HEIGHT / 2) - (end_screen.get_height() / 2)
    end_standby = True

    while end_standby == True:
        for event in pygame.event.get():            #For Loop to make the quit "X" work
            if event.type == pygame.QUIT:
              return
            if event.type == pygame.KEYDOWN:
                sys.exit("Thanks for playing!")

        pygame.mixer.music.pause()
        screen.blit(end_screen, (gow, goh))
        pygame.display.flip()
        dt = (fpsclock.tick(60)) /1000

if __name__ == "__main__":
    main()