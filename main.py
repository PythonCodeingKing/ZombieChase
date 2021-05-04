import pygame

from player import Player
from zombie import Zombie

class Game:
	def __init__(self):
		pygame.init()
		
		self.screen = pygame.display.set_mode((600, 600))
		
		self.player = Player(self)
		self.zombies = pygame.sprite.Group()
		pygame.mouse.set_visible(False)
		self.ticks = 1
		self.clock = pygame.time.Clock()
		self.run_game()
		
	def run_game(self):
		while True:
			self.check_events()
			self.player.update()
			self.collisions()
			self.update_screen()
			self.update_tickspeed()
			#print(len(self.zombies))
			self.zombies.update()
	def update_tickspeed(self):
		self.ticks += 1
		if (self.ticks % 120) == 0:
			self.zombies.add(Zombie(self))
		if (self.ticks % 120) == 0:
			for zombie in self.zombies.copy():
				zombie.seconds -= 1
				if zombie.seconds == 0:
					self.zombies.remove(zombie)
			
		if self.ticks > 10000000:
			self.ticks = 1
	
	def collisions(self):
		
		if pygame.sprite.spritecollideany(self.player, self.zombies):
				self.player.health -= 10
				self.zombies.empty()
				if self.player.health == 0:
					quit()
		
	
	def update_screen(self):
		self.screen.fill((0, 0, 230))
		for zombie in self.zombies.sprites():
			zombie.draw()
		
		self.player.draw()
		font = pygame.font.SysFont(None, 24)
		img = font.render(f'P1 Health: {self.player.health}', True, (255, 0, 0))
		self.screen.blit(img, (0, 0))
		pygame.display.flip()
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			

game = Game()
