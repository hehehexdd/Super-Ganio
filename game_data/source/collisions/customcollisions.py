from source.engine.collision import *


class DeathBox(Box):
    def __init__(self, rect: pygame.rect.Rect, collision_channel: CollisionChannel):
        super().__init__(rect, collision_channel)

    def on_collide(self, entity: Entity, new_pos: list):
        if not entity.is_dead():
            entity.kill()
