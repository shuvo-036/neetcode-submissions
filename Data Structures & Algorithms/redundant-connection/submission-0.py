class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for i in range(len(edges)+1)]

        def dfs(node, target, visited):
            
            visited.add(node)
            if node == target:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False
            
        for u,v in edges:
            visited = set()

            if dfs(u,v,visited):
                return [u,v]

            graph[u].append(v)
            graph[v].append(u)

        return []