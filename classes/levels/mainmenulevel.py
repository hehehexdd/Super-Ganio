from classes.levels.base.level import *
from classes.buttons.base.button import *
from classes.buttons.playbutton import *
from classes.buttons.exitbutton import *


class MainMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)
        screen_size = self.gameInstance.window.get_window_size()
        widget = Widget((screen_size[0] / 2, screen_size[1] / 2), 20, 10, "Main menu")
        widget.add_button(PlayButton(True, True, 'Play', 20, owner=self))
        widget.add_button(ExitButton(True, True, 'Exit', 20, owner=self))
        self.set_widget(widget)
