class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        opa =[(-1,0),(0,-1),(1,0),(0,1)]

        def dfs(r,c):

            grid[r][c] = 0
            max_area = 1

            for dr,dc in opa:
                nr, nc = dr +r , c + dc

                if 0 <= nr < row  and 0 <= nc < col and grid[nr][nc] == 1:
                    max_area += dfs(nr,nc)

            return max_area

        max_area =0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area