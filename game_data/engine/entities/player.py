from game_data.engine.base.collision import *
from game_data.engine.levels.base.level import *
from game_data.engine.base.collisioninfo import *
import time


class Player(Entity):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images, images['idle'], 300)
        self.scale_all_images_by(2)
        self.jump_key_released = True
        self.collision = Box(self, self.current_image.get_rect(), {CollisionChannel.Entity: CollisionAction.Pass},
                             {CollisionChannel.Death: CollisionAction.Pass, CollisionChannel.Objective: CollisionAction.Pass, CollisionChannel.Damage: CollisionAction.Pass,CollisionChannel.World: CollisionAction.Block})
        self.level_instance.collisions.append(self.collision)
        self.dev_mode_collision = Box(self, self.current_image.get_rect(), {CollisionChannel.Entity: CollisionAction.Pass},
                                      {CollisionChannel.Death: CollisionAction.Pass, CollisionChannel.Objective: CollisionAction.Pass, CollisionChannel.World: CollisionAction.Pass})
        self.can_use_space = True
        self.force_added = False

    def handle_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and self.can_use_space:
                if not self.fly_mode:
                    self.enable_gravity = True
                    self.can_jump = False
                self.jump_key_released = True
            # dev mode
            if not self.level_instance.game_instance.paused:
                if event.key == pygame.K_f:
                    self.fly_mode = not self.fly_mode
                    self.enable_gravity = not self.enable_gravity
                if event.key == pygame.K_g:
                    if self.fly_mode:
                        self.toggle_collision()
                if event.key == pygame.K_q:
                    self.god_mode = not self.god_mode

    def toggle_collision(self):
        temp = self.collision
        self.collision = self.dev_mode_collision
        self.dev_mode_collision = temp

    def handle_input(self):
        self.move_x = 0
        if self.can_use_space:
            self.move_y = 0
        self.switch_current_image_set('idle')
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move_x = -1
            self.switch_current_image_set('move')
            self.flip_all_images(False)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move_x = 1
            self.switch_current_image_set('move')
            self.flip_all_images(True)
        if self.fly_mode:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.move_y = -1
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.move_y = 1
        if keys[pygame.K_SPACE] and self.can_use_space:
            if not self.fly_mode:
                self.jump_key_released = False
                self.calc_jump_point()
                self.jump()
                if not self.is_on_ground:
                    self.switch_current_image_set('jump')
            else:
                self.move_y = -1

    def add_force(self, value):
        self.can_calc_jump_point = False
        self.force_added = True
        self.can_use_space = False
        self.max_jump_pos_y = (value * -1) + self.y
        self.can_jump = True
        self.jump()

    def check_can_jump_again(self):
        if self.is_on_ground and self.jump_key_released:
            self.can_jump = True

    def tick(self, delta_time):
        self.check_can_jump_again()
        self.handle_input()
        super(Player, self).tick(delta_time)
        self.added_force_check(delta_time)

    def added_force_check(self, delta_time):
        if self.force_added:
            if self.is_on_ground:
                self.force_added = False
                self.can_jump = True
                self.can_use_space = True
                self.can_calc_jump_point = True
            
    def kill(self):
        if not self.god_mode:
            super(Player, self).kill()
            self.level_instance.game_instance.toggle_pause()
            pos = self.level_instance.game_instance.window.get_window_size()
            widget = Widget((pos[0] / 2, pos[1] / 2), title_text="You died.", text_size=50, text_color=(255, 0, 0))
            self.level_instance.set_widget(widget)
            self.level_instance.game_instance.set_timer(self.level_instance.game_instance.restart, 1)
