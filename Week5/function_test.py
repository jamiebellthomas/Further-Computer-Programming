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

def possible_values_square(grid, n_rows, n_cols, row, column):
	# For a given cell, return a list of possible values for that cell based on the values in the square that the cell is in
    possible_values = list(range(1, len(grid)+1))
    squares = get_squares(grid, n_rows, n_cols)
    if grid[row][column] == 0:
        # Find the square that the cell is in
        index = (row//n_rows)*n_rows + column//n_cols
        square = squares[index]
        for i in square:
            if i in possible_values:
                possible_values.remove(i)
        return possible_values
	
grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]
print(get_squares(grid6, 2, 3))
print(possible_values_square(grid6, 2, 3, row=5, column=3))
