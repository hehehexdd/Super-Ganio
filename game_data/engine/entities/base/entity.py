from game_data.engine.base.camera import *
import time


def clamp(value, min_val, max_val):
	if value < min_val:
		value = min_val
	elif value > max_val:
		value = max_val
	return value


class Entity:
	def __init__(self, hp, x, y, level_instance, images: dict, default_set, speed_x):
		self.items = []
		self.level_instance = level_instance
		self.collision = None
		self.hp = hp
		self.max_lives = self.hp + self.hp / 2
		self.time_was_hit = 0.0
		self.invincibility_frames_seconds = 0.6
		self.blinking_time_start = 0.0
		self.blinking_time_in_between = 0.2
		self.start_blinking = False
		self.should_blink = True
		self.should_be_drawn = True
		self.x = x
		self.y = y
		self.images = images
		self.current_image_set = default_set
		self.current_image_set_index = 0
		self.current_image = self.current_image_set[self.current_image_set_index]
		self.speed_x = speed_x
		self.can_update_animation = True
		self.start_ticking = True
		self.move_x = 0
		self.move_y = 0
		self.fly_mode = False
		self.god_mode = False
		self.is_on_ground = False
		self.facing_right = True
		# jump vals v
		self.can_jump = True
		self.can_calc_jump_point = True
		self.jump_speed = 700
		self.max_jump_pos_y = 0
		self.max_jump_height = 200
		# gravity vals v
		self.enable_gravity = True
		self.initial_gravity = 1
		self.current_gravity_pull = 1
		self.gravity_increment = 5000
		self.max_gravity = 800

	def scale_all_images_by(self, scale):
		for image_set in self.images:
			for i in range(len(self.images[image_set])):
				image = self.images[image_set][i]
				self.images[image_set][i] = pygame.transform.scale(image, (image.get_rect().width * scale, image.get_rect().height * scale))

	def move_x_axis(self, value):
		if not self.is_dead():
			new_pos = self.x + value

			if not self.move_x == 0:
				if not self.level_instance.check_collides_any(self, (new_pos, self.y)):
					self.x = new_pos
					self.collision.move(self.current_image.get_rect(topleft=(self.x, self.y)))

	def move_y_axis(self, value):
		if not self.is_dead():
			new_pos = self.y + value
			condition = self.level_instance.check_collides_any(self, (self.x, new_pos))

			if not self.fly_mode:
				# if jumping
				if value < 0:
					if not condition and new_pos > self.max_jump_pos_y:
						self.y = new_pos
						self.collision.move(self.current_image.get_rect(topleft=(self.x, self.y)))
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
					self.collision.move(self.current_image.get_rect(topleft=(self.x, self.y)))
					self.can_calc_jump_point = False
					self.can_jump = False
					self.is_on_ground = False
				else:
					self.is_on_ground = True
					self.can_calc_jump_point = True
			elif not condition:
				self.y = new_pos
				self.collision.move(self.current_image.get_rect(topleft=(self.x, self.y)))

	def jump(self):
		if self.can_jump:
			self.enable_gravity = False
			self.move_y = -1

	def calc_jump_point(self):
		if self.can_calc_jump_point:
			self.max_jump_pos_y = self.y - self.max_jump_height
			self.can_calc_jump_point = False

	def stop_movement(self):
		self.move_x = 0
		self.enable_gravity = False

	def add_item_to_inventory(self, item):
		self.items.append(item)
		self.on_item_add_to_inventory()

	def on_item_add_to_inventory(self):
		pass

	def get_num_of_items_of_name(self, name):
		count = 0
		for item in self.items:
			if item.name == name:
				count += 1
		return count

	def handle_events(self, event):
		pass

	def tick(self, delta_time):
		self.move_x_axis(self.speed_x * self.move_x * delta_time)
		self.move_y_axis(self.jump_speed * self.move_y * delta_time)

	def apply_physics(self, delta_time):
		if self.enable_gravity:
			self.move_y = 1
			self.move_y_axis(self.current_gravity_pull * delta_time)
			self.current_gravity_pull += self.gravity_increment * delta_time
			self.current_gravity_pull = clamp(self.current_gravity_pull, self.initial_gravity, self.max_gravity)

	def switch_current_image_set(self, image_set_name: str):
		if image_set_name in self.images.keys():
			self.current_image_set = self.images[image_set_name]

	def flip_all_images(self, facing_right_now: bool):
		if facing_right_now != self.facing_right:
			for image_list_name in self.images:
				for i in range(len(self.images[image_list_name])):
					self.images[image_list_name][i] = pygame.transform.flip(self.images[image_list_name][i], True, False)
			self.current_image = pygame.transform.flip(self.current_image, True, False)
			self.facing_right = not self.facing_right

	def animate(self):
		if self.can_update_animation:
			self.apply_animation()
			self.level_instance.game_instance.set_timer(self.reset_animation, 0.125)

	def apply_animation(self):
		if self.current_image_set_index < len(self.current_image_set):
			self.current_image = self.current_image_set[self.current_image_set_index]
			self.current_image_set_index += 1
		else:
			self.current_image_set_index = 0
		self.can_update_animation = False

	def reset_animation(self):
		self.can_update_animation = True

	def apply_blink(self):
		if time.time() >= (self.time_was_hit + self.invincibility_frames_seconds):
			self.start_blinking = False
			self.should_be_drawn = True
		elif self.start_blinking:
			if time.time() >= self.blinking_time_start + self.blinking_time_in_between:
				self.blinking_time_start = time.time()
				self.should_be_drawn = not self.should_be_drawn

	def toggle_blinking(self):
		self.start_blinking = True

	def draw(self, renderer, camera):
		self.apply_blink()
		rect = self.current_image.get_rect(topleft=(self.x, self.y))
		if isinstance(camera, Camera):
			rect = camera.apply_rect(rect)
		if self.should_be_drawn:
			renderer.blit(self.current_image, rect)

	def hit(self):
		if not self.god_mode:
			if time.time() >= (self.time_was_hit + self.invincibility_frames_seconds):
				if self.hp - 1 > 0:
					self.hp -= 1
					self.time_was_hit = time.time()
					self.toggle_blinking()
				else:
					if not self.is_dead():
						self.kill()

	def kill(self):
		self.hp = 0

	def is_dead(self):
		return self.hp <= 0
