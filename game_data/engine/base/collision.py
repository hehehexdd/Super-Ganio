from game_data.engine.entities.base.entity import *
from game_data.engine.base.collisioninfo import *


class Box:
    def __init__(self, entity, rect: pygame.rect.Rect, self_collision_channels: dict, target_collision_channels: dict):
        self.rect = rect
        self.entity = entity
        self.self_collision_channels = self_collision_channels
        self.target_collision_channels = target_collision_channels
        self.should_skip = True

    def move(self, rect: pygame.Rect):
        self.rect = rect

    def pre_collide(self, entity: Entity, new_pos: list):
        if not self.entity == entity:
            for collision_key in self.self_collision_channels:
                for entity_collision_key in entity.collision.target_collision_channels:
                    if collision_key == entity_collision_key:
                        result = self.check_collides(entity, new_pos, ((collision_key, self.self_collision_channels[collision_key]),
                                                                      (entity_collision_key, entity.collision.target_collision_channels[entity_collision_key])))
                        if self.self_collision_channels[collision_key] == entity.collision.target_collision_channels[entity_collision_key]:
                            return result
        return False

    def check_collides(self, entity: Entity, new_pos: list, channel_infos):
        const = 2
        new_pos = (new_pos[0] - const, new_pos[1] - const)
        if self.rect.colliderect(entity.current_image.get_rect(topleft=new_pos)):
            self.on_collide(entity, new_pos, channel_infos)
            if channel_infos[0][1] == channel_infos[1][1] and channel_infos[0][1] == CollisionAction.Block:
                return True
            return False
        else:
            self.on_no_collision(entity, new_pos)
            return False

    def on_collide(self, entity: Entity, new_pos: list, channel_infos):
        pass

    def on_no_collision(self, entity: Entity, new_pos: list):
        pass
