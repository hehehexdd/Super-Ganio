from game_data.source.buttons.backbutton import BackButton
from game_data.source.buttons.backbuttonmethod import BackButtonMethod
from engine.entities.player import Player
import pygame
from engine.widgets.widget import Widget


class Ganio(Player):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images)
        size = self.level_instance.game_instance.window.get_window_size()
        menu_widget = Widget((size[0] / 2, size[1] / 2), 50, 40)
        menu_widget.add_button(BackButtonMethod(True, True, 'Back to Main Menu', 60, owner=self.level_instance, custom_data=[self.level_instance.game_instance.restart]))
        self.level_instance.last_widget = menu_widget

    def handle_events(self, event):
        super(Ganio, self).handle_events(event)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if not self.is_dead():
                    self.toggle_menu()

    def toggle_menu(self):
        self.level_instance.set_widget(self.level_instance.last_widget)
        self.level_instance.game_instance.toggle_pause()

    def on_item_add_to_inventory(self):
        self.level_instance.check_win_condition()
