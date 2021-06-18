import pygame


class Camera:
    def __init__(self, width, height, window):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.window = window

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target_rect):
        x = -target_rect.centerx + int(self.window.get_window_size()[0] / 2)
        y = -target_rect.centery + int(self.window.get_window_size()[1] / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - self.window.get_window_size()[0]), x)  # right
        y = max(-(self.height - self.window.get_window_size()[1]), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)
