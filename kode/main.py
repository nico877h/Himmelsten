import pygame
import board
import brikker 
import menu
import værdier

pygame.init()

size = (500,500)
color = (120,120,120)
felt1 = pygame.Rect(60, 10, 120, 120)
felt2 = pygame.Rect(190, 10, 120, 120)
felt3 = pygame.Rect(320, 10, 120, 120)
felt4 = pygame.Rect(60, 140, 120, 120)
felt5 = pygame.Rect(190, 140, 120, 120)
felt6 = pygame.Rect(320, 140, 120, 120)
felt7 = pygame.Rect(60, 270, 120, 120)
felt8 = pygame.Rect(190, 270, 120, 120)
felt9 = pygame.Rect(320, 270, 120, 120)




pygame.display.set_caption("Himmelsten")

display = pygame.display.set_mode((size))

pygame.draw.rect(display, color, felt1)
pygame.draw.rect(display, color, felt2)
pygame.draw.rect(display, color, felt3)
pygame.draw.rect(display, color, felt4)
pygame.draw.rect(display, color, felt5)
pygame.draw.rect(display, color, felt6)
pygame.draw.rect(display, color, felt7)
pygame.draw.rect(display, color, felt8)
pygame.draw.rect(display, color, felt9)




pygame.display.flip()



def main():
    run=True


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    
    pygame.display.update()





main()

pygame.quit()