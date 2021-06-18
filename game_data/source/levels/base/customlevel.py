from source.levels.base.maplevel import *
from game_data.source.entities.ganio_player import *


class CustomLevel(MapLevel):
    def __init__(self, instance, level_path):
        super().__init__(instance)

        # player_animations = MapLevel.setup_player_resources()
        name = os.path.join(os.path.dirname(os.path.abspath("player.png")),
                            'game_data\\assets\\images\\player\\player.png')
        player_images = {
            "idle": [pygame.image.load(name)]
        }
        #     "idle": player_animations[0],
        #     "jump": player_animations[1],
        #     "move": player_animations[2]
        # }

        self.setup_assets(level_path, Ganio(1, 0, 0, self, player_images))

    @staticmethod
    def setup_player_resources():
        idle_anims = []
        dir_name = os.path.dirname(os.path.abspath("player.png"))
        player_anim_path = os.path.join(dir_name, 'assets/images/player')
        idle_anim_path = os.path.join(player_anim_path, "idle")
        idle_anim_files = os.listdir(idle_anim_path)
        for file in idle_anim_files:
            idle_anims.append(pygame.image.load(os.path.join(idle_anim_path, file)))

        jump_anims = []
        jump_anim_path = os.path.join(player_anim_path, "jump")
        jump_anim_files = os.listdir(jump_anim_path)
        for file in jump_anim_files:
            jump_anims.append(pygame.image.load(os.path.join(jump_anim_path, file)))

        move_anims = []
        move_anim_path = os.path.join(player_anim_path, "move")
        move_anim_files = os.listdir(move_anim_path)
        for file in move_anim_files:
            move_anims.append(pygame.image.load(os.path.join(move_anim_path, file)))

        return [idle_anims, jump_anims, move_anims]

    def check_win_condition(self):
        pass
