from classes.levels.base.level import *
from classes.buttons.base.button import *
from classes.buttons.playbutton import *


class MainMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)
        screen_size = self.gameInstance.window.get_window_size()
        quit_button = PlayButton(True, True, 'Play', 20, position=(screen_size[0]/2, screen_size[1]/2), owner=self)
        self.buttons.append(quit_button)
