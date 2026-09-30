from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m = len(heights)
        n = len(heights[0])

        matric =[[float("inf")] * n for _ in range(m)]
        matric[0][0] = 0

        hq = []
        heappush(hq,(0,0,0))
        ops =[(0,1),(1,0),(-1,0),(0,-1)]

        while hq:

            effort , row, col = heappop(hq)

            if row == m-1 and col == n-1:
                return effort

            if effort > matric[row][col]:
                continue

            for dr,dc in ops:
                nr,nc = row + dr , col + dc
                if 0 <= nr < m and 0 <= nc < n :
                    dist = abs(heights[row][col] - heights[nr][nc])

                    new_effort = max(dist, effort)

                    if new_effort < matric[nr][nc]:
                        heappush(hq,(new_effort,nr,nc))
                        matric[nr][nc] = new_effort
