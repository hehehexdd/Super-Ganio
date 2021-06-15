import pygame
from source.entities.base.entity import *
from source.entities.camera import Follow
from source.levels.base.level import *


class Player(Entity):

	LIVES = 3
	COLLECTED_ROSES = 0

	def __init__(self, x, y, level_instance, images: list, jump_max_height, owner: Level, speed, screen_width, screen_height):
		super().__init__(x, y, level_instance, images, jump_max_height, owner)
		self.camera = Camera(self, screen_width, screen_height)
		self.camera.set_method(Follow(self.camera, self))
		self.speed = speed
		self.start_ticking = True
		self.start_moving = False
		self.moving_direction = 1

	def move(self, value):
		if not self.owner.check_collides_any(self.current_image.get_rect(center=(self.x - self.camera.offset.x + value, self.y - self.camera.offset.y))):
			self.x += value * self.owner.game_instance.delta_time
			self.camera.move()

	def draw(self, renderer, camera: Camera):
		player_rect = self.current_image.get_rect(center=(self.x - self.camera.offset.x, self.y - self.camera.offset.y))
		player_center = player_rect.bottomright
		renderer.blit(self.current_image, player_center)

	def tick(self, delta_time):
		if self.start_moving:
			self.move(self.speed * self.moving_direction)
		print(self.x - self.camera.offset.x, self.y - self.camera.offset.y)
		pass

	def handle_events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				self.start_moving = True
				self.moving_direction = -1
			elif event.key == pygame.K_d:
				self.start_moving = True
				self.moving_direction = 1
			elif event.key == pygame.K_SPACE:
				self.calc_jump_point()
				self.jump(0.01)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				self.start_moving = False
			elif event.key == pygame.K_d:
				self.start_moving = False
			if event.key == pygame.K_SPACE:
				pass
