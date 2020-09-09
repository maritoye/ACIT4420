import random


def main():
	horizontal = int(input("What is the size in horizontal direction? "))
	vertical = int(input("What is the size in vertical direction? "))
	mines = int(input("How many mines should we have? "))

	solution = make_board(horizontal, vertical, mines)
	masked = make_board(horizontal, vertical, 0)

	play_game(solution, masked)



def make_board(horizontal, vertical, mines):
	board = [["?"] * horizontal for i in range(vertical)]

	if mines > 0:
		minecount = mines
		while minecount > 0:
			posy = random.randint(0, horizontal-1)
			posx = random.randint(0, vertical-1)
			if board[posx][posy] != "*":
				board[posx][posy] = "*"
				minecount -= 1

		for i in range(horizontal):
			for j in range(vertical):
				val = board[i][j]
				if val == "?":
					board[i][j] = str(neighbor_mine_count(board, i, j))

	return board


def neighbor_mine_count(board, x, y):
	subboard = []
	minecount = 0
	maxx = len(board)
	maxy = len(board[0])

	for i in range((x-1 if x-1 > -1 else 0), (x+2 if x+2 < maxx else maxx)):
		row = []
		for j in range((y-1 if y-1 > -1 else 0), (y+2 if y+2 < maxy else maxy)):
			row.append(board[i][j])
		subboard.append(row)

	for x in range(len(subboard)):
		for y in range(len(subboard[0])):
			if subboard[x][y] == "*":
				minecount += 1

	return minecount


def play_game(solution, masked):
	maskedboard = masked
	lost = False
	won = False

	while not lost and not won:
		print("To exit game write x")
		print("Bonus feature: To insert flag write f followed by coordinates separated by space. Example: 'f 1 1'")
		playermove = str(input("Enter coordinates separated by space: "))

		if playermove == "x":
			exit()

		# I added the option to put flags to make it more similar to the actual game
		if "f" in playermove:
			move = playermove.split()
			y = int(move[1]) - 1
			x = int(move[2]) - 1
			maskedboard[x][y] = "f"
			print_board(maskedboard)

		else:
			move = playermove.split()
			ymove = int(move[0]) - 1
			xmove = int(move[1]) - 1

			if solution[xmove][ymove] == "*":
				lost = True
			else:
				if maskedboard[xmove][ymove] == "?":
					maskedboard[xmove][ymove] = solution[xmove][ymove]
					won = check_win(maskedboard, solution)
					if won:
						print("You won!")
						print_board(solution)
						exit()
					print_board(maskedboard)

				else:
					print_board(maskedboard)
					print("You already opened this cell")

	if lost:
		print("You lost!")
		print_board(solution)
		exit()


def print_board(board):
	for j in range(len(board)):
		line = ""
		for i in range(len(board[0])):
			line += (str(board[j][i]) + " ")
		print(line)


def check_win(board, solution):
	win = 0

	for j in range(len(board)):
		for i in range(len(board[0])):
			if board[j][i] == "?" and solution[j][i] != "*":
				win += 1

	return True if win == 0 else False


if __name__ == '__main__':
	main()