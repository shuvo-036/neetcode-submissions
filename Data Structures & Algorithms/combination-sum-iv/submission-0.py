class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        n = len(nums)
        
        def solve(target):
            if target == 0:
                return 1

            res = 0
            for i in range(n):
                if nums[i] > target:
                    continue
                
                res += solve(target - nums[i])

            return res
        
        return solve(target)