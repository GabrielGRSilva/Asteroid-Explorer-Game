
import pygame     #opensource Python library for games
from player import *
from constants import *

def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsclock = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        
    while True:                                     #Game Loop
        for event in pygame.event.get():            #For Loop to make the quit "X" work
            if event.type == pygame.QUIT:
              return
            
        screen.fill("black")
        player.draw(screen)
        player.update(dt)                   #update the player's position/rotation   
        pygame.display.flip()               #Update the full display Surface to the screen
        

        dt = (fpsclock.tick(60)) /1000                   ##This limits the FPS to 60

if __name__ == "__main__":
    main()