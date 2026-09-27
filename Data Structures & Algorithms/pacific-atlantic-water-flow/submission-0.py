class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row = len(heights)
        col = len(heights[0])
        res =[]

        pecific = set()
        atlantic = set()
        ops=[(0,1),(-1,0),(0,-1),(1,0)]

        def dfs(r,c, visited):

            visited.add((r,c))

            for dr,dc in ops:
                nr = r+dr
                nc = c+ dc
                
                if (0 <= nr < row and 
                    0 <= nc < col and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
            
                    dfs(nr,nc, visited)

        for r in range(row):
            dfs(r, 0, pecific)
        
        for c in range(col):
            dfs(0, c, pecific)
        
        for r in range(row):
            dfs(r, col-1, atlantic)
        
        for c in range(col):
            dfs(row-1,c , atlantic)
        
        for r in range(row):
            for c in range(col):
                if (r,c) in pecific and (r,c) in atlantic:
                    res.append([r,c])
        return res

