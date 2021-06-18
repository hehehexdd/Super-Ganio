from source.engine.collision import *


class DeathBox(Box):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(None, rect, CollisionChannel.Entity)

    def on_collide(self, entity: Entity, new_pos: list):
        if not entity.is_dead():
            entity.kill()


class ObjectiveBox(Box):
    def __init__(self, entity, rect: pygame.rect.Rect):
        super().__init__(entity, rect, CollisionChannel.Player)

    def pre_collide(self, entity: Entity, new_pos: list):
        super(ObjectiveBox, self).pre_collide(entity, new_pos)
        return False

    def on_collide(self, entity: Entity, new_pos: list):
        entity.add_item_to_inventory(self.entity.items[0])
        self.entity.level_instance.collisions.remove(self)
        self.entity.level_instance.entities.remove(self.entity)

