import pygame
import pytmx
import pyscroll
from player import Player
import Data.settings.setting as setting
import Data.data as data
from map import MapManager


class Game:
    def __init__(self):
        
        # creer la fenetre du jeu 
        self.screen = pygame.display.set_mode((data.display_x, data.display_y))
        pygame.display.set_caption(data.game_name)   

        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")

    def update(self):
        self.map_manager.update()



    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu 
        running = True


        while running:

            self.update()
            self.move()
            self.map_manager.draw()
            self.map_manager.check_collision()
            self.player.save_location()
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(setting.FPS)

        pygame.quit()