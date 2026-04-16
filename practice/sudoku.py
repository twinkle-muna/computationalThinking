import numpy as np

sudoku_grid = [
            [0,0,8,0,0,0,0,1,6],
            [5,0,0,0,9,2,0,0,8],
            [0,0,0,1,0,0,0,0,0],
            [9,0,0,3,0,0,8,2,0],
            [0,2,0,0,0,0,0,7,0],
            [0,8,4,0,0,6,0,0,5],
            [0,0,0,0,0,3,0,0,0],
            [4,0,0,9,6,0,0,0,2],
            [1,6,0,0,0,0,7,0,0]
        ]

def is_valid(row_index, column_index, number):
    global sudoku_grid
    for n in range(0,9):
        if sudoku_grid[row_index][n] == number:
            return False
        
    for n in range(0,9):
        if sudoku_grid[n][column_index] == number:
            return False
        
    square_col = (column_index // 3) * 3
    square_row = (row_index // 3) * 3
    for n in range(0,3):
        for m in range(0,3):
            if sudoku_grid[square_row+n][square_col+m] == number:
                return False
    
    return True

def solve():
    global sudoku_grid
    for row in range(0,9):
        for column in range(0,9):
            if sudoku_grid[row][column] == 0:
                for number in (range(1,10)):
                    if is_valid(row, column, number):
                        sudoku_grid[row][column] = number
                        solve()
                        sudoku_grid[row][column] = 0
                return
            
    print(np.matrix(sudoku_grid))
    input('Press enter for more solutions')
    return 

solve()