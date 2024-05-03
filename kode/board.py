import pygame

class Board():
        def __init__(self):
            self.felt1 = pygame.Rect(210, 50, 120, 120)
            self.felt2 = pygame.Rect(340, 50, 120, 120)
            self.felt3 = pygame.Rect(470, 50, 120, 120)
            self.felt4 = pygame.Rect(210, 180, 120, 120)
            self.felt5 = pygame.Rect(340, 180, 120, 120)
            self.felt6 = pygame.Rect(470, 180, 120, 120)
            self.felt7 = pygame.Rect(210, 310, 120, 120)
            self.felt8 = pygame.Rect(340, 310, 120, 120)
            self.felt9 = pygame.Rect(470, 310, 120, 120)
            self.felter = [self.felt1, self.felt2, self.felt3, self.felt4, self.felt5, self.felt6, self.felt7, self.felt8, self.felt9]
