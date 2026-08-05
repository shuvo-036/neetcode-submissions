from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph =[[] for i in range(n+1)]

        for u, v,t in times:
            graph[u].append((v,t))

        dist = [float('inf')] * (n+1)
        dist[k] =0

        hp = [(0,k)]
        

        while hp:
            d , node = heappop(hp)

            if d > dist[node]:
                continue
            
            for nei, time in graph[node]:
                new_dist = d + time
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heappush(hp,(new_dist, nei))

        ans = max(dist[1:])

        if ans == float('inf'):
            return -1
        
        return ans