from Board import Board
from Cell import Cell

# Greedy Best First Search solver
def solve_gbfs(board, x, y):
	# Evaluation function = heuristic = manhattan distance = x+y distance from node to goal

	startcell = board.get_cell(x,y)
	open_cells = []
	closed_cells = []
	done = False

	open_cells.append(startcell)

	goal = None
	goal.solution = True
	goal.h = 0
	start.h = int(goal.x - start.x) + int(goal.y - start.y)
	start.cost = 0

	# start in cell with pos x,y in board
	# change colour of cell to path colour
	# make a list of all cells visited, and all cells in final solution
	while not done:
		if not open_cells:
			break
		current = open_cells.pop(0)
		closed_cells.append(current)
		if current.solution:
			return True
		build_children(current, board)
		for child in current.children:
			if child not in open_cells and child not in closed_cells:
				attach_and_evan(current, child) # check if child can lead to a better path
				open_cells.append(child)
				sorted(open_cells, key=lambda node: node.tot) # sorts the list by total estimates
			elif current.g < child.g:
				attach_and_evan(current, child) # check if child can lead to a better path
				if child in closed_cells:
					propagate(child)



def attach_and_evan(parent, child):
	"""
	Attaches the node to the so far best parent this node can have.
	Updates the cost of getting to this node (through its new parent)
	"""
	child.parent = parent
	child.g = parent.g + child.cost
	child.h = int(goal.x - child.x) + int(goal.y - child.y)
	child.tot = child.g + child.h

def propagate(cell):
	"""
	recurses through the possible descendants of the node.
	If path through this node is shorter for a child than its already known shortest path,
	this node is set as the new parent
	"""
	for child in cell.children:
		if cell.g < cell.g:
			child.parent = cell
			child.g = cell.g + child.cost
			propagate(child)


def build_children(cell):
	pass


def something(board, current, parent):
	children = []
	#find all children of this cell
	if not current.solution:
		# north
		if not current.get_wall_n():
			child = board.get_cell(board.get_cell(current.get_x(), current.get_y() - 1))
			if child != parent:
				children.append(child)

		# south
		if not current.get_wall_s():
			child = board.get_cell(board.get_cell(current.get_x(), current.get_y() + 1))
			if child != parent:
				children.append(child)

		# east
		if not current.get_wall_e():
			child = board.get_cell(board.get_cell(current.get_x()+1, current.get_y()))
			if child != parent:
				children.append(child)

		# west
		if not current.get_wall_w():
			child = board.get_cell(board.get_cell(current.get_x()-1, current.get_y()))
			if child != parent:
				children.append(child)

	if children: #if any children
		pass
	pass




