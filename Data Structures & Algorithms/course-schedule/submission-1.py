class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =[[] for _ in range(numCourses)]
        indegree = [0] *numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] +=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        count =0
        while q:
            node = q.popleft()
            count +=1
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] ==0:
                    q.append(nei)
        
        return count == numCourses