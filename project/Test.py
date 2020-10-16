from Board import Board
from Visualizer import visualize
from Wallfollower import wallfollower


def main():
	board = Board(20, 20)
	visualize(board)

	start_x = 2
	start_y = 2
	wallfollower(board, start_x, start_y)
	visualize(board)


if __name__ == '__main__':
	main()