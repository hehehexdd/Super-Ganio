from game_data.source.buttons.custombuttons import *
from game_data.source.levels.BaseLevel import *
from game_data.engine.levels.base.level import *
from game_data.engine.widgets.widget import *
import os


class MainMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)

        abs_path = os.path.dirname(os.path.abspath("assets"))
        abs_path = os.path.join(abs_path, 'game_data\\assets\\music\\Terraria Music - Day.mp3')
        self.game_instance.music.load(abs_path)
        self.game_instance.music.play(-1)
        self.game_instance.music.set_volume(0.2)

        screen_size = self.game_instance.window.get_window_size()

        main_menu_widget = Widget((screen_size[0] / 2, 250), 50, 100, "Super Ganio!", 80)
        play_menu_widget = Widget((self.game_instance.window.get_window_size()[0] / 2, 250), 50, 100, "Select a Level", 80)

        main_menu_widget.add_button(PlayButton(True, True, 'Play', 60, owner=self, custom_data=[play_menu_widget]))
        main_menu_widget.add_button(ExitButton(True, True, 'Exit', 60, owner=self))

        play_menu_widget.add_button(StartLevelButton(True, True, 'Level1', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level1/level.tmx")]))
        play_menu_widget.add_button(StartLevelButton(True, True, 'Level2', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level2/level.tmx")]))
        play_menu_widget.add_button(StartLevelButton(True, True, 'Level3', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level3/level.tmx")]))
        play_menu_widget.add_button(OpenFileBrowser(True, True, 'Load custom', 60, owner=self, custom_data=[BaseLevel(self.game_instance, ""), self.game_instance]))
        play_menu_widget.add_button(BackButtonWidget(True, True, 'Back', 60, owner=self, custom_data=[main_menu_widget]))

        self.background_color = (0, 100+50, 70+50)
        self.set_widget(main_menu_widget)
