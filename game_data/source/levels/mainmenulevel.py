from game_data.source.buttons.exitbutton import *
from game_data.source.buttons.playbutton import *
from game_data.source.buttons.startlevelbutton import *
from game_data.source.levels.BaseLevel import BaseLevel
from game_data.engine.levels.base.level import Level
from game_data.engine.widgets.widget import Widget


class MainMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)

        screen_size = self.game_instance.window.get_window_size()

        widget = Widget((screen_size[0] / 2, 250), 50, 40, "Super Ganio!", 100)
        widget1 = Widget((self.game_instance.window.get_window_size()[0] / 2, 250), 50, 40, "Select a map", 100)

        widget.add_button(PlayButton(True, True, 'Play', 60, owner=self, custom_data=[widget1]))
        widget.add_button(ExitButton(True, True, 'Exit', 60, owner=self))

        widget1.add_button(StartLevelButton(True, True, 'Level1', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level1/level.tmx")]))
        widget1.add_button(StartLevelButton(True, True, 'Level2', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level2/level.tmx")]))
        from game_data.source.buttons.backbuttonwidget import BackButtonWidget
        widget1.add_button(BackButtonWidget(True, True, 'Back', 60, owner=self, custom_data=[widget]))

        self.background_color = (0, 100+50, 70+50)
        self.set_widget(widget)
