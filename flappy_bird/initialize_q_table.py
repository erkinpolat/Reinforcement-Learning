import json
import numpy as np

#Create empty dictionary
Q = {}

#Getting the vertical and horizontal states
vertical_space = np.linspace(-400, 400, 200)
horizontal_space = np.linspace(0, 500, 50)


#Fill in the dictionary for each state
for i in range(len(vertical_space)+1):
	for j in range(len(horizontal_space)+1):
		for action in range(2):
			Q[str(((i, j), action))] = 0


'''for i in range(len(vertical_space)+1):
	for action in range(2):
		Q[str((i, action))] = 0
'''

#Open the json file
out_file = open("q_table.json", "w") 


#Put the initial q-values in the file
json.dump(Q, out_file)

#Close the file
out_file.close() 