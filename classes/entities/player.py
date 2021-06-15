import pygame
from classes.entities.base.entity import *


class Player(Entity):

	LIVES = 3
	COLLECTED_ROSES = 0

	def __init__(self, x, y, level_instance, images: list, jump_max_height, owner: object, speed, screen_width, screen_height):
		super().__init__(x, y, level_instance, images, jump_max_height, owner)
		self.camera = Camera(self, screen_width, screen_height)
		self.camera.set_method(Follow(self.camera, self))
		self.speed = speed

	def move(self, value):
		if not self.owner.collides_with_any(self.current_image.get_rect(center=(self.x + value, self.y))):
			self.x += value
			self.camera.move()

	def draw(self, renderer):
		renderer.blit(self.current_image, (self.x - self.camera.offset.x, self.y - self.camera.offset.y))

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
				self.jump(0.01)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				pass
