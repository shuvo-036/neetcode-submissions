class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if sum(nums) %2 !=0:
            return False

        target = sum(nums) //2
        
        dp =[[None] * (target+1) for _ in range(n+1)]

        def solve(i, target):
            
            if target ==0:
                return True

            if i >=n:
                return False
            
            if dp[i][target] is not None:
                return dp[i][target]

            take = False
            if nums[i] <= target:
                take = solve(i+1, target - nums[i])
                
            skip = solve(i+1, target)

            dp[i][target] = take or skip
            return dp[i][target]

        return solve(0, target)
