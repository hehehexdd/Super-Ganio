# got this from github by ChristianD37
import pygame
import pygame.camera
from abc import ABC, abstractmethod
vec = pygame.math.Vector2


class Camera:
    def __init__(self, player, screen_width, screen_height):
        self.player = player
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)
        self.screen_width, self.screen_height = screen_width, screen_height
        self.const = vec(-self.screen_width / 2 + self.player.current_image.get_rect().width / 2, -screen_height / 2 + self.player.current_image.get_rect().height / 2) #- self.player.ground_y + 20)
        self.method = None

    def set_method(self, method):
        self.method = method

    def move(self):
        self.method.move()


class CamScroll(ABC):
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def move(self):
        pass


class Follow(CamScroll):
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)

    def move(self):
        self.camera.offset_float.x += (self.player.x - self.camera.offset_float.x + self.camera.const.x)
        self.camera.offset_float.y += (self.player.y - self.camera.offset_float.y + self.camera.const.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
