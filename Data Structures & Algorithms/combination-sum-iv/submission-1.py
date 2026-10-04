class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        n = len(nums)
        memo ={}
        def solve(target):
            if target == 0:
                return 1

            if target in memo:
                return memo[target]

            res = 0
            for i in range(n):
                if nums[i] > target:
                    continue
                
                res += solve(target - nums[i])

            memo[target] = res
            return res
        
        return solve(target)