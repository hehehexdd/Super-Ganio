from source.engine.collision import Box
from source.entities.base.entity import *
import pygame


class Enemy(Entity):
	def __init__(self, hp, x, y, level_instance, images: dict, speed_x, initial_move_dir: int):
		super().__init__(hp, x, y, level_instance, images, speed_x)
		self.current_image = pygame.transform.scale2x(self.current_image)
		self.collision = Box(self, self.current_image.get_rect(), CollisionChannel.Enemy)
		self.level_instance.collisions.append(self.collision)
		self.move_x = initial_move_dir

	def kill(self):
		super(Enemy, self).kill()
		self.level_instance.collisions.remove(self.collision)
		self.level_instance.entities.remove(self)