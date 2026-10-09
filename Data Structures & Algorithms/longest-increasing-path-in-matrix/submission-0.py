class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        row = len(matrix)
        col = len(matrix[0])

        ops = [(-1,0),(0,-1),(0,1),(1,0)]
        
        memo ={}

        def dfs(r,c):

            ans =1
            if (r,c) in memo:
                return memo[(r,c)]

            for dr,dc in ops:
                nr= r+ dr
                nc = c + dc

                if 0<= nr < row and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dfs(nr,nc))

            memo[(r,c)] = ans
            return ans


        res =0
        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r,c))
        
        return res