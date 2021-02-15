import pygame
import sys
import random
from bird import Bird
from pipe import Pipe 
from game_variables import Game
from q_learning import QBot
import time


#Function to run the game. Player type and training mode can be chosen
#To run the q-learning algorithm use the key word "qbot"
def start_game(player='human', train='True'):
	
	#Initiating the game and creating user events
	pygame.init()

	#Event for flapping wings
	BIRDFLAP = pygame.USEREVENT + 1
	pygame.time.set_timer(BIRDFLAP, 200)

	#Event for spawning pipes
	SPAWNPIPE = pygame.USEREVENT
	pygame.time.set_timer(SPAWNPIPE, 1200)
	#Both events use a timer

	#BOTINPUT = pygame.USEREVENT + 2

	#creating game, bird and pipe instances
	game = Game()
	bird = Bird()
	pipe = Pipe()

	
	#Creates the q-learning ai if it's chosen as the player 
	if player == 'qbot':
		bot = QBot(bird, pipe)


	#Initiating some useful variables
	iteration = 0
	reward = 0
	rewards = []


	#The game loop
	while True:


		#The AI is allowed to make moves every 20 iteration of the game loop		
		if player != 'human' and iteration%20 == 0:
			#Take action for the current position
			bot_input = bot.take_action(train, bird, pipe)
			
			#If the AI inputs 1 make the bird jump
			if bot_input == 1:
				bird.movement = 0
				bird.movement -= 9

		
		#After the first action, update the q-table every time an action is taken (for the previous action)
		if player != 'human' and train and iteration%20 == 0 and iteration > 0:
			bot.update_bellman(reward, bird, pipe)



		#Checking events
		for event in pygame.event.get():
			#Quitting the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#If space is pressed when a human is playing the game
			if event.type == pygame.KEYDOWN and player =='human':
				#Make the bird jumo
				if event.key == pygame.K_SPACE:
					bird.movement = 0
					bird.movement -= 9

				#If the game isn't running, restart the game
				if event.key == pygame.K_SPACE and game.active == False and player=='human':
					game.active = True
					pipe.list.clear()
					bird.rect.center = (100, 512)
					bird.movement = 0
					game.score = 0


			#Creating pipes
			if event.type == SPAWNPIPE and game.active:
				pipe.create_pipe()


			#Updating the bird index to change images to make the bird look like it's flapping
			if event.type == BIRDFLAP:
				if bird.index < 2:
					bird.index+=1
				else:
					bird.index = 0

				bird.animation()

		#Putting the background in place
		game.screen.blit(game.bg_surface, (0, 0))
		
		
		#The general game logic
		if game.active:
			#bird
			bird.movement += game.gravity
			bird.rotate()
			bird.rect.centery+= bird.movement
			game.screen.blit(bird.rotated_bird, bird.rect)
			game.active, reward_increment = pipe.check_collision(bird)
			reward += reward_increment
			
			
			#pipe
			pipe.move_pipes()
			game.draw_pipes(pipe)

			game.score += 0.01
			game.score_display('main_game')


		#At the end the q-table is updated again
		else:
			pygame.quit()
			pygame.font.quit()
			bot.update_bellman(reward, bird, pipe)
			
			if player == 'qbot':
				bot.save_q_values()

			return 'loop: '


#You will need this in the else clause when playing as a human to get the gameover screen
#game.screen.blit(game.game_over_surface, game.game_over_rect)
#game.update_score()
#game.score_display('game_over')




		#floor
		game.floor_x_pos -= 1
		game.draw_floor()
		if game.floor_x_pos <= -576:
			game.floor_x_pos = 0

		

		#The reard is reset every time the AI makes a move
		if iteration%20 == 0:
			rewards.append(reward)
			reward = 0



		pygame.display.update()
		game.clock.tick(120)

		iteration += 1



#start_game()

for i in range(200):
	try:
		start_game(player='qbot', train=True)
		print(str(i))
	except:
		pygame.quit()
		pygame.init()
		pygame.quit()
		pygame.font.quit()
		print(str(i), ": failed attempt")

	time.sleep(1)


