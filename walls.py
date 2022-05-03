import pygame


class Walls(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 801, 31)
        self.rect2 = pygame.Rect(768, 31, 32, 769)
        self.rect3 = pygame.Rect(0, 769, 768, 30)
        self.rect4 = pygame.Rect(0, 31, 32, 737)   
        self.rect5 = pygame.Rect(447, 736, 64, 31)
        self.rect6 = pygame.Rect(448, 368, 63, 302)
        self.rect7 = pygame.Rect(320, 368, 127, 47)
        self.rect8 = pygame.Rect(320, 258, 63, 110)
        self.rect9 = pygame.Rect(320, 31, 63, 158)
        self.rect10 = pygame.Rect(32, 560, 61, 48)
        self.rect11 = pygame.Rect(162, 560, 286, 47)
        




# [<rect(0, 0, 801, 31)>, 1
# <rect(768, 31, 32, 769)>, 2
# <rect(0, 769, 768, 30)>, 3
# <rect(0, 31, 32, 737)>, 4
# <rect(447, 736, 64, 31)>, 5
# <rect(448, 368, 63, 302)>, 6
# <rect(320, 368, 127, 47)>, 7
# <rect(320, 258, 63, 110)>, 8
# <rect(320, 31, 63, 158)>, 9
# <rect(32, 560, 61, 48)>, 10
# <rect(162, 560, 286, 47)>] 11