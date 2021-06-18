from source.engine.collision import *
from source.items.item import *


class DeathBox(Box):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(None, rect, CollisionChannel.Entity)

    def on_collide(self, entity: Entity, new_pos: list):
        if not entity.is_dead():
            entity.kill()


class ObjectiveBox(Box):
    def __init__(self, entity, rect: pygame.rect.Rect):
        super().__init__(entity, rect, CollisionChannel.Player)

    def on_collide(self, entity: Entity, new_pos: list):
        entity.add_item_to_inventory(Item('rose'))
        self.entity.level_instance.entities.remove(self.entity)

