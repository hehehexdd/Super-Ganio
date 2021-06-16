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
		self.start_moving_down = False
		self.moving_direction = 1
		self.moving_down_direction = 1
		self.movement_add_up = [0, 0]

	def apply_camera_movement(self, map_pos, surfaces: dict):
		map_pos[0] += self.movement_add_up[0]
		map_pos[1] += self.movement_add_up[1]

		for drawable in surfaces:
			surfaces[drawable][0] += self.movement_add_up[0]
			surfaces[drawable][1] += self.movement_add_up[1]

		self.movement_add_up = [0, 0]

	def add_movement(self, value_x, value_y):
		self.movement_add_up[0] += value_x
		self.movement_add_up[1] += value_y

	def move(self, value,):
		if not self.owner.check_collides_any(self.current_image.get_rect(bottomleft=((self.x + value), self.y))):
			new_pos = value
			self.x += new_pos
			self.add_movement(-value, 0)

	def move_down(self, value, ):
		#if not self.owner.check_collides_any(self.current_image.get_rect(bottomleft=(self.x, (self.y + value)))):
		new_pos = value
		self.y += new_pos
		self.add_movement(0, -value)

	def draw(self, renderer: pygame.Surface):
		renderer.blit(self.current_image, renderer.get_rect().center)

	def tick(self, delta_time):
		if self.start_moving:
			self.move(self.speed * self.moving_direction * delta_time)
		if self.start_moving_down:
			self.move_down(self.speed * self.moving_down_direction * delta_time)
		# print(self.camera.offset.x, self.camera.offset.y)
		#print(self.x, self.y)

	def handle_events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				self.start_moving = True
				self.moving_direction = -1
			elif event.key == pygame.K_d:
				self.start_moving = True
				self.moving_direction = 1
			elif event.key == pygame.K_w:
				self.start_moving_down = True
				self.moving_down_direction = -1
			elif event.key == pygame.K_s:
				self.start_moving_down = True
				self.moving_down_direction = 1
			elif event.key == pygame.K_SPACE:
				self.calc_jump_point()
				self.jump(0.01)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				self.start_moving = False
			elif event.key == pygame.K_d:
				self.start_moving = False
			elif event.key == pygame.K_w:
				self.start_moving_down = False
			elif event.key == pygame.K_s:
				self.start_moving_down = False
			if event.key == pygame.K_SPACE:
				pass
