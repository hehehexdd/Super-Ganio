from source.base.map import Map
from source.entities.player import *
from source.base.camera import *
import os
import pygame


class MapLevel(Level):
    def __init__(self, instance):
        super().__init__(instance)
        self.map = None
        self.surface = None

    def setup_assets(self, filename):
        self.map = Map(filename)
        self.surface = self.map.make_map()

        if self.map:
            self.collisions = []
            for object_tile in self.map.tmxdata.objects:
                if object_tile.name == 'collision':
                    self.collisions.append(pygame.rect.Rect(object_tile.x, object_tile.y, object_tile.width, object_tile.height))
                if object_tile.name == 'player':
                    # player_animations = MapLevel.setup_player_resources()
                    name = os.path.join(os.path.dirname(os.path.abspath("player.png")), 'assets\\images\\player\\player.png')
                    player_images = {
                        "idle": [pygame.image.load(name)]
                    }
                    #     "idle": player_animations[0],
                    #     "jump": player_animations[1],
                    #     "move": player_animations[2]
                    # }
                    self.camera = Camera(self.map.width, self.map.height, self.game_instance.window)
                    self.player = Player(object_tile.x, object_tile.y, self, player_images, 20, 200)
                    print(object_tile.x, object_tile.y)

    @staticmethod
    def setup_player_resources():
        idle_anims = []
        dir_name = os.path.dirname(os.path.abspath("player.png"))
        player_anim_path = os.path.join(dir_name, 'assets/images/player')
        idle_anim_path = os.path.join(player_anim_path, "idle")
        idle_anim_files = os.listdir(idle_anim_path)
        for file in idle_anim_files:
            idle_anims.append(pygame.image.load(os.path.join(idle_anim_path, file)))

        jump_anims = []
        jump_anim_path = os.path.join(player_anim_path, "jump")
        jump_anim_files = os.listdir(jump_anim_path)
        for file in jump_anim_files:
            jump_anims.append(pygame.image.load(os.path.join(jump_anim_path, file)))

        move_anims = []
        move_anim_path = os.path.join(player_anim_path, "move")
        move_anim_files = os.listdir(move_anim_path)
        for file in move_anim_files:
            move_anims.append(pygame.image.load(os.path.join(move_anim_path, file)))

        return [idle_anims, jump_anims, move_anims]

    def post_handle_events(self, event: pygame.event.Event):
        if self.player:
            self.player.handle_events(event)

    def hidden_tick(self, delta_time):
        pass

    def draw(self, renderer):
        if self.camera:
            self.camera.update(self.player.current_image.get_rect(topleft=(self.player.x, self.player.y)))
        if self.map:
            surface_rect = self.surface.get_rect()
            if self.camera:
                surface_rect = self.camera.apply_rect(surface_rect)
            renderer.blit(self.surface, surface_rect)
        for entity in self.entities:
            entity.draw(renderer, self.camera)
        if self.player:
            self.player.draw(renderer, self.camera)
