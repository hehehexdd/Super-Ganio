from game_data.source.buttons.custombuttons import BackButtonMethod
from game_data.engine.entities.player import Player
import pygame
from game_data.engine.widgets.widget import Widget


class Ganio(Player):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images)
        size = self.level_instance.game_instance.window.get_window_size()
        self.menu_widget = Widget((size[0] / 2, size[1] / 2), 50, 40)
        self.menu_widget.add_button(BackButtonMethod(True, True, 'Back to Main Menu', 60, owner=self.level_instance, custom_data=[self.level_instance.game_instance.restart]))
        self.menu_widget_set = False

    def handle_events(self, event):
        super(Ganio, self).handle_events(event)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if not self.is_dead():
                    self.toggle_menu()

    def toggle_menu(self):
        if self.menu_widget_set:
            self.level_instance.clear_widgets()
        else:
            self.level_instance.set_widget(self.menu_widget)
        self.menu_widget_set = not self.menu_widget_set
        self.level_instance.game_instance.toggle_pause()

    def on_item_add_to_inventory(self):
        self.level_instance.check_win_condition()
        if self.get_num_of_items_of_name('rose') % 3 == 0:
            if self.hp + 1 <= self.max_lives:
                self.hp += 1
