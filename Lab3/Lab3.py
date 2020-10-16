"""
Marit Øye Gjersdal
s348588
"""

import random


def main():
	horizontal = int(input("What is the size in horizontal direction? "))
	vertical = int(input("What is the size in vertical direction? "))
	mines = int(input("How many mines should we have? "))

	solution = make_board(horizontal, vertical, mines)
	masked = [[True] * horizontal for i in range(vertical)]
	play_game(solution, masked)


def make_board(horizontal, vertical, mines):
	"""
	creates a minesweeper game board, with the given size and given amount of mines.
	calculates the mine-count value for the cells surrounding the mines
	:param horizontal: int
	:param vertical: int
	:param mines: int
	:return: 2d array
	"""
	board = [["0"] * horizontal for i in range(vertical)]

	if mines > 0:
		minecount = mines
		while minecount > 0:
			posy = random.randint(0, horizontal-1)
			posx = random.randint(0, vertical-1)

			if board[posx][posy] != "*":
				# create mine at the random position if it was not already a mine
				board[posx][posy] = "*"

				# keeps count of how many mines are left to create
				minecount -= 1

				# increases the value of the neighboring cells with 1 (to represent their neighboring mine count)
				for i in range((posx - 1 if posx - 1 > -1 else 0), (posx + 2 if posx + 2 < len(board) else len(board))):
					for j in range((posy - 1 if posy - 1 > -1 else 0), (posy + 2 if posy + 2 < len(board[0]) else len(board[0]))):
						if board[i][j] != "*":
							board[i][j] = str(int(board[i][j]) + 1)

	return board


def play_game(solution, masked):
	"""
	To play the minesweeper game.
	Takes input from the user containing x and y position of a cell, unmasks the cell,
	checks if game has been lost or won. keeps doing this until game has been lost or won, or user writes "x"
	:param solution: 2d array of boolean values
	:param masked: 2d array of strings (containing * or number from 0-8)
	"""
	masked_board = masked
	lost = False
	won = False

	while not lost and not won:
		print("To exit game write x")
		player_move = str(input("Enter coordinates separated by space: "))

		if player_move == "x":
			exit()

		else:
			move = player_move.split()
			ymove = int(move[0]) - 1
			xmove = int(move[1]) - 1

			# if player chose a mine they lose
			if solution[xmove][ymove] == "*":
				print("You lost!")
				print_board(solution)
				lost = True

			else:
				# if the chosen cell was masked: unmask it and check if the game was won
				if masked_board[xmove][ymove]:
					masked_board[xmove][ymove] = False
					if check_win(masked_board, solution):
						print("You won!")
						print_board(solution)
					else:
						print_masked(masked_board, solution)

				else:
					print_masked(masked_board, solution)
					print("You already opened this cell")


def print_board(board):
	"""
	Prints the given board
	:param board: 2d array of boolean values
	"""
	for j in range(len(board)):
		line = ""
		for i in range(len(board[0])):
			line += (str(board[j][i]) + " ")
		print(line)


def print_masked(masked, solution):
	"""
	Prints the unmasked cells (given by masked 2d array) in the solution, the rest is printed as "?"
	:param masked: 2d array of strings (containing * or number from 0-8)
	:param solution: 2d array of boolean values
	"""
	for j in range(len(solution)):
		line = ""
		for i in range(len(solution[0])):
			if not masked[j][i]:
				line += (str(solution[j][i]) + " ")
			else:
				line += "? "
		print(line)


def check_win(masked, solution):
	"""
	If the masked board has yet to unmask a cell that is not a bomb in the solution, the game has not been won
	:param masked: 2d array of strings (containing * or number from 0-8)
	:param solution: 2d array of boolean values
	:return: boolean value
	"""
	won = True

	for j in range(len(solution)):
		for i in range(len(solution[0])):
			if masked[j][i] and solution[j][i] != "*":
				won = False

	return won


if __name__ == '__main__':
	main()