from source.engine.collision import *
from source.entities.enemies import Enemy
from source.entities.player import Player


class DeathBox(Box):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(None, rect, list([CollisionChannel.Entity]))

    def on_collide(self, entity: Entity, new_pos: list, channel, should_skip):
        if not entity.is_dead():
            entity.kill()


class ObjectiveBox(Box):
    def __init__(self, entity, rect: pygame.rect.Rect):
        super().__init__(entity, rect, list([CollisionChannel.Player]))

    def on_collide(self, entity: Entity, new_pos: list, channel, should_skip):
        if channel == CollisionChannel.Player:
            if isinstance(entity, Player):
                self.entity.level_instance.collisions.remove(self)
                entity.add_item_to_inventory(self.entity.items[0])
                self.entity.level_instance.entities.remove(self.entity)


# class EnemyCollision(Box):
#     def __init__(self, entity, rect: pygame.rect.Rect, collision_channels: list):
#         super().__init__(entity, rect, collision_channels)
#
#     def pre_collide(self, entity: Entity, new_pos: list):
#         self.entity: Enemy
#
#
#
# class DamageBox(Box):
#     pass
