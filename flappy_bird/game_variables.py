import pygame

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((576, 1024))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font('04B_19.ttf', 40)

		self.gravity = 0.25
		
		self.active = True

		self.score = 0
		self.high_score = 0

		self.bg_surface = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())
		self.floor_surface = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
		self.floor_x_pos = 0

		self.game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
		self.game_over_rect = self.game_over_surface.get_rect(center=(288, 512))


	def draw_pipes(self, pipes):
		for pipe in pipes.list:
			if pipe.bottom >= 1024:
				self.screen.blit(pipes.surface, pipe)
			else:
				flip_pipe = pygame.transform.flip(pipes.surface, False, True)
				self.screen.blit(flip_pipe, pipe)


	def draw_floor(self):
		self.screen.blit(self.floor_surface, (self.floor_x_pos, 900))
		self.screen.blit(self.floor_surface, (self.floor_x_pos+576, 900))


	def score_display(self, game_state):
		if game_state == 'main_game':
			score_surface = self.font.render(str(int(self.score)), True, (255, 255, 255))
			score_rect = score_surface.get_rect(center=(288, 100))
			self.screen.blit(score_surface, score_rect)
		if game_state == 'game_over':
			score_surface = self.font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
			score_rect = score_surface.get_rect(center=(288, 100))
			self.screen.blit(score_surface, score_rect)

			high_score_surface = self.font.render(f'High score: {int(self.high_score)}', True, (255, 255, 255))
			high_score_rect = high_score_surface.get_rect(center=(288, 850))
			self.screen.blit(high_score_surface, high_score_rect)

	def update_score(self):
		if self.score > self.high_score:
			self.high_score = self.score



