class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num:
                return False
        for x in range(9):
            if self.grid[x][col] == num:
                return False
        st_row = (row // 3) * 3
        st_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[st_row + i][st_col + j] == num:
                    return False   
        return True
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None
    def solve(self):
        empty_cell = self.find_empty()    
        if not empty_cell:
            return True       
        row, col = empty_cell        
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num                
                if self.solve():
                    return True
                self.grid[row][col] = 0       
        return False
    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
# Example usage
def main():
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solver = SudokuSolver(sudoku_grid)
    
    print("Original Sudoku:")
    solver.print_grid()
    
    if solver.solve():
        print("\nSolved Sudoku:")
        solver.print_grid()
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
