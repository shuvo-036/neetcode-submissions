from heapq import heappush, heappop
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        ans = 0
        heap =[(0,0)]
        n = len(points)
        visited = set()
        
        while len(visited) < n:
            
            cost , node = heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            ans += cost
            x1,y1  = points[node]

            for nei in range(n):
                if nei not in visited:
                    x2 , y2 = points[nei]

                    dist = abs(x1-x2) + abs(y1-y2)
                    heappush(heap,(dist,nei))
            
        return ans

             