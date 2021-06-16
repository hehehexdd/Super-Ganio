from source.levels.base.level import *


class Player(Entity):
    LIVES = 3
    COLLECTED_ROSES = 0

    def __init__(self, x, y, level_instance, images: dict, jump_max_height, speed):
        super().__init__(x, y, level_instance, images, jump_max_height)
        self.speed = speed
        self.start_ticking = True
        self.start_moving = False
        self.start_moving_down = False
        self.move_x = 0
        self.move_y = 0

    def move(self, value):
        new_pos = value
        self.x += new_pos

    def move_down(self, value):
        new_pos = value
        self.y += new_pos

    def handle_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass

    def handle_input(self):
        self.move_x = 0
        self.move_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move_x = -1
        elif keys[pygame.K_d]:
            self.move_x = 1
        elif keys[pygame.K_w]:
            self.move_y = -1
        elif keys[pygame.K_s]:
            self.move_y = 1
        elif keys[pygame.K_SPACE]:
            pass

    def tick(self, delta_time):
        self.handle_input()
        self.move(self.speed * self.move_x * delta_time)
        self.move_down(self.speed * self.move_y * delta_time)

    def draw(self, renderer: pygame.Surface, camera: Camera):
        rect = self.current_image.get_rect(topleft=(self.x, self.y))
        if isinstance(camera, Camera):
            rect = camera.apply_rect(rect)
        renderer.blit(self.current_image, rect)
