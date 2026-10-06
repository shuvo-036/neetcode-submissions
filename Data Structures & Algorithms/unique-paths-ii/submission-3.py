class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n =len(obstacleGrid[0])

        memo ={}

        def solve(start, end):

            if not (0 <= start < m and 0 <= end < n):
                return 0

            if obstacleGrid[start][end] == 1:
                return 0

            if start == m-1 and end == n-1:
                return 1

            if (start, end) in memo:
                return memo[(start, end)]

            right = solve(start, end + 1)
            down = solve(start + 1, end)

            memo[(start, end)] = right + down

            return memo[(start, end)]
        return solve(0,0)