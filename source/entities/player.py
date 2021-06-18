from source.engine.collision import Box
from source.levels.base.level import *


class Player(Entity):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images, 300)
        self.current_image = pygame.transform.scale2x(self.current_image)
        self.jump_key_released = True
        self.collision = Box(self, self.current_image.get_rect(), CollisionChannel.Player)

    def handle_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
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
                        self.ghost_mode = not self.ghost_mode
                if event.key == pygame.K_q:
                    self.god_mode = not self.god_mode

    def handle_input(self):
        self.move_x = 0
        self.move_y = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.move_x = -1
            self.flip_all_images(False)
        elif keys[pygame.K_d]:
            self.move_x = 1
            self.flip_all_images(True)
        if self.fly_mode:
            if keys[pygame.K_w]:
                self.move_y = -1
            elif keys[pygame.K_s]:
                self.move_y = 1
        if keys[pygame.K_SPACE]:
            if not self.fly_mode:
                self.jump_key_released = False
                self.calc_jump_point()
                self.jump()
            else:
                self.move_y = -1

    def check_can_jump_again(self):
        if self.is_on_ground and self.jump_key_released:
            self.can_jump = True

    def hidden_tick(self, delta_time):
        self.check_can_jump_again()
        self.handle_input()
        super(Player, self).hidden_tick(delta_time)

    def tick(self, delta_time):
        pass

    def draw(self, renderer: pygame.Surface, camera: Camera):
        rect = self.current_image.get_rect(topleft=(self.x, self.y))
        if isinstance(camera, Camera):
            rect = camera.apply_rect(rect)
        renderer.blit(self.current_image, rect)

    def kill(self):
        if not self.god_mode:
            super(Player, self).kill()
            pos = self.level_instance.game_instance.window.get_window_size()
            widget = Widget((pos[0] / 2, pos[1] / 2), title_text="You died.", text_size=50, text_color=(255, 0, 0))
            self.level_instance.set_widget(widget)
            self.level_instance.game_instance.set_timer(self.level_instance.game_instance.restart, 1)