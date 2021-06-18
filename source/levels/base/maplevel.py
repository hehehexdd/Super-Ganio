from game_data.source.collisions.customcollisions import *
from source.engine.map import Map
from source.entities.player import *
from source.engine.camera import *
import os
import pygame


class MapLevel(Level):
    def __init__(self, instance):
        super().__init__(instance)
        self.map = None
        self.surface = None

    def setup_assets(self, filename, player):
        self.map = Map(filename)
        self.surface = self.map.make_map()
        self.player = player

        if self.map:
            self.collisions = []
            for object_tile in self.map.tmxdata.objects:
                if object_tile.type == 'collision':
                    if object_tile.name == 'death':
                        self.collisions.append(DeathBox(pygame.rect.Rect(object_tile.x, object_tile.y, object_tile.width, object_tile.height)))
                    elif object_tile.name == 'player':
                        self.camera = Camera(self.map.width, self.map.height, self.game_instance.window)
                        self.player.x = object_tile.x
                        self.player.y = object_tile.y
                    elif not object_tile.name:
                        self.collisions.append(Box(None, pygame.rect.Rect(object_tile.x, object_tile.y, object_tile.width, object_tile.height), [CollisionChannel.World]))

    def draw(self, renderer):
        if self.camera:
            self.camera.update(self.player.current_image.get_rect(topleft=(self.player.x, self.player.y)))
        if self.map:
            surface_rect = self.surface.get_rect()
            if self.camera:
                surface_rect = self.camera.apply_rect(surface_rect)
            renderer.blit(self.surface, surface_rect)
        for entity in self.entities:
            entity.draw(renderer, self.camera)
        if self.player:
            self.player.draw(renderer, self.camera)
