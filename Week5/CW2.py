import copy
import time

#Grids 1-5 are 2x2
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''
def check_section(section, n):

	if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
		return True
	return False


def get_squares(grid, n_rows, n_cols):

	squares = []
	for i in range(n_cols):
		rows = (i*n_rows, (i+1)*n_rows)
		for j in range(n_rows):
			cols = (j*n_cols, (j+1)*n_cols)
			square = []
			for k in range(rows[0], rows[1]):
				line = grid[k][cols[0]:cols[1]]
				square +=line
			squares.append(square)


	return(squares)


def check_solution(grid, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	n = n_rows*n_cols

	for row in grid:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows):
		column = []
		for row in grid:
			column.append(row[i])
		if check_section(column, n) == False:
			return False

	squares = get_squares(grid, n_rows, n_cols)
	for square in squares:
		if check_section(square, n) == False:
			return False

	return True

def possible_values_column(grid, row, column):
	possible_values = list(range(1, len(grid)+1))
	if grid[row][column] == 0:
		for i in range(len(grid)):
			if grid[i][column] in possible_values:
				possible_values.remove(grid[i][column])
		return possible_values
	else:
		return None
		
def possible_values_row(grid, row, column):
	possible_values = list(range(1, len(grid)+1))
	if grid[row][column] == 0:
		for i in range(len(grid)):
			if grid[row][i] in possible_values:
				possible_values.remove(grid[row][i])
		return possible_values
	else:
		return None

def possible_values_square(grid, n_rows, n_cols, row, column):
	possible_values = list(range(1, len(grid)+1))
	squares = get_squares(grid, n_rows, n_cols)
	if grid[row][column] == 0:
		# Find the square that the cell is in
		for i in range(len(squares)):
			if row in range(n_rows*(i//n_rows), n_rows*(i//n_rows)+n_rows) and column in range(n_cols*(i%n_cols), n_cols*(i%n_cols)+n_cols):
				square = squares[i]
				break
		for i in square:
			if i in possible_values:
				possible_values.remove(i)
		return possible_values
	else:
		return None


def possible_values_combined(grid, n_rows, n_cols, row, column):
	possible_row_values = possible_values_row(grid,row,column)
	if possible_row_values == None:
		return None
	possible_column_values = possible_values_column(grid, row, column)
	if possible_column_values == None:
		return None
	possible_square_values = possible_values_square(grid, n_rows, n_cols, row, column)
	if possible_square_values == None:
		return None
	possible_values = []
	# Find the intersection of all three lists
	for i in possible_row_values:
		if i in possible_column_values and i in possible_square_values:
			possible_values.append(i)

	return possible_values
def recursive_solve(grid, n_rows, n_cols):

	#N is the maximum integer considered in this board
	# Replace all 0's with a list of all remaining possible values
	n = n_rows*n_cols
	solved = False
	it = 0
	while solved == False and it < 10:
		remaining = 0
		
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				possible_values = possible_values_combined(grid, n_rows, n_cols, i, j)
				if possible_values == None:
					continue
				elif len(possible_values) == 1:
					grid[i][j] = possible_values[0]
				else:
					grid[i][j] = possible_values
					remaining += 1
		# reset all lists to 0
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if type(grid[i][j]) == list:
					grid[i][j] = 0
		it += 1
		if remaining == 0:
			solved = True
			return grid
		elif it == 10:
			print("Too many iterations")
			return False
		

				
	
		

				


	return grid


def random_solve(grid, n_rows, n_cols, max_tries=500):

	for _ in range(max_tries):
		# Find a random cell that is not yet filled
		# If all cells are filled, return the grid
		# Otherwise, choose a random value from the list of possible values
		# and assign it to the cell
		
		pass

	return grid


def solve(grid, n_rows, n_cols):

	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''
	
	return recursive_solve(grid, n_rows, n_cols)
	#return recursive_solve(grid, n_rows, n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	for (i, (grid, n_rows, n_cols)) in enumerate(grids):
		print("Solving grid: %d" % (i+1))
		start_time = time.time()
		solution = solve(grid, n_rows, n_cols)
		elapsed_time = time.time() - start_time
		print("Solved in: %f seconds" % elapsed_time)
		print(solution)
		if check_solution(solution, n_rows, n_cols):
			print("grid %d correct" % (i+1))
			points = points + 10
		else:
			print("grid %d incorrect" % (i+1))

	print("====================================")
	print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
	main()

