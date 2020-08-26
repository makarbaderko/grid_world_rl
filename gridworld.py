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