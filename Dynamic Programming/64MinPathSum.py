class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1]*len(grid[0]) for _ in range(len(grid))]
        n = len(grid) - 1 # row
        m = len(grid[0]) - 1 # col
        
        return self.findShortestPath(grid, memo, n, m)

    def findShortestPath(self, grid, memo, n, m):
        if memo[n][m] != -1:
            return memo[n][m]
        
        # not on last row
        if n == 0 and m == 0:
            memo[n][m] = grid[n][m]
        elif n == 0 and m > 0:
            memo[n][m] = grid[n][m] + self.findShortestPath(grid, memo, n, m-1)
        elif n > 0 and m == 0:
            memo[n][m] = grid[n][m] + self.findShortestPath(grid, memo, n-1, m)
        else:
            memo[n][m] = grid[n][m] + min(self.findShortestPath(grid, memo, n-1, m), self.findShortestPath(grid, memo, n, m-1))

        return memo[n][m]

