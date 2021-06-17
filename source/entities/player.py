from source.levels.base.level import *


class Player(Entity):
    LIVES = 3
    COLLECTED_ROSES = 0

    def __init__(self, x, y, level_instance, images: dict, speed):
        super().__init__(x, y, level_instance, images, speed)
        self.start_ticking = True
        self.start_moving = False
        self.start_moving_down = False
        self.current_image = pygame.transform.scale2x(self.current_image)
        self.jump_key_released = True

    def handle_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if not self.fly_mode:
                    self.enable_gravity = True
                    self.can_jump = False
                self.jump_key_released = True
            if event.key == pygame.K_f:
                self.fly_mode = not self.fly_mode
                self.enable_gravity = not self.enable_gravity
            if event.key == pygame.K_g:
                if self.fly_mode:
                    self.ghost_mode = not self.ghost_mode

    def handle_input(self):
        self.move_x = 0
        self.move_y = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.move_x = -1
        elif keys[pygame.K_d]:
            self.move_x = 1
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
        self.move_x_axis(self.speed_x * self.move_x * delta_time)
        self.move_y_axis(self.jump_speed * self.move_y * delta_time)

    def tick(self, delta_time):
        pass

    def draw(self, renderer: pygame.Surface, camera: Camera):
        rect = self.current_image.get_rect(topleft=(self.x, self.y))
        if isinstance(camera, Camera):
            rect = camera.apply_rect(rect)
        renderer.blit(self.current_image, rect)
