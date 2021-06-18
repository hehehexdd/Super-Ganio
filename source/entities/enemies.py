from source.engine.collision import Box
from source.entities.base.entity import *


class Enemy(Entity):
	def __init__(self, hp, x, y, level_instance, images: dict, speed_x):
		super().__init__(hp, x, y, level_instance, images, speed_x)
		self.collision = Box(self.current_image.get_rect(), CollisionChannel.Enemy)


class Rat(Enemy):
	pass


class EnglishMan(Enemy):
	pass


class Chicken(Enemy):
	pass
