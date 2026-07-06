class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row = len(grid)
        col = len(grid[0])

        q = deque()
        direction =[(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))


        while q:
            r,c = q.popleft()

            for dr , dc in direction:
                nr = r+dr
                nc = c+dc
                if nr <0 or nr >= row or nc <0 or nc >= col:
                    continue
                    
                if grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] +1

                q.append((nr,nc))
