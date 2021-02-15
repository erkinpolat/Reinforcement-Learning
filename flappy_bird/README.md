# Q-Learning for Flappy Bird

## Instructions
1. To run the code first set your directory to the flappy_bird folder.
2. Create a virtual environment with
	$ python3 -m venv my_env
	$ source my_env/bin/activate
3. Load dependencies with
    $ pip install -r requirements.txt
4. To run the code, type:
    $ python game.py
(if you want to play the game comment out the last loop in the game.py file and just type start_game() at the end of the file. The current settings make the bot play the game in training mode.)

## Files in the directory
- game.py: Involves the main loop of the game as a start_game() function. With the parameters, the function can be set to have a human player or the q learning AI as a player. 
- bird.py: Defining the bird object.
- pipe.py: Defining the pipe object. The object itself holds the list of all pipes. Has methods that generate pipes, move pipes, check for collisions etc.
- game_variables.py: Defines an object to store the variables of the game. Creates the screen, does the rendering, takes care of the scores etc.
- q_learning.py: Defining the q-learning AI object. 
- initiate_q_table.py: Initiates the q-table in the json file.
- q_table.json: Stores the q-values of each state.

(Here's some intro on q-learning, you can skip it if you feel comfortable with the topic.)

## Q-Learning:

Q-Learning is a type of reinforcement learning with an AI agent operating in an environment with states, rewards and actions. By interacting with the environment, the agent aims to find an optimal policy through trial and error.

The agents utilize q-values to assess each state and action pair. Q(s, a) indicates the quality of an action a in a given state s.

The q-values are stored in q-tables where there is an entry for each state, action pair. It is important to note that the number of states and possible actions are limited, therefore, we can encompass them in a table.

### Temporal Difference and The Bellman Equation

In q-learning, the agent calculates a temporal difference at each step. Temporal difference shows how much the q-value for the action taken in the previous state should change. It could be written as:

TD(s_t, s_t) = r_t + gamma x max Q(s_t+1, a) - Q(s_t, a_t)
Q_new(s_t, a_t) = Q_old(s_t, a_t) + alpha x TD(s_t, a_t)
