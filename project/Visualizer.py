"""
input: an instance of Board (2d array of instances of Cell class)
"""

import pygame

def visualize(board):
	for y in range((board.get_height()+1)*2):
		for x in range((board.get_width()+1)*2):
			lab = [["+"] * x for i in range(y)]

	for y in range(board.get_height()):
		for x in range(board.get_width()):
			posx = ((x+1)*2)-1
			posy = ((y+1)*2)-1

			cell = board.get_cell(x,y)

			if cell.get_path():
				lab[posy][posx] = " p "

			elif cell.get_visited():
				lab[posy][posx] = " v "

			else:
				lab[posy][posx] = "   "

			
			# set north wall, or blank
			if cell.get_wall_n():
				lab[posy-1][posx] = "---"
			else:
				lab[posy-1][posx] = "   "

			# set south wall, or blank
			if cell.get_wall_s():
				lab[posy+1][posx] = "---"
			else:
				lab[posy+1][posx] = "   "

			# set west wall, or blank
			if cell.get_wall_w():
				lab[posy][posx-1] = "|"
			else:
				lab[posy][posx-1] = " "

			# set east wall, or blank
			if cell.get_wall_e():
				lab[posy][posx+1] = "|"
			else:
				lab[posy][posx+1] = " "

	for i in range(len(lab)):
		row = ""
		for j in range(len(lab[0])):
			row += lab[i][j]
		print(row)



def update(board):
	black = (0, 0, 0)

	for y in range(board.get_height()):
		for x in range(board.get_width()):
			cell = board.get_cell(x, y)

			# set north wall, or blank
			if cell.get_wall_n():
				pygame.draw.line(SCREEN, black, (x*20 + 50, y*20 + 50), ((x+1)*20 + 50, y*20 + 50), 3)

			# set south wall, or blank
			if cell.get_wall_s():
				pygame.draw.line(SCREEN, black, (x*20 + 50, (y+1)*20 + 50), ((x+1)*20 + 50, (y+1)*20 + 50), 3)

			# set west wall, or blank
			if cell.get_wall_w():
				pygame.draw.line(SCREEN, black, (x*20 + 50, y*20 + 50), (x*20 + 50, (y+1)*20 + 50), 3)

			# set east wall, or blank
			if cell.get_wall_e():
				pygame.draw.line(SCREEN, black, ((x+1)*20 + 50, y*20 + 50), ((x+1)*20 + 50, (y+1)*20 + 50), 3)



def fancy(board, height, width):
	global SCREEN, CLOCK
	white = (200, 200, 200)

	pygame.init()
	SCREEN = pygame.display.set_mode((height*20, width*20))
	CLOCK = pygame.time.Clock()
	SCREEN.fill(white)

	while True:
		drawGrid(height,width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()

def drawGrid(height,width):
	black = (0, 0, 0)

	blockSize = 20  # Set the size of the grid block
	for x in range(width*20):
		for y in range(height*20):
			rect = pygame.Rect(x * blockSize, y * blockSize,
								   blockSize, blockSize)
			pygame.draw.line(SCREEN, black, (10,20), (100,20),3)

