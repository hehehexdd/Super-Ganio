from game_data.source.collisions.customcollisions import ObjectiveBox
from source.items.item import Item
from source.entities.base.entity import Entity, CollisionChannel
import pygame


class Rose(Entity):
    def __init__(self, hp, x, y, level_instance, images: dict, speed_x):
        super().__init__(hp, x, y, level_instance, images, speed_x)
        self.start_ticking = False
        self.items.append(Item('rose'))
        self.current_image = pygame.transform.scale2x(self.current_image)
        self.collision = ObjectiveBox(self, self.current_image.get_rect(topleft=(self.x, self.y)))
        self.level_instance.collisions.append(self.collision)


