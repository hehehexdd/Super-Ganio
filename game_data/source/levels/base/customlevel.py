from game_data.engine.levels.base.maplevel import *


class CustomLevel(MapLevel):
    def __init__(self, instance, level_path):
        super().__init__(instance)

    def check_win_condition(self):
        pass
