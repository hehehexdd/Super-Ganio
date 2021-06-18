from source.entities.base.entity import *
from source.engine.collisionchannels import *


class Box:
    def __init__(self, entity, rect: pygame.rect.Rect, collision_channel: CollisionChannel):
        self.rect = rect
        self.entity = entity
        self.collision_channel = collision_channel

    def move(self, rect: pygame.Rect):
        self.rect = rect

    def pre_collide(self, entity: Entity, new_pos: list):
        if self.collision_channel == entity.collision.rect:
            return self.check_collides(entity, new_pos)
        elif entity.collision.collision_channel < CollisionChannel.Entity:
            return self.check_collides(entity, new_pos)

    def check_collides(self, entity: Entity, new_pos: list):
        if self.rect.colliderect(entity.current_image.get_rect(topleft=new_pos)):
            self.on_collide(entity, new_pos)
            return True
        else:
            self.on_no_collision(entity, new_pos)
            return False

    def on_collide(self, entity: Entity, new_pos: list):
        pass

    def on_no_collision(self, entity: Entity, new_pos: list):
        pass
