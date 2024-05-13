import pygame
import random
from board import Board
from brikker import Brikker 
import menu
import værdier

pygame.init()

board = Board()
brikker = Brikker()

size = (800,500)
grey = (120,120,120)
White = (0,0,0)


pygame.display.set_caption("Himmelsten")

display = pygame.display.set_mode((size))


for x in board.felter:
    pygame.draw.rect(display, grey, x)

imageSize = (200, 200)
square = pygame.image.load("square.png").convert_alpha()
square = pygame.transform.scale(square, imageSize)




def draw_cards():
    if len(brikker.deck) >= 5:
        return random.sample(brikker.deck, 5)
    else:
        print("not enough cards in deck")
        return None


player1_cards = draw_cards()
if player1_cards:
    print("player1 drew")
    for card in player1_cards:
        print("-",card)
        

player2_cards = draw_cards()
if player2_cards:
    print("player2 drew")
    for card in player2_cards:
        print("-",card)



def play_himmelsten():
    run=True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        display.blit(square, (0,0))
        
        pygame.display.flip()
    
        
        pygame.display.update()
    




play_himmelsten()

pygame.quit()