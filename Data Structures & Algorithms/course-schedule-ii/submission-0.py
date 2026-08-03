class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph =[[] for i in range(numCourses) ]
        indegree = [0] * numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] +=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] ==0:
                q.append(i)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] ==0:
                    q.append(nei)

        if len(ans) != numCourses:
            return []
        return ans