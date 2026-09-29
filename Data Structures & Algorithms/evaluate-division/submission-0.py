class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        graph =defaultdict(list)

        for (u,v) ,val in zip(equations, values):
            graph[u].append((v,val))
            graph[v].append((u,1/val))
        
        

        def dfs(src, des, visited):

            if src == des:
                return 1.0

            visited.add(src)

            for nei,wt in graph[src]:
                if nei not in visited:
                    ans = dfs(nei,des,visited)
                    if ans != -1.0:
                        return ans * wt
            return -1
            
        res =[]
        for src , des in queries:
            if src not in graph or des not in graph:
                res.append(-1.0)
            elif src == des:
                res.append(1.0)
            else:
                visited = set()
                res.append(dfs(src,des,visited))
        
        return res