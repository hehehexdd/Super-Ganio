from source.engine.collision import Box
from source.entities.base.entity import *
import pygame


class Enemy(Entity):
	def __init__(self, hp, x, y, level_instance, images: dict, speed_x, initial_move_dir: int):
		super().__init__(hp, x, y, level_instance, images, images['move'], speed_x)
		self.scale_all_images_by(3)
		self.flip_all_images(False)
		from game_data.source.collisions.customcollisions import EnemyDamageBox
		self.collision = EnemyDamageBox(self, self.current_image.get_rect(), {CollisionChannel.Entity: CollisionAction.Pass},
										{CollisionChannel.World: CollisionAction.Block, CollisionChannel.EnemyObstacle: CollisionAction.Block})
		self.level_instance.collisions.append(self.collision)
		self.move_x = initial_move_dir

	def move_x_axis(self, value):
		self.switch_current_image_set('move')
		if not self.is_dead():
			new_pos = self.x + value

			if not self.move_x == 0:
				if not self.level_instance.check_collides_any(self, (new_pos, self.y)):
					self.x = new_pos
					self.collision.move(self.current_image.get_rect(topleft=(self.x, self.y)))
				else:
					if self.move_x > 0:
						self.flip_all_images(False)
					else:
						self.flip_all_images(True)
					self.move_x *= -1

	def kill(self):
		super(Enemy, self).kill()
		self.level_instance.collisions.remove(self.collision)
		self.level_instance.entities.remove(self)