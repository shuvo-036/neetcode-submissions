class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = [[] for i in range(numCourses)]

        indegre =[0] * (numCourses)

        for u, v in prerequisites:
            graph[u].append(v)
            indegre[v] +=1

        pre = [set() for i in range(numCourses)]

        q= deque()

        for i in range(numCourses):
            if indegre[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()

            for nei in graph[node]:
                pre[nei].add(node)

                for p in pre[node]:
                    pre[nei].add(p)

                indegre[nei] -=1
                if indegre[nei] ==0:
                    q.append(nei)
        
        res =[]
        for u,v in queries:
        
            if u in pre[v]:
                res.append(True)
            else:
                res.append(False)
        return res