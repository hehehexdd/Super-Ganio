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

    def handle_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.enable_gravity = True
                self.can_jump = False
            if event.key == pygame.K_ESCAPE:
                self.debug_mode = not self.debug_mode
                self.enable_gravity = not self.enable_gravity

    def handle_input(self):
        self.move_x = 0
        self.move_y = 0
        keys = pygame.key.get_pressed()
        keys_hold = pygame.key.get_repeat()

        if keys[pygame.K_a]:
            self.move_x = -1
        elif keys[pygame.K_d]:
            self.move_x = 1
        if self.debug_mode:
            if keys[pygame.K_w]:
                self.move_y = -1
            elif keys[pygame.K_s]:
                self.move_y = 1
        if keys[pygame.K_SPACE]:
            self.calc_jump_point()
            self.jump()

    def hidden_tick(self, delta_time):
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
