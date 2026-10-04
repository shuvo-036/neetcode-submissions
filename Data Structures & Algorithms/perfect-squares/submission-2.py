class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float("inf")] * (n+1)

        dp[0] = 0

        for num in range(1, n+1):
            for i in range(1, int(n ** 0.5)+1):
                squre = i*i
                dp[num] = min(dp[num], 1 + dp[num - squre])
            
        return dp[n]





