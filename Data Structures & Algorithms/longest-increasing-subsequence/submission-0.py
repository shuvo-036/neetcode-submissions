class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [[-1]*(n+1) for _ in range(n+1)]
        def dfs(i,p):
            
            if i >=n:
                return 0

            if dp[i][p] != -1:
                return dp[i][p]

            take =0

            if p == -1 or nums[p] < nums[i]:
                dp[i][p] = 1 + dfs(i+1, i)
                take =dp[i][p]
                
            dp[i][p] = dfs(i+1,p)
            skip = dp[i][p]

            dp[i][p] = max(take , skip) 
            return dp[i][p]
        return dfs(0,-1)