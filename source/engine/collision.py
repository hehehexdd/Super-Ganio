import pygame
from source.entities.entity import *
from source.engine.collisionchannels import *


class Box:
    def __init__(self, rect: pygame.rect.Rect, collision_channel: CollisionChannel):
        self.rect = rect
        self.collision_channel = collision_channel

    def check_collides(self, entity: Entity, new_pos: list):
        if self.rect.colliderect(entity.current_image.get_rect(topleft=new_pos)):
            self.pre_collide(entity, new_pos)
            return True
        else:
            self.on_no_collision(entity, new_pos)
            return False

    def pre_collide(self, entity: Entity, new_pos: list):
        if self.collision_channel == CollisionChannel.Entity and (entity.collision_channel == CollisionChannel.Player or entity.collision_channel.Enemy):
            self.on_collide(entity, new_pos)
        elif self.collision_channel == entity.collision_channel:
            self.on_collide(entity, new_pos)

    def on_collide(self, entity: Entity, new_pos: list):
        pass

    def on_no_collision(self, entity: Entity, new_pos: list):
        pass
