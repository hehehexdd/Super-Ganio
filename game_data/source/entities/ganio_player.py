from game_data.source.levels.base.customlevel import *


class Ganio(Player):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images)

    def on_item_add_to_inventory(self):
        if isinstance(self.level_instance, CustomLevel):
            self.level_instance.check_win_condition()