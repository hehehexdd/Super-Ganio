from game_data.engine.widgets.widget import *
from game_data.engine.entities.base.entity import *
import pygame
import os


class Level:
    def __init__(self, instance: object):
        self.collisions = []
        self.entities = []
        self.player = None
        self.camera = None
        self.current_widget = None
        self.last_widget = None
        self.game_instance = instance
        self.background_color = (0, 0, 0, 255)

    def handle_events(self, event: pygame.event.Event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if self.current_widget is not None:
                self.current_widget.handle_event(ButtonEvent.Hover, mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_widget is not None:
                self.current_widget.handle_event(ButtonEvent.Click, mouse_pos)
        if self.player:
            self.player.handle_events(event)

    def tick(self, delta_time):
        if not self.game_instance.paused:
            for entity in self.entities:
                if entity.start_ticking:
                    entity.animate()
                    entity.tick(delta_time)
                    entity.apply_physics(delta_time)
            if self.player:
                if self.player.start_ticking:
                    self.player.animate()
                    self.player.tick(delta_time)
                    self.player.apply_physics(delta_time)

    def draw(self, renderer):
        pass

    def post_draw(self, renderer):
        self.draw(renderer)

        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def check_collides_any(self, entity: Entity, pos: list):
        rect = entity.current_image.get_rect(topleft=(pos[0], pos[1]))
        for collision in self.collisions:
            if collision.pre_collide(entity, pos):
                return True

        if self.player:
            if rect.left < 0:
                return True
            elif rect.top < 0:
                return True
            elif rect.right > self.map.width:
                return True
            elif rect.bottom > self.map.height:
                return True
        return False

    def set_widget(self, widget: Widget):
        self.last_widget = self.current_widget
        self.current_widget = widget

    def remove_widget(self):
        self.current_widget = None

