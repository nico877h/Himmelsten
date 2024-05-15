import pygame
import random
from board import Board
from brikker import Brikker 
import menu
import værdier

pygame.init()

board = Board()
brikker = Brikker()

width, height = (800,600)
grey = (120,120,120)
White = (255,255,255)
gridSize = 3
sideGridSize = 5
CellSize = 100
GridSpaceing = 20


pygame.display.set_caption("Himmelsten")

display = pygame.display.set_mode((width, height))


###for x in board.felter:
    ###pygame.draw.rect(display, grey, x)

imageSize = (CellSize, CellSize)
square_img = pygame.image.load("square.png").convert_alpha()
square_img = pygame.transform.scale(square_img, imageSize)


def draw_grid(x_offset, y_offset, rows, collums):
    for row in range(rows):
        for collum in range(collums):
            rect = pygame.Rect(x_offset + collum * (CellSize + GridSpaceing),
                               y_offset + row * (CellSize + GridSpaceing), CellSize, CellSize)
            pygame.draw.rect(display, White, rect, gridSize)

#Draw 5 cards from deck list
def draw_cards():
    if len(brikker.deck) >= 5:
        return random.sample(brikker.deck, 5)
    else:
        print("not enough cards in deck")
        return None

#use Draw card function
player1_cards = draw_cards()
if player1_cards:
    print("player1 drew")
    for card in player1_cards:
        print("-",card)
        
#use Draw card function
player2_cards = draw_cards()
if player2_cards:
    print("player2 drew")
    for card in player2_cards:
        print("-",card)

#main
def play_himmelsten():
    run=True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        #Draw main 3x3 grid
        center_x = (width - (gridSize * CellSize + (gridSize - 1) * GridSpaceing)) // 2
        center_y = (height - (gridSize * CellSize + (gridSize - 1) * GridSpaceing)) // 2
        draw_grid(center_x, center_y, gridSize, gridSize)

        #Draw left 1x5 grid
        left_x = center_x - (GridSpaceing + CellSize)
        left_y = (height - (sideGridSize * CellSize + (sideGridSize - 1) * GridSpaceing)) // 2
        draw_grid(left_x, left_y, sideGridSize, 1)

        # Draw right 1x5 grid
        right_x = center_x + (gridSize * CellSize) + GridSpaceing*3
        draw_grid(right_x, left_y, sideGridSize, 1)

        
        for iterator, square in enumerate(player1_cards):
            display.blit(square_img, (left_x,left_y+iterator*(CellSize+GridSpaceing)))
            font = pygame.font.Font(None, 50)
            text1N = font.render(str(player1_cards[iterator]["north"]), 1, White)
            text1S = font.render(str(player1_cards[iterator]["south"]), 1, White)
            text1E = font.render(str(player1_cards[iterator]["east"]), 1, White)
            text1W = font.render(str(player1_cards[iterator]["west"]), 1, White)

            display.blit(text1N,(left_x+40,(left_y)+iterator*(CellSize+GridSpaceing)))
            display.blit(text1S,(left_x+40,(left_y)+iterator*(CellSize+GridSpaceing)+70))
            display.blit(text1E,(left_x+75,(left_y)+iterator*(CellSize+GridSpaceing)+35))
            display.blit(text1W,(left_x+5,(left_y)+iterator*(CellSize+GridSpaceing)+35))


        
        for iterator, square in enumerate(player2_cards):
            display.blit(square_img, (right_x,left_y+iterator*(CellSize+GridSpaceing)))
            text2N = font.render(str(player2_cards[iterator]["north"]), 1, White)
            text2S = font.render(str(player2_cards[iterator]["south"]), 1, White)
            text2E = font.render(str(player2_cards[iterator]["east"]), 1, White)
            text2W = font.render(str(player2_cards[iterator]["west"]), 1, White)

            display.blit(text2N,(right_x+40,(left_y)+iterator*(CellSize+GridSpaceing)))
            display.blit(text2S,(right_x+40,(left_y)+iterator*(CellSize+GridSpaceing)+70))
            display.blit(text2E,(right_x+75,(left_y)+iterator*(CellSize+GridSpaceing)+35))
            display.blit(text2W,(right_x+5,(left_y)+iterator*(CellSize+GridSpaceing)+35))


        pygame.display.update()
    


play_himmelsten()

pygame.quit()