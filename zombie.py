import pygame
import random

class Zombie(pygame.sprite.Sprite):
	def __init__(self, chase):
		super().__init__()
		self.screen = chase.screen
		self.player_rect = chase.player.rect
		self.image = pygame.image.load("images/zombie.png")
		self.rect = self.image.get_rect()
		random.seed()
		self.rect.x = random.randint(0, 600)
		self.rect.y = random.randint(0, 600)
		self.seconds = 15
	
	def draw(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		if self.rect.x < self.player_rect.x:
			self.rect.x += 0.5
		if self.rect.x > self.player_rect.x:
			self.rect.x -= 0.5
			
		if self.rect.y < self.player_rect.y:
			self.rect.x += 0.5
		if self.rect.y > self.player_rect.y:
			self.rect.y -= 0.5
		
			
		
