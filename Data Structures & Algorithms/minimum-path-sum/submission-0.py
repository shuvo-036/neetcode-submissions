class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

       

        def solve(i,j):

            if i== row -1 and j == col -1:
                return grid[i][j]

            res = float("inf")

            if 0 <= i < row and 0 <= j <col:
                down = grid[i][j] + solve(i ,j + 1)
                right = grid[i][j] + solve(i+1,j)
            
                res = min(down ,right)
                return res
            return res
        return solve(0,0)