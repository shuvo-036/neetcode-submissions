class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n =len(obstacleGrid[0])

        memo ={}

        def solve(start, end):
            if start == m-1 and end ==n-1:
                return 1
            
            if (start,end) in memo:
                return memo[(start, end)]
            
            if 0 <= start < m and 0 <= end < n and obstacleGrid[start][end] ==0:

                right = solve(start + 1,end)
                down = solve(start, end+1)

                memo[(start, end)] = right +down
                return memo[(start, end)]

            memo[(start, end)] =0
            return 0
        return solve(0,0)