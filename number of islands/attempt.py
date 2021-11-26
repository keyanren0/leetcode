class Solution:
    
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or not grid[i][j] or grid[i][j] == '0':
            return
        #print(grid)
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        numOfIsland = 0


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numOfIsland += 1
                    self.dfs(grid, i, j)

        return numOfIsland