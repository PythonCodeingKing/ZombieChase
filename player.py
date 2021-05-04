import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, zombieGame):
		
		self.screen = zombieGame.screen
		self.image = pygame.image.load("images/player.png")
		self.rect = self.image.get_rect()
		
		self.y = self.rect.y
		self.x = self.rect.x
		
		self.health = 100
	def draw(self):
		self.rect.y = self.y
		self.rect.x = self.x
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		x, y = pygame.mouse.get_pos()
		
		self.x = x
		self.y = y
