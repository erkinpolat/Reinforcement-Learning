import pygame

class Bird():
	def __init__(self):

		self.downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
		self.midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
		self.upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())

		self.frames = [self.downflap, self.midflap, self.upflap]

		self.index = 0

		self.surface = self.frames[self.index]
		self.rect = self.surface.get_rect(center=(100, 512))
		
		self.movement = 0
		self.rotated_bird = pygame.transform.rotozoom(self.surface, self.movement*-3, 1)

		

	def animation(self):
		self.surface = self.frames[self.index]
		self.rect = self.surface.get_rect(center=(100, self.rect.centery))

	def rotate(self):
		self.rotated_bird = pygame.transform.rotozoom(self.surface, self.movement*-3, 1)



