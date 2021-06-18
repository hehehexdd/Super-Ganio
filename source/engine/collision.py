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
            for collision in self.collision_channels:
                for entity_collision in entity.collision.collision_channels:
                    if collision == entity_collision:
                        should_skip = False
                        result = self.check_collides(entity, new_pos, entity_collision, should_skip)
                        if not should_skip:
                            return result
                    elif entity_collision <= CollisionChannel.World:
                        should_skip = False
                        result = self.check_collides(entity, new_pos, entity_collision, should_skip)
                        if not should_skip:
                            return result

    def check_collides(self, entity: Entity, new_pos: list, channel, should_skip):
        if self.rect.colliderect(entity.current_image.get_rect(topleft=new_pos)):
            self.on_collide(entity, new_pos, channel, should_skip)
            if not should_skip:
                return True
            return False
        else:
            self.on_no_collision(entity, new_pos, should_skip)
            return False

    def on_collide(self, entity: Entity, new_pos: list, channel, should_skip):
        if channel <= CollisionChannel.World:
            should_skip = False

    def on_no_collision(self, entity: Entity, new_pos: list, should_skip):
        should_skip = False
