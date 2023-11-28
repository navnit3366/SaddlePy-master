class Game(object):
	'''
	basic class for strategic normal form games, represented at players with payoff matrices
	'''

	def __init__(self, matrices):
		self.matrices = matrices
		self.dimension = self.matrices[0].shape
		self.no_players = len(self.matrices)



class Subgame(object):
	'''
	basic class for sub games
	'''

	def __init__(self, matrices, indices):
		self.no_players = len(indices)
		self.indices = indices
		self.matrices = matrices
		self.submatrices = [None]*self.no_players			# ugly, what is a better way?
		self.computeAllSubgames()

	def __str__(self):
		string = ""
		for i in self.submatrices:
			string = string + "\n" + str(i) + "\n"
		return string

	def __eq__(self, other):
		if self.matrices == other.matrices and self.indices == other.indices:
			return True
		return False


	'''
		comparison function if the subgame is a subgame of the given subgame
		@param subgame - Subgame the original subgame is compared to
		@return Boolean - True if game is subgame, False if not
	'''
	def __le__(self, subgame):
		for i,j in zip(self.indices, subgame.indices):
			set_i = set(i)
			set_j = set(j)
			if not set_i <= set_j: 
				return False
		return True


	''' function that computes the subgame payoff matrix for given game and indices
		@param i - player id
	'''
	def computeSubgame(self, player_id):
		self.submatrices[player_id] = self.matrices[player_id]
		#print "Compute subgame..."
		for i in range(len(self.indices)):
			self.submatrices[player_id] = self.submatrices[player_id].take(self.indices[i], axis=i)


	''' function that computes the subgame payoff matrix for all players
	'''
	def computeAllSubgames(self):
		for i in range(self.no_players):
			self.computeSubgame(i)


	''' function to add a new action and return the new, bigger subgame '''
	def addActions(self, player_id, action_id_list):
		#print "Add action " + str(action_id_list) + " for player " + str(player_id)
		self.indices[player_id].extend(action_id_list)
		list_tmp = set(self.indices[player_id])
		self.indices[player_id] = sorted(list_tmp)
		self.computeAllSubgames()



	''' function that returns the size of a subgame 
		@return int[] where first entry corresponds to first player a.s.o.
	'''
	def getSize(self):
		sizes = []
		for i in self.indices:
			sizes.append(len(i))
		return sizes



