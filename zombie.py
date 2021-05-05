import math

import pygame
import random

class Zombie(pygame.sprite.Sprite):
	def __init__(self, chase):
		super().__init__()
		self.screen = chase.screen
		self.player_rect = chase.player.rect
		self.image = pygame.image.load("images/zombie.png")
		self.rect = self.image.get_rect()
		self.speed = 0.2
		random.seed()
		self.rect.x = random.randint(0, 600)
		self.rect.y = random.randint(0, 600)
		self.seconds = 15
	
	def draw(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		dx, dy = self.player_rect.x - self.rect.x, self.player_rect.y - self.rect.y
		dist = math.hypot(dx, dy)
		dx, dy = dx / dist, dy / dist
		self.rect.x += dx * self.speed
		self.rect.y += dy * self.speed
			
		
