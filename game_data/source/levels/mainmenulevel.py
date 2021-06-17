from game_data.source.buttons.exitbutton import *
from game_data.source.buttons.playbutton import *
from game_data.source.buttons.startlevelbutton import *
from game_data.source.levels.level1 import Level1
from source.levels.base.level import Level
from source.widgets.widget import Widget


class MainMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)

        screen_size = self.game_instance.window.get_window_size()

        widget = Widget((screen_size[0] / 2, 250), 50, 40, "Super Ganio!", 100)
        widget1 = Widget((self.game_instance.window.get_window_size()[0] / 2, 250), 50, 40, "Select a map", 100)

        widget.add_button(PlayButton(True, True, 'Play', 60, owner=self, custom_data=[widget1]))
        widget.add_button(ExitButton(True, True, 'Exit', 60, owner=self))

        widget1.add_button(StartLevelButton(True, True, 'Level1', 60, owner=self, custom_data=[Level1(self.game_instance)]))
        from game_data.source.buttons.backbuttonwidget import BackButtonWidget
        widget1.add_button(BackButtonWidget(True, True, 'Back', 60, owner=self, custom_data=[widget]))

        self.background_color = (0, 100+50, 70+50)
        self.set_widget(widget)