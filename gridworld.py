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
	def undo_move(self, action):
		if action == "U":
			self.i += 1
		elif action == "D":
			self.i -= 1
		elif action == "R":
			self.j -= 1
		elif action == "L":
			self.j += 1
		#should never happen
		assert(self.current_state() in self.all_states())
	def game_over(self):
		#returns true if the. game if over
		#and false if not
		return (self.i, self.j) not in self.actions
	def all_states(self):
		#returns all next possible states
		return set(self.actions.keys()) | set(self.rewards.keys())
	def standart_grid():
		g = Grid(3, 4, (2, 0))
		rewards = {(0, 3): 1, (1, 3): -1}
		actions = {
			(0, 0) : ('D', 'R'),
			(0, 1) : ('L', 'R'),
			(0, 2) : ('L', 'D', 'R'),
			(1, 0) : ('U', 'D'),
			(1, 2) : ('U', 'D', 'R'),
			(2, 0) : ('U', 'R'),
			(2, 1) : ('L', 'R'),
			(2, 2) : ('L', 'R', 'U'),
			(2, 3) : ('L', 'U'),
		}
		g.set(rewards, actions)
		return g