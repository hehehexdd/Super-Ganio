from source.levels.base.maplevel import *


class Level1(MapLevel):
    def __init__(self, instance):
        super().__init__(instance)
        self.setup_assets('./game_data/assets/levels/level2/level.tmx')
