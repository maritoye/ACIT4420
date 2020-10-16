"""

"""
from Visualizer import visualize

order = ["n", "e", "s", "w"]


def wallfollower(board, x, y):
	"""

	:param board: the Board to be solved
	:param x: int - start position x for search
	:param y: int - start position y for search
	:return:
	"""
	start_cell = board.get_cell(x, y)
	start_cell.set_path(True)
	start_cell.set_visited(True)

	wall_direction = 0 # the current direction of walls we are trying to follow, in order list
	solved = False
	current = start_cell
	count = 0



	while not solved:
		# if cell has current wall direction wall: go to cell to the direction next in order_list then set neighbor as current
		count+=1

		neighbor_x, neighbor_y, wall_direction = next_cell(current, wall_direction, board)


		# if you go back to a cell previously visited, this cannot be the shortest path and will not be part of the solution
		if board.get_cell(neighbor_x, neighbor_y).get_path():
			current.set_path(False)

		board.get_cell(neighbor_x, neighbor_y).set_visited(True) # to mark the visited cells in the visualization
		board.get_cell(neighbor_x, neighbor_y).set_path(True) # to mark the visited cells in the visualization


		# check if solution was found, this will end the loop
		if board.get_cell(neighbor_x, neighbor_y).get_solution():
			solved = True

		current = board.get_cell(neighbor_x, neighbor_y)

	if solved:
		return True


def next_cell(current, d, board):
	"""
	finds a neighboring cell of the given cell, following the given direction and checking for neighbors
	in the order given by the order list
	:param current: instance of class Cell
	:param direction: int
	:return: instance of class Cell
	"""
	direction = d

	new_direction = 0

	if order[direction] == "n":
		wall = current.get_wall_n()

		if wall:
			new_direction = direction+1 if direction < 3 else 0

			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)

		elif not wall:
			neighbor_x, neighbor_y = current.get_x(), (current.get_y() - 1)
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction


	elif order[direction] == "e":
		wall = current.get_wall_e()

		if wall:
			new_direction = direction+1 if direction < 3 else 0

			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = (current.get_x() + 1) , current.get_y()
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction


	elif order[direction] == "s":
		wall = current.get_wall_s()

		if wall:
			new_direction = direction+1 if direction < 3 else 0

			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = current.get_x(), (current.get_y() + 1)
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction


	elif order[direction] == "w":
		wall = current.get_wall_w()

		if wall:
			new_direction = direction+1 if direction < 3 else 0

			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = (current.get_x() - 1), current.get_y()

			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction

	return neighbor_x, neighbor_y, new_direction










