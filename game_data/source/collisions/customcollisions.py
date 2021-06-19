from game_data.engine.base.collision import *
from game_data.engine.entities.player import Player


class DeathBox(Box):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(None, rect, {CollisionChannel.Death: CollisionAction.Pass}, {})

    def on_collide(self, entity: Entity, new_pos: list, channel):
        if not entity.is_dead():
            entity.kill()


class ObjectiveBox(Box):
    def __init__(self, entity, rect: pygame.rect.Rect):
        super().__init__(entity, rect, {CollisionChannel.Objective: CollisionAction.Pass}, {})

    def on_collide(self, entity: Entity, new_pos: list, channel):
        if isinstance(entity, Player):
            self.entity.level_instance.collisions.remove(self)
            entity.add_item_to_inventory(self.entity.items[0])
            self.entity.level_instance.entities.remove(self.entity)


class EnemyDamageBox(Box):
    def __init__(self, entity, rect: pygame.rect.Rect, self_collision_channels: dict, target_collision_channels: dict):
        self_collision_channels[CollisionChannel.Damage] = CollisionAction.Pass
        super().__init__(entity, rect, self_collision_channels, target_collision_channels)

    def on_collide(self, entity: Entity, new_pos: list, channel):
        entity: Player
        const = 10.0
        if entity.collision.rect.bottom < self.rect.top + self.rect.height / 4:
            self.entity.hit()
            entity.add_force(100)
        else:
            entity.hit()
