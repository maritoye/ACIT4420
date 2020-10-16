from Board import Board
import pygame
from Solver import solve_gbfs
from Wallfollower import wallfollower


def main():
	global screen, clock

	height, width, start_x, start_y = get_user_input()

	board = Board(width, height)

	cell_size, height, width, margin, line = get_display(height, width)
	white = (250, 250, 250)

	pygame.init()
	screen = pygame.display.set_mode((width + margin*2 , height + margin*2))
	clock = pygame.time.Clock()
	screen.fill(white)

	update(board, cell_size, margin, line)
	pygame.display.update()
	wallfollower(board, start_x, start_y)
	update(board, cell_size, margin, line)


	while True:
		update(board, cell_size, margin, line)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		pygame.display.update()


def get_user_input():
	height = int(input("Height of the labyrinth: "))
	width = int(input("Width of the labyrinth: "))
	start_x = int(input("x position of start point when solving the labyrinth: ")) - 1
	start_y = int(input("y position of start point when solving the labyrinth: ")) - 1

	return height, width, start_x, start_y

def get_display(height, width):
	if (height < 40) and (width < 60):
		cell_size = 20
		height = height * cell_size
		width = width * cell_size
		margin = 50
		line = 3

	elif height > 200 or width > 350:
		cell_size = 2
		height = height * cell_size
		width = width * cell_size
		margin = 3
		line = 1

	elif height > 100 or width > 160:
		cell_size = 4
		height = height * cell_size
		width = width * cell_size
		margin = 5
		line = 1

	else:
		cell_size = 8
		height = height * cell_size
		width = width * cell_size
		margin = 5
		line = 2

	return cell_size, height, width, margin, line


def update(board, cell_size, margin, line):
	"""

	:param board:
	:param cell_size:
	:param margin:
	:param line:
	"""
	black = (0, 0, 0)
	green = (50, 130, 00)
	purple = (100, 0, 100)

	for y in range(board.get_height()):
		for x in range(board.get_width()):
			cell = board.get_cell(x, y)
			cell_rect = pygame.Rect(x*cell_size + margin, y*cell_size + margin, cell_size, cell_size)

			# set cell color is cell is in the final path
			#if cell.get_visited() and not cell.get_path():
			#	pygame.draw.rect(screen, green, cell_rect)

			# set cell color is cell is in the final path
			if cell.get_path():
				pygame.draw.rect(screen, purple, cell_rect)


			# set north wall, or blank
			if cell.get_wall_n():
				pygame.draw.line(screen, black, (x*cell_size + margin, y*cell_size + margin), ((x+1)*cell_size + margin, y*cell_size + margin), line)

			# set south wall, or blank
			if cell.get_wall_s():
				pygame.draw.line(screen, black, (x*cell_size + margin, (y+1)*cell_size + margin), ((x+1)*cell_size + margin, (y+1)*cell_size + margin), line)

			# set west wall, or blank
			if cell.get_wall_w():
				pygame.draw.line(screen, black, (x*cell_size + margin, y*cell_size + margin), (x*cell_size + margin, (y+1)*cell_size + margin), line)

			# set east wall, or blank
			if cell.get_wall_e():
				pygame.draw.line(screen, black, ((x+1)*cell_size + margin, y*cell_size + margin), ((x+1)*cell_size + margin, (y+1)*cell_size + margin), line)


if __name__ == '__main__':
	main()
