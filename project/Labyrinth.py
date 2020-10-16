from Board import Board
from Visualizer import visualize
import random

class Labyrinth:
	def __init__(self, x, y):
		self._labyrinth = Board(x,y)
		self._labyrinth.create_walls()
		#visualize(self._labyrinth.get_subboard(0,6,0,8))
		split_horizontal(self._labyrinth)

		visualize(self._labyrinth)

	def get_labyrinth(self):
		return self._labyrinth


	def get_height(self):
		return self._labyrinth.get_height()


	def get_width(self):
		return self._labyrinth.get_width()

	def get_cell(self,x,y):
		return self._labyrinth.get_cell(x,y)


def split(board):
	top, bottom = split_horizontal(board)
	if top.get_width()>1:
		left, right = split_vertical(top)
		if left.get_height()>1: split(left)
		if right.get_height()>1: split(right)
	if bottom.get_width()>1:
		left, right = split_vertical(bottom)
		if left.get_height()>1: split(left)
		if right.get_height()>1: split(right)


def split_horizontal(board):
	split = random.randint(1, board.get_height()-1)
	opening = random.randint(0, board.get_width()-1)

	for cell in range(board.get_width()):
		if cell != opening:
			board.get_cell(cell, split).set_wall_n(board, True)

	top_board = board.get_subboard(0, board.get_width()-1, 0, split-1)
	visualize(top_board)
	top_board.get_cell(opening, top_board.get_height() - 1).set_wall_s(board, False)

	bottom_board = board.get_subboard(0, board.get_width()-1, split+1, board.get_height()-1)
	bottom_board.get_cell(opening, 0).set_wall_n(board, False)
	visualize(bottom_board)

	return top_board, bottom_board



def split_vertical(board):
	split = random.randint(1, board.get_width() - 1)
	opening = random.randint(0, board.get_height() - 1)

	for cell in range(board.get_height()):
		if cell != opening:
			board.get_cell(split, cell).set_wall_w(board, True)

	left_board = board.get_subboard(0, split, 0, board.get_height()-1)
	left_board.get_cell(split-1, opening).set_wall_e(board, False)
	visualize(left_board)

	right_board = board.get_subboard(split+1, board.get_width()-1, 0, board.get_height()-1)
	right_board.get_cell(0, opening).set_wall_w(board, False)
	visualize(right_board)


	return left_board, right_board


"""
		left_board = Board(width, split - 1)
		left_board.get_cell(opening, left_board.get_height() - 1).set_wall_s(self, False)

		right_board = Board(width, height - (split - 1))
		right_board.get_cell(opening, 0).set_wall_n(self, False)

		return left_board, right_board
"""
