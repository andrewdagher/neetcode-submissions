class Solution:
    def helper(self, row, col, rows, cols, grid):
        self.ones.add((row, col))
        
        if (row - 1) != -1:   # Check bounds 
            if grid[row - 1][col] == "1" and (row - 1, col) not in self.ones: # Check land and check visited
                self.helper(row - 1, col, rows, cols, grid)  # Recurse
        if (col - 1) != -1:
            if grid[row][col - 1] == "1" and (row, col - 1) not in self.ones:
                self.helper(row, col - 1, rows, cols, grid)
        if (row + 1) != rows:
            if grid[row + 1][col] == "1" and (row + 1, col) not in self.ones:
                self.helper(row + 1, col, rows, cols, grid)
        if (col + 1) != cols:
            if grid[row][col + 1] == "1" and (row, col + 1) not in self.ones:
                self.helper(row, col + 1, rows, cols, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0
        self.ones = set()
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in self.ones:
                    self.helper(row, col, rows, cols, grid)
                    self.islands += 1
        return self.islands
        
    
