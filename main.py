# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    while True:
        pygame.Surface.fill(pygame.screen, "black")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return


if __name__ == "__main__":
    main()