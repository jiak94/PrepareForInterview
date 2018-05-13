class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
            
        x = len(grid)
        y = len(grid[0])
        res = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '1':
                    res += int(grid[i][j])
                    self.dfs(grid, i, j, x, y)
    
    def dfs(self, grid, i, j, x, y):
        if i < 0 or i >= x or j < 0 or j >=y or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        self.dfs(grid, i+1, j, x, y)
        self.dfs(grid, i-1, j, x, y)
        self.dfs(grid, i, j+1, x, y)
        self.dfs(grid, i, j-1, x, y)