import pygame
from classes.entities.base.Entity import *


class Player(Entity):

	LIVES = 3
	COLLECTED_ROSES = 0
	#SPRITES = player_sprites

	def __init__(self, x, y, level_instance, jump_max_height, sprites):
		super().__init__(self, x, y, level_instance, jump_max_height, sprites)
		self.speed = 2.4

	def move(self, value):
		self.level_instance.move_assets(value)

	def jump(self):
		pass

	def tick(self, delta_time):
		pass

	def handle_events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				self.move(self.speed)
			elif event.key == pygame.K_d:
				self.move(self.speed * (-1))
			elif event.key == pygame.K_SPACE:
				self.calc_jump_point()
				self.jump()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				#TODO self.reset_jump()