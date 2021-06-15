from source.entities.camera import Camera


class Entity:
	def __init__(self, x, y, level_instance, images: list, jump_max_height, owner: object):
		self.owner = owner
		self.level_instance = level_instance
		self.x = x
		self.y = y
		self.images = images
		self.current_image = self.images[0]
		self.jump_max_height = jump_max_height
		self.jump_max_pos = self.y - jump_max_height 
		self.started_jumping = False
		self.enable_gravity = True
		self.start_ticking = True

	def move(self, value):
		self.x += value

	def jump(self, value):
		if self.y > self.jump_max_pos:
			self.y += value
		else:
			self.enable_gravity = True

	def calc_jump_point(self):
		if not self.started_jumping:
			self.jump_max_pos = self.y + self.jump_max_height
			self.started_jumping = True

	def handle_events(self, event):
		pass

	def draw(self, renderer, camera: Camera):
		renderer.blit(self.current_image, (self.x - camera.offset.x, self.y - camera.offset.y))

	def tick(self, delta_time):
		pass
