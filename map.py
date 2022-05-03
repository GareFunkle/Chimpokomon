from dataclasses import dataclass
import pygame
import pytmx
import pyscroll
from walls import Walls


@dataclass
class Map:
    name: str
    walls: list([pygame.Rect])
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap


class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.screen = screen
        self.current_map = "map"
        self.player = player
        self.mur = Walls()
        
        self.register_map("map")
        self.teleport_player("player")


    def check_collision(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                print(True)
                sprite.move_back()
                self.player.save_location()
            else:
                print(False)
                

    def draw_collision(self):
        for collision in self.get_walls():
            pygame.draw.rect(self.screen, (64, 64, 64, 0), collision)


    # positionne mon joueur a la position choisie sur tiled
    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[1] = point.y
        self.player.position[0] = point.x
        self.player.save_location()

    def register_map(self, name):
        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(f"tiled/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())
        map_layer.zoom = 2

        # definir une liste qui va stocker mes collision
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(
                    obj.x, obj.y, obj.width, obj.height))


 
        # dessiner ke groupe de calques
        group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3)
        group.add(self.player)

        # creer un objet map
        self.maps[name] = Map(name, walls, group, tmx_data)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls

    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
        # self.draw_collision()

    def update(self):
        self.get_group().update()
        # self.check_collision()
        
        
