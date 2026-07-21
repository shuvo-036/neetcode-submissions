class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res=[]
        path =[]

        def solve(i):
            if i == len(nums):
                res.append(path[:])
                return 

            path.append(nums[i])
            solve(i+1)
            path.pop()

            idx =i+1
            while idx < len(nums) and nums[idx] == nums[idx-1]:
                idx +=1
            
            solve(idx)
        
        solve(0)
        return res