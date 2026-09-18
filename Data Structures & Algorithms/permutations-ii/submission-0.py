class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res =[]
        path =[]
        visited =[False] * n

        def solve(i):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if visited[i] == True:
                    continue
                
                if i >0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                path.append(nums[i])
                visited[i] = True
                solve(i+1)

                path.pop()
                visited[i] = False
        solve(0)
        return res