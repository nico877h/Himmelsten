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
White = (255, 255, 255)
gridSize = 3
sideGridSize = 5
CellSize = 100
GridSpaceing = 20


pygame.display.set_caption("Himmelsten")

display = pygame.display.set_mode((width, height))


###for x in board.felter:
    ###pygame.draw.rect(display, grey, x)

imageSize = (150, 150)
square = pygame.image.load("square.png").convert_alpha()
square = pygame.transform.scale(square, imageSize)


def draw_grid(x_offset, y_offset, rows, collums):
    for row in range(rows):
        for collum in range(collums):
            rect = pygame.Rect(x_offset + collum * (CellSize + GridSpaceing),
                               y_offset + row * (CellSize + GridSpaceing),
                               CellSize, CellSize)
            pygame.draw.rect(display, White, rect, 3)


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
            
        center_x = (width - (gridSize * CellSize + (gridSize - 1) * GridSpaceing)) // 2
        center_y = (height - (gridSize * CellSize + (gridSize - 1) * GridSpaceing)) // 2
        draw_grid(center_x, center_y, gridSize, gridSize)

        # Draw the left 1x5 grid
        left_x = center_x - (GridSpaceing + CellSize)
        left_y = (height - (sideGridSize * CellSize + (sideGridSize - 1) * GridSpaceing)) // 2
        draw_grid(left_x, left_y, sideGridSize, 1)

        # Draw the right 1x5 grid
        right_x = center_x + (gridSize * CellSize) + GridSpaceing*3
        draw_grid(right_x, left_y, sideGridSize, 1)

        display.blit(square, (left_x,left_y))
        
        pygame.display.flip()
    
        
        pygame.display.update()
    




play_himmelsten()

pygame.quit()