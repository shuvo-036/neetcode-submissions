class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        path =[]
        n = len(nums)
        visited =[False] * n

        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            
            for i in range(n):
                if visited[i] == True:
                    continue
                
                visited[i] = True
                
                path.append(nums[i])
                dfs()
                path.pop()
                visited[i] = False
        
        dfs()
        return ans
