import numpy as np
import json
import random

class QBot():
	def __init__(self, bird, pipe):

		#Create the observation space for both
		self.vertical_space = np.linspace(-400, 400, 200)
		self.horizontal_space = np.linspace(0, 500, 50)

		#self.state_space = self.find_state_space()

		#Defining the hyper-parameters
		#Discount factor
		self.gamma = 0.9
		#Learning rate
		self.alpha = 0.1
		#Randomness in move selesction
		self.epsilon = 0.05

		
		#Upon initiation loads the q-values from the json file
		self.load_q_values()

		
		#Gets the starting state
		self.state = self.get_state(bird, pipe)

		#Stores each of the states in a list
		self.state_list = [self.state]
		
		#Store each action taken
		self.action_list = []



	#Function to find the state space. Not actively used
	def find_state_space(self):
		states = []

		for i in range(len(self.vertical_space)+1):
			for j in range(len(self.horizontal_space)+1):
				states.append((i, j))


	#Find the parameters of the game
	def find_parameters(self, bird, pipe):
		#Runs the function to get the vertical and horizontal distance of the bird to the closest pipe
		parameters = pipe.get_height_of_the_next_pipe()

		
		if parameters:
			vert_dist = bird.rect.bottom - parameters[0]
			horiz_dist = parameters[1] - bird.rect.right

		
		#If we don't get any parameters I set them to most likely figures
		else:
			vert_dist = 600
			horiz_dist = 500
		
		return [vert_dist, horiz_dist]

	
	#Function to get the state
	def get_state(self, bird, pipe):
		
		#Runs find parameters function to get the distances
		observation = self.find_parameters(bird, pipe)
		observation1, observation2 = observation[0], observation[1]

		#If the parameters are beyond the limit of the state space, reduce them
		if observation1 > 400:
			observation = 399

		elif observation1 < -400:
			observation = -399

		if observation2 > 500:
			observation2 = 499

		#Digitize the observations to get indice-like numbers from the state space
		observation1 = int(np.digitize(observation1, self.vertical_space))
		observation2 = int(np.digitize(observation2, self.horizontal_space))

		#Return the state values as a tuple
		return (observation1, observation2)

	
	#Get state function for a single parameter model. Not used in the current version.
	def get_state1(self, bird, pipe):
		obs = bird.rect.bottom - pipe.get_height_of_the_next_pipe()

		obs = int(np.digitize(obs, self.vertical_space))

		return obs


	#Upon initialization, we get the q-values from a json file and put them in a dictionary
	def load_q_values(self):
		#Create a dictionary
		self.q_values = {}

		#Open the json file
		try:
			fil = open("q_table.json", "r")

		except IOError:
			return

		#Put the values in the dictionary
		self.q_values = json.load(fil)

		#Close the json file
		fil.close() 

	#After the training q-values are stored in a json file
	def save_q_values(self):
		#open the json file
		fil = open("q_table.json", "w")
		
		#Put the qvalues in the json file
		json.dump(self.q_values, fil)
		
		#Close the json file
		fil.close()

	def check_q_value(self, state, action):
		#Takes a state and action pair and returns the q-value
		return self.q_values[str((state, action))]

	def get_max_action(self, state):
		#Gets the q values of a state for either action
		action_1 = self.q_values[str((state, 0))]
		action_2 = self.q_values[str((state, 1))]

		#Compares the q-values and returns the better action totake
		if action_2 > action_1:
			return 1
		else:
			return 0

	def take_action(self, train, bird, pipe):
		#While in training mode
		if train:
			#With a probability of epsilon we make a random move
			if random.random() < self.epsilon:
				action = random.choice([0, 1])
				
				#recording the state and the action
				self.action_list.append(action)
				self.state_list.append(self.get_state(bird, pipe))
				return action

			else:
				#In other cases we make the action with the highest return
				action = self.get_max_action(self.get_state(bird, pipe))
				
				#Recording the action and the state
				self.action_list.append(action)
				self.state_list.append(self.get_state(bird, pipe))
				return action

		else:
			
			#If it isn't trained, always the best action is performed
			action = self.get_max_action(self.get_state(bird, pipe))
			self.action_list.append(action)
			self.state_list.append(self.get_state(bird, pipe))
			return action

	def update_bellman(self, reward, bird, pipe):
		#get the current state
		current_state = self.state_list[-1]

		#compute the temporal difference
		td = reward + self.gamma * self.check_q_value(current_state, self.get_max_action(current_state)) - self.check_q_value(self.state_list[-2], self.action_list[-2])

		
		#uodate the state
		self.q_values[str((self.state_list[-2], self.action_list[-2]))] = self.q_values[str((self.state_list[-2], self.action_list[-2]))] + self.alpha * td






