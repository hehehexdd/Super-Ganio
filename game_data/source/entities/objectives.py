from game_data.source.collisions.customcollisions import ObjectiveBox
from engine.items.item import Item
from engine.entities.base.entity import Entity, CollisionChannel
import pygame


class Rose(Entity):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images, images['idle'], 0)
        self.start_ticking = True
        self.enable_gravity = False
        self.can_jump = False
        self.items.append(Item('rose'))
        self.collision = ObjectiveBox(self, self.current_image.get_rect(topleft=(self.x, self.y)))
        self.level_instance.collisions.append(self.collision)

    def tick(self, delta_time):
        super(Rose, self).tick(delta_time)
