from source.engine.camera import *
from source.engine.collisionchannels import *


def clamp(value, min_val, max_val):
	if value < min_val:
		value = min_val
	elif value > max_val:
		value = max_val
	return value


class Entity:
	def __init__(self, hp, collision_channel: CollisionChannel, x, y, level_instance, images: dict, speed_x):
		self.level_instance = level_instance
		self.hp = hp
		self.x = x
		self.y = y
		self.images = images
		self.current_image = self.images['idle'][0]
		self.speed_x = speed_x
		self.start_ticking = True
		self.move_x = 0
		self.move_y = 0
		self.fly_mode = False
		self.ghost_mode = False
		self.is_on_ground = False
		self.collision_channel = collision_channel
		# jump vals v
		self.can_jump = True
		self.can_calc_jump_point = True
		self.jump_speed = 800
		self.max_jump_pos_y = 0
		self.max_jump_height = 200
		# gravity vals v
		self.enable_gravity = True
		self.initial_gravity = 1
		self.current_gravity_pull = 1
		self.gravity_increment = 10000
		self.max_gravity = 800

	def move_x_axis(self, value):
		new_pos = self.x + value

		if not self.move_x == 0:
			if not self.level_instance.check_collides_any(self, (new_pos, self.y)):
				self.x = new_pos

	def move_y_axis(self, value):
		new_pos = self.y + value
		condition = True

		if not self.move_y == 0:
			condition = self.level_instance.check_collides_any(self, (self.x, new_pos))

		if not self.fly_mode:
			# if jumping
			if value < 0:
				if not condition and new_pos > self.max_jump_pos_y:
					self.y = new_pos
					self.is_on_ground = False
				else:
					self.is_on_ground = False
					self.can_jump = False
					self.enable_gravity = True
					self.move_y = 0
					self.current_gravity_pull = self.initial_gravity
			# if not jumping
			elif not condition:
				self.y = new_pos
			else:
				self.is_on_ground = True
				self.can_calc_jump_point = True
		elif not condition:
			self.y = new_pos

	def jump(self):
		if self.can_jump:
			self.enable_gravity = False
			self.move_y = -1

	def calc_jump_point(self):
		if self.can_calc_jump_point:
			self.max_jump_pos_y = self.y - self.max_jump_height
			self.can_calc_jump_point = False

	def handle_events(self, event):
		pass

	def hidden_tick(self, delta_time):
		self.move_x_axis(self.speed_x * self.move_x * delta_time)
		self.move_y_axis(self.jump_speed * self.move_y * delta_time)

	def tick(self, delta_time):
		pass

	def apply_physics(self, delta_time):
		if self.enable_gravity:
			self.move_y = 1
			self.move_y_axis(self.current_gravity_pull * delta_time)
			self.current_gravity_pull += self.gravity_increment * delta_time
			self.current_gravity_pull = clamp(self.current_gravity_pull, self.initial_gravity, self.max_gravity)

	def draw(self, renderer, camera):
		rect = self.current_image.get_rect()
		if isinstance(camera, Camera):
			rect = camera.apply_rect(rect)
		renderer.blit(self.current_image, rect)

	def is_dead(self):
		return self.hp <= 0

	def kill(self):
		pass
