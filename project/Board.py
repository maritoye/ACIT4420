"""
Board class
A board contains a 2d array of instances of Cell
The Board will upon initialization split itself until it becomes a perfect labyrinth,
with one exit and only one solution from any position
"""

from Cell import Cell
import random


class Board:
	def __init__(self,x,y):
		self._board = [["c"] * x for i in range(y)]
		id = 0
		for i in range(x):
			for j in range(y):
				self._board[j][i] = Cell(i,j, id)
				id+=1

		self.create_walls()

		self.split_horizontal(0, 0, self.get_width()-1, self.get_height()-1)


	def create_walls(self):
		"""
		Creates the outer walls of the labyrinth, and chooses a random opening in one of the walls chosen randomly
		:return: instance of class Cell - the Cell that has the opening of the labyrinth
		"""
		exit_wall = random.randint(0, 4)
		exit_index = random.randint(0,self.get_width()) if ((exit_wall == 0) or (exit_wall == 1)) else random.randint(0,self.get_height())

		for ncell in range(len(self._board[0])):
			border_cell = self._board[0][ncell]
			border_cell.set_wall_n(self,True)
			if exit_wall == 0:
				if ncell==exit_index:
					border_cell.set_wall_n(self, False)
					border_cell.set_solution(True)


		for scell in range(len(self._board[0])):
			border_cell = self._board[len(self._board)-1][scell]
			border_cell.set_wall_s(self,True)
			if exit_wall == 1:
				if scell==exit_index:
					border_cell.set_wall_s(self, False)
					border_cell.set_solution(True)


		for wcell in range(len(self._board)):
			border_cell = self._board[wcell][0]
			border_cell.set_wall_w(self,True)
			if exit_wall == 2:
				if wcell==exit_index:
					border_cell.set_wall_w(self, False)
					border_cell.set_solution(True)


		for ecell in range(len(self._board)):
			border_cell = self._board[ecell][len(self._board[0])-1]
			border_cell.set_wall_e(self, True)
			if exit_wall == 3:
				if ecell==exit_index:
					border_cell.set_wall_e(self, False)
					border_cell.set_solution(True)


	def get_cell(self,x,y):
		"""
		:param x: int - x position of cell to be returned
		:param y: int - y position of cell to be returned
		:return: instance of class Cell
		"""
		cell = self._board[y][x]
		return cell


	def get_solution(self):
		"""
		:return: instance of class Cell
		"""
		return self.solution


	def get_height(self):
		"""
		:return: int - y length of the board
		"""
		return len(self._board)


	def get_width(self):
		"""
		:return: int - x length of the board
		"""
		return len(self._board[0])


	def _set_cell(self, board, x,y):
		"""
		inserts a given instance of Cell (by x,y) from given Board into this Board
		:param board: instance of Board
		:param x: int -
		:param y: int -
		:return:
		"""
		self._board[y][x] = board.get_cell(x,y)

	def split_horizontal(self, fromx, fromy, tox, toy):
		"""
		splits subset of board in two if height is two cells or larger, calls split vertical for each of those boards
		inserts a wall at the split, with one opening
		:param fromx: int - the subsets starting position x on the board
		:param fromy: int - the subsets starting position y on the board
		:param tox: int - the subsets ending position x on the board
		:param toy: int - the subsets ending position y on the board
		"""

		# breaks the recursive calling if the cell is size 1x1
		if (tox-fromx) < 1 and (toy-fromy) < 1:
			return

		elif ((toy - fromy) > 0 and (tox-fromx)<=(toy-fromy)) or (toy - fromy) == 1:
		#elif (toy - fromy) > 0:
			if (toy - fromy) > 0:
				split = random.randint(fromy+1, toy)
			else:
				split = toy

			if (tox - fromx) > 0:
				opening = random.randint(fromx, tox)
			else:
				opening = fromx

			for cell in range(fromx,tox+1):
				if cell != opening:
					self.get_cell(cell, split).set_wall_n(self, True)

		#call split_vertical for top board if width is larger than one
			self.split_vertical(fromx, fromy, tox, split-1)

		#call split_vertical for bottom board
			self.split_vertical(fromx, split, tox, toy)

		# if grid is less than two cells high, go to split vertically
		elif tox-fromx > 2:
			self.split_vertical(fromx, fromy, tox, toy)


	def split_vertical(self, fromx, fromy, tox, toy):
		"""
		splits subset of board in two if width is two cells or larger, calls split horizontal for each of those boards
		inserts a wall at the split, with one opening
		:param fromx: int - the subsets starting position x on the board
		:param fromy: int - the subsets starting position y on the board
		:param tox: int - the subsets ending position x on the board
		:param toy: int - the subsets ending position y on the board
		"""
		# breaks the recursive calling if the cell is size 1x1
		if (tox - fromx) < 1 and (toy - fromy) < 1:
			return

		elif ((tox-fromx) > 0 and (tox-fromx)>=(toy-fromy)) or (tox - fromx) == 1:
		#elif (tox - fromx) > 0:

			if (tox - fromx) > 0:
				split = random.randint(fromx + 1, tox)
			else:
				split = tox

			if (toy - fromy) > 0:
				opening = random.randint(fromy, toy)
			else:
				opening = fromy

			for cell in range(fromy,toy+1):
				if cell != opening:
					self.get_cell(split,cell).set_wall_w(self, True)

		#call split_vertical for top board if width is larger than one
			self.split_horizontal(fromx, fromy, split-1, toy)

		#call split_vertical for bottom board
			self.split_horizontal(split, fromy, tox, toy)

		# if grid is less than two cells high, go to split vertically
		elif toy-fromy > 2:
			self.split_horizontal(fromx, fromy, tox, toy)

