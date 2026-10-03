import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = set()

        hq = [(grid[0][0],0,0)]
        ops =[(-1,0),(0,-1),(0,1),(1,0)]

        while hq:

            time , row , col = heapq.heappop(hq)
            

            if (row, col) in visited:
                continue
            visited.add((row,col))
            if row == m-1 and col ==n-1:
                return time
            
            for dr, dc in ops:
                nr, nc = row + dr, col + dc
            
                if 0 <= nr <m and 0<= nc < n and (nr,nc) not in visited:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(hq,(new_time, nr,nc))








