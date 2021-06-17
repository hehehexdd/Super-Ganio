from source.entities.entity import *


class Enemy(Entity):
	def __init__(self, x, y, level_instance, sprites: list, jump_max_height):
		super().__init__(x, y, level_instance, sprites, jump_max_height)


class Rat(Enemy):
	pass


class EnglishMan(Enemy):
	pass


class Chicken(Enemy):
	pass
