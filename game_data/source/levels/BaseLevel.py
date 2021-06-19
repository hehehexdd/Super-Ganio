from game_data.source.entities.objectives import *
from game_data.source.levels.base.customlevel import *
from game_data.source.entities.ganio_player import *
from game_data.engine.base.collision import *
from game_data.engine.entities.enemies import *
from game_data.engine.widgets.widget import *


class BaseLevel(CustomLevel):
    def __init__(self, instance, level_path):
        super().__init__(instance, level_path)
        self.roses_to_collect = 0
        self.level_path = level_path
        self.setup_assets(level_path, Ganio(1, 0, 0, self, BaseLevel.setup_resources('player')))

    def setup_assets(self, filename, player):
        super(BaseLevel, self).setup_assets(filename, player)

        for object_tile in self.map.tmxdata.objects:
            # spawn objective and enemies
            if object_tile.type == 'collision':
                if object_tile.name == "rose":
                    self.entities.append(Rose(1, object_tile.x, object_tile.y, self, BaseLevel.setup_resources('rose')))
                    self.roses_to_collect += 1
                if object_tile.name == "enemy":
                    self.collisions.append(Box(None, pygame.rect.Rect(object_tile.x, object_tile.y, object_tile.width, object_tile.height), {CollisionChannel.EnemyObstacle: CollisionAction.Block}, {}))
            elif object_tile.type == 'enemy':
                if object_tile.name == 'englishman':
                    self.entities.append(Enemy(2, object_tile.x, object_tile.y, self, BaseLevel.setup_resources('englishman'), 80, -1))
                elif object_tile.name == 'rat':
                    self.entities.append(Enemy(1, object_tile.x, object_tile.y, self, BaseLevel.setup_resources('rat'), 300, -1))
                elif object_tile.name == 'chicken':
                    self.entities.append(Enemy(1, object_tile.x, object_tile.y, self, BaseLevel.setup_resources('chicken'), 150, -1))

    @staticmethod
    def setup_resources(entity_name):
        idle_anims = []
        dir_name = os.path.dirname(os.path.abspath("assets"))
        assets_path = os.path.join('game_data', 'assets')
        images_path = os.path.join(assets_path, 'images')
        anim_path = os.path.join(dir_name, os.path.join(images_path, entity_name))
        idle_anim_path = os.path.join(anim_path, "idle")

        if os.path.exists(idle_anim_path):
            idle_anim_files = os.listdir(idle_anim_path)
            for file in idle_anim_files:
                idle_anims.append(pygame.image.load(os.path.join(idle_anim_path, file)))

        jump_anims = []
        jump_anim_path = os.path.join(anim_path, "jump")
        if os.path.exists(jump_anim_path):
            jump_anim_files = os.listdir(jump_anim_path)
            for file in jump_anim_files:
                jump_anims.append(pygame.image.load(os.path.join(jump_anim_path, file)))

        move_anims = []
        move_anim_path = os.path.join(anim_path, "move")
        if os.path.exists(move_anim_path):
            move_anim_files = os.listdir(move_anim_path)
            for file in move_anim_files:
                move_anims.append(pygame.image.load(os.path.join(move_anim_path, file)))

        return {'idle': idle_anims, 'jump': jump_anims, 'move': move_anims}

    def check_win_condition(self):
        if self.player.get_num_of_items_of_name('rose') >= self.roses_to_collect:
            self.win()

    def win(self):
        self.game_instance.toggle_pause()
        pos = self.game_instance.window.get_window_size()
        widget = Widget((pos[0] / 2, pos[1] / 2), title_text="You won!", text_size=50, text_color=(255, 0, 0))
        self.set_widget(widget)
        self.game_instance.set_timer(self.game_instance.restart, 1)
