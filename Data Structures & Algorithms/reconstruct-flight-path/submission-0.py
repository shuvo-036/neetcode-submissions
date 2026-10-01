class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for src , des in tickets:
            graph[src].append(des)
        
        for src in graph:
            graph[src].sort(reverse = True)
        
        res = []

        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            
            res.append(src)
        
        dfs("JFK")
        
        res.reverse()
        return res