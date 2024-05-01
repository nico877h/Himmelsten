import pygame
import board
import brikker 
import menu
import værdier

pygame.init()

size = (500,500)


canvas = pygame.display.set_mode((size))
pygame.display.set_caption("Himmelsten")




def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
     
    pygame.display.update()

main()





pygame.quit()