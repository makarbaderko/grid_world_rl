class Grid: #Environment
	def __init__(self, rows, cols, start):
		self.rows = rows
		self.cols = cols
		self.i = start[0]
		self.j = start[1]
	#Set class's prameters to given rewards and actions
	def set(self, rewards, actions):
		#reward = dict of (i, j) : A (row, col): reward
		#actions = dict of (i, j) : A (row, col): action list
		self.rewards = rewards
		self.actions = actions
	def set_state(self, s):
		'''Cheats'''
		self.i = s[0]
		self.j = s[1]
	#What's happening in the gridworld
	def current_state(self):
		return (self.i, self.j)
	#End or not
	def is_terminal(self, s):
		return s not in self.actions
	#Get the new state
	def get_next_state(self, s, a):
		i, j = s[0], s[1]
		if a in self.actions[(i, j)]:
			#If action is
			#Up
			if a == 'U':
				i -= 1
			#Down
			elif a == 'D':
				i += 1
			#Right
			elif a == 'R':
				j+=1
			#Left
			elif a == 'L':
				j -= 1
		#The new state
		return i, j
	def move(self, action):
		#check if allowed
		if action in self.actions[(self.i, self.j)]:
			if action == 'U':
				self.i -= 1
			#Down
			elif action == 'D':
				self.i += 1
			#Right
			elif action == 'R':
				self. j += 1
			#Left
			elif action == 'L':
				self.j -= 1
		return self.rewards.get((self.i, self.j), 0)
	