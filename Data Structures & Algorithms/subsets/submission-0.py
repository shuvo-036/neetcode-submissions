class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res =[]

        def solve(i, path):
            if i == len(nums):
                res.append(path[:])
                return 
            
            path.append(nums[i])
            solve(i + 1 , path)
            path.pop()
            solve(i+1,path)
        solve(0,[])
        return res