from classes.levels.base.level import *
from classes.buttons.backbutton import *


class PlayMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)
        screen_size = self.gameInstance.window.get_window_size()
        back_button = BackButton(True, True, 'Back', 20, position=(screen_size[0]/2, screen_size[1]/2), owner=self)
        self.buttons.append(back_button)