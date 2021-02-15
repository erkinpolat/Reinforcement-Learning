import random
import pygame

class Pipe():
	def __init__(self):
		self.surface = pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png').convert())
		self.list = []
		self.height = [400, 600, 800]

	def create_pipe(self):
		random_pipe_position = random.choice(self.height)
		bottom_pipe = self.surface.get_rect(midtop=(700, random_pipe_position))
		top_pipe = self.surface.get_rect(midbottom=(700, random_pipe_position - 300))

		self.list.extend((bottom_pipe, top_pipe))

	def move_pipes(self):
		if len(self.list) > 5:
			self.list.pop(0)
			self.list.pop(0)

		for pipe in self.list:
			pipe.centerx -= 5

	def check_collision(self, bird):
		
		if bird.rect.top <= -100 or bird.rect.bottom >= 900:
			return False, -1000

		for pipe in self.list:
			if bird.rect.colliderect(pipe):
				return False, -1000
				
		return True, 1

	
	#The function to get the height of the closest lower pipe and it's horizontal position
	def get_height_of_the_next_pipe(self):
		
		#If there is no pipe return most likely values
		if len(self.list) == 0:
			return [600, 500]

		else:
			#For each pipe
			for pipe in self.list:
				#Check if lower or upper pipe
				if pipe.top > 0:
					#Check if the pipe has already been passed and if the pipe's in the screen
					if pipe.right > 70 and pipe.left < 576:
						#Return coordinates
						return [pipe.top, pipe.left]

			return [600, 500]

	def passed(self, bird):
		for pipe in self.list:
			if pipe.right + 10 < bird.rect.left:
				return True

		return False

