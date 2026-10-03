class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        graph =[[] for i in range(n)]

        for u, v, wt in flights:
            graph[u].append((v,wt))
        
        distance =[float("inf")] * n
        distance[src] =0
        q = deque()
        q.append((src, 0,0))

        while q:
            city, cost, edge = q.popleft()

            if edge > k:
                continue
            
            for new_city, wt in graph[city]:
                new_cost = cost + wt

                if new_cost < distance[new_city]:
                    distance[new_city] = new_cost
                    q.append((new_city , new_cost, edge +1))
        
        if distance[dst] == float("inf"):
            return -1
        else:
            return distance[dst]













