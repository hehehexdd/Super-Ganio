from source.entities.base.entity import *
from source.engine.collisionchannels import *


class Box:
    def __init__(self, entity, rect: pygame.rect.Rect, collision_channels: list):
        self.rect = rect
        self.entity = entity
        self.collision_channels = collision_channels

    def move(self, rect: pygame.Rect):
        self.rect = rect

    def pre_collide(self, entity: Entity, new_pos: list):
        self.collision_channels: list
        if not self.entity == entity:
            for i in range(len(self.collision_channels)):
                for j in range(len(entity.collision.collision_channels)):
                    if self.collision_channels[i] == entity.collision.collision_channels[j]:
                        return self.check_collides(entity, new_pos, entity.collision.collision_channels[j])
                    elif self.collision_channels[i] <= CollisionChannel.World:
                        return self.check_collides(entity, new_pos, entity.collision.collision_channels[j])

    def check_collides(self, entity: Entity, new_pos: list, channel):
        if self.rect.colliderect(entity.current_image.get_rect(topleft=new_pos)):
            return self.on_collide(entity, new_pos, channel)
        else:
            return self.on_no_collision(entity, new_pos)

    def on_collide(self, entity: Entity, new_pos: list, channel):
        if channel <= CollisionChannel.World:
            return True
        return False

    def on_no_collision(self, entity: Entity, new_pos: list):
        return False
