class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n= len(nums)

        def solve(i, curr_some):

            if i == n:
                if curr_some == target:
                    return 1
                else:
                    return 0
                
            
            curr_some =0

            if nums[i] <= target:
                take = solve(i+1, curr_some -nums[i])
            
            not_take = solve(i+1, curr_some)

            return take + not_take
        
        return solve(0,0)