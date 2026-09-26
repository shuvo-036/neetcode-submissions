class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        degree = [0] *(n+1)

        for u,v in trust:
            degree[u] -=1
            degree[v] +=1
        
        for i in range(1, n+1):
            if degree[i] == n-1:
                return i
        return -1