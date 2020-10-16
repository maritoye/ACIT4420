class Cell:
	def __init__(self,x,y,id):
		self._posx = x
		self._posy = y
		self.id = id

		self._north = False
		self._south = False
		self._west = False
		self._east = False
		self._solution = False

		# for solving the labyrinth
		self._visited = False
		self._path = False

		self.g = 0  # cost of getting to this node, not needed for gbfs
		self.h = 0  # estimated cost from this node to goal
		self.tot = 0 # g + h
		self.children = [] # a list of neighbor cells, for solution

	def set_wall_n(self, board, val):
		self._north = val
		if self._posy > 0:
			neighbor = board.get_cell(self._posx, self._posy-1)
			if not (neighbor.get_wall_s() == val):
				neighbor.set_wall_s(board, val)

	def set_wall_s(self, board, val):
		self._south = val
		if self._posy < board.get_height()-1:
			neighbor = board.get_cell(self._posx, self._posy+1)
			if not (neighbor.get_wall_n() == val):
				neighbor.set_wall_n(board, val)


	def set_wall_w(self, board, val):
		self._west = val

		if self._posx > 0:
			neighbor = board.get_cell(self._posx-1, self._posy)
			if not (neighbor.get_wall_e() == val):
				neighbor.set_wall_e(board, val)


	def set_wall_e(self, board, val):
		self._east = val

		if self._posx < board.get_width()-1:
			neighbor = board.get_cell(self._posx+1, self._posy)
			if not (neighbor.get_wall_w() == val):
				neighbor.set_wall_w(board, val)

	def set_path(self, value):
		self._path = value

	def set_visited(self, value):
		self._visited = value

	def set_solution(self, value):
		self._solution = value

	def get_wall_n(self):
		return self._north

	def get_wall_s(self):
		return self._south

	def get_wall_w(self):
		return self._west

	def get_wall_e(self):
		return self._east

	def get_y(self):
		return self._posy

	def get_x(self):
		return self._posx

	def get_path(self):
		return self._path

	def get_visited(self):
		return self._visited

	def get_solution(self):
		return self._solution
