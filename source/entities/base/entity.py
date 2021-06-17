from source.base.camera import *


class Entity:
	def __init__(self, x, y, level_instance, images: dict, jump_max_height):
		self.level_instance = level_instance
		self.x = x
		self.y = y
		self.images = images
		self.current_image = self.images['idle'][0]
		self.jump_max_height = jump_max_height
		self.jump_max_pos = self.y - jump_max_height 
		self.started_jumping = False
		self.enable_gravity = True
		self.start_ticking = True

	def move_x_axis(self, value):
		pass

	def jump(self, value):
		pass
		# if self.y > self.jump_max_pos:
		# 	self.y += value
		# else:
		# 	self.enable_gravity = True

	def calc_jump_point(self):
		if not self.started_jumping:
			self.jump_max_pos = self.y + self.jump_max_height
			self.started_jumping = True

	def handle_events(self, event):
		pass

	def tick(self, delta_time):
		pass

	def draw(self, renderer, camera):
		rect = self.current_image.get_rect()
		if isinstance(camera, Camera):
			rect = camera.apply_rect(rect)
		renderer.blit(self.current_image, rect)
