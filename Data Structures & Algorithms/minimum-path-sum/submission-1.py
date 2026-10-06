class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        memo ={}

        def solve(i,j):

            if i== row -1 and j == col -1:
                return grid[i][j]

            
            if (i,j) in memo:
                return memo[(i,j)]

            if 0 <= i < row and 0 <= j <col:
                down = grid[i][j] + solve(i ,j + 1)
                right = grid[i][j] + solve(i+1,j)
            
                memo[(i,j)] = min(down ,right)
                return memo[(i,j)]
            return float("inf")
        return solve(0,0)