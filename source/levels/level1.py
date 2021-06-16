from source.levels.base.maplevel import *


class Level1(MapLevel):
    def __init__(self, instance):
        super().__init__(instance)
        self.create_map('./assets/levels/level1/level.tmx')
        image1 = pygame.image.load('./assets/images/player.png')
        images = [image1]
        self.player = Player(self.game_instance.window.get_window_size()[0] / 2,
                             self.game_instance.window.get_window_size()[1] / 2,
                             self,
                             images,
                             10,
                             self,
                             200,
                             self.game_instance.window.get_window_size()[0],
                             self.game_instance.window.get_window_size()[1])
